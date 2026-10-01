# -*- coding: utf-8 -*-
"""
Build the French, German and Italian trees from the built English site.

Run AFTER tools/build-pages.py:

    python3 tools/build-pages.py && python3 tools/i18n_build.py

WHY IT WORKS ON THE OUTPUT
    The chrome is lifted out of index.html and the page bodies live in big HTML
    constants in build-pages.py. Threading a language through all of that would
    have meant touching every one of its 1400 lines. Translating the built HTML
    instead means the generator stays monolingual and there is exactly one
    place where a language can go wrong.

WHY IT SPLICES BY OFFSET
    It finds the byte range of each translatable unit and replaces that range,
    rather than parsing the document and writing it back out. Re-serialising
    would reformat markup that has been tuned by hand, and every diff would be
    unreadable. What comes out differs from the English only where a string
    changed.

SAFETY
    - A translation must contain the same inline tags as its source. A dropped
      <strong> or <a> is an error, not a warning: it would ship a link-less
      sentence or an unstyled one.
    - A language is written only at 100% coverage (i18n.PUBLISH). Half a
      translation is worse than none.
    - Links keep English paths in i18n.py; they are prefixed here. So no
      translation can hard-code /de/ and rot when a page is renamed.
"""
import os
import re
import sys
import glob
import io
import json as _json
import hashlib
import datetime
import html as _html
import shutil
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content
import i18n
from i18n_extract import unit_spans, meta_units, skip
from paths import rootify_assets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The same origin the page generator uses, and imported rather than repeated.
# It was declared here as its own literal, and a drill -- change the domain in
# one place and rebuild -- showed what that costs: og:image and the JSON-LD
# followed the new host while every canonical, every hreflang and all 960
# sitemap entries stayed on the old one, because THIS file writes those three
# and had its own copy of the answer. Two constants with the same name in two
# files is not one place.
from paths import ORIGIN  # noqa: E402

# Pages that make up the site, relative to the repo root.
def source_pages():
    out = []
    for pat in ("*.html", "news/*.html", "services/*.html", "sectors/*.html",
                "projects/*.html"):
        out += sorted(glob.glob(os.path.join(ROOT, pat)))
    keep = []
    for f in out:
        rel = os.path.relpath(f, ROOT)
        if rel.split(os.sep)[0] in i18n.LANGS and rel.split(os.sep)[0] != "en":
            continue
        keep.append(rel.replace(os.sep, "/"))
    return keep


TAG_RE = re.compile(r"<\s*([a-zA-Z][a-zA-Z0-9]*)")


def tag_bag(s):
    """Multiset of inline tags in a unit, for parity checking."""
    bag = {}
    for m in TAG_RE.finditer(s):
        t = m.group(1).lower()
        bag[t] = bag.get(t, 0) + 1
    return bag


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


# ============================================================
# link rewriting
# ============================================================
LINK_RE = re.compile(r'((?:href|action)=")(/[^"#?]*)([^"]*)(")')


def langs_for(rel):
    """The published languages that actually have this page.

    Every place that used to read `[l for l in LANGS if PUBLISH[l]]` reads this
    instead. A language covering part of the site would otherwise be offered in
    the switcher on all 41 pages and declared as an hreflang alternate on all
    of them -- 40 links and 40 alternates to pages that do not exist."""
    return [l for l in i18n.LANGS
            if i18n.PUBLISH.get(l) and i18n.covers(l, rel)]


def rel_for_path(path):
    """The source page a site-internal path refers to.

    /            -> index.html
    /company     -> company.html
    /news/       -> news/index.html
    /404.html    -> 404.html
    Needed because prefixing has to know whether the target exists in this
    language, and the only handle on that is the source filename."""
    if path in ("", "/"):
        return "index.html"
    p = path.strip("/")
    if p.endswith(".html"):
        return p
    return p + "/index.html" if path.endswith("/") else p + ".html"


def prefix_links(body, lang):
    """Prefix site-internal paths with the language directory -- but only for
    pages this language actually has.

    A partial language is the reason for the second half. Russian covers the
    careers page; its header and footer link to twenty-seven other places, and
    prefixing those would have produced /ru/company, /ru/services and so on --
    every one a 404, on the one page whose whole job is to be read by somebody
    who came to apply. Unprefixed, they lead to the English pages, which exist.

    The four full languages are unaffected: covers() is true for every page, so
    every link is prefixed exactly as before."""
    if lang == i18n.DEFAULT:
        return body

    def repl(m):
        pre, path, tail, post = m.groups()
        if path.startswith(i18n.SHARED_PREFIXES):
            return m.group(0)
        if not i18n.covers(lang, rel_for_path(path)):
            return m.group(0)
        if path == "/":
            return pre + "/" + lang + "/" + tail + post
        return pre + "/" + lang + path + tail + post

    return LINK_RE.sub(repl, body)


def lang_url(lang, rel):
    """Absolute URL of a page in a given language. rel is like
    'company.html' or 'news/index.html'."""
    p = rel
    if p.endswith("index.html"):
        p = p[:-len("index.html")]
    elif p.endswith(".html") and p != "404.html":
        # clean URLs: /company, not /company.html. GitHub Pages serves both, so
        # the canonical and the hreflang set have to name the one we link to.
        p = p[:-len(".html")]
    p = "/" + p
    if p == "/index.html":
        p = "/"
    if lang == i18n.DEFAULT:
        return ORIGIN + p
    return ORIGIN + "/" + lang + p


# ============================================================
# the switcher
# ============================================================
def switcher(lang, rel, extra_class=""):
    langs = langs_for(rel)
    if len(langs) < 2:
        return ""            # nothing to switch between: render nothing
    out = []
    for lg in langs:
        href = lang_url(lg, rel).replace(ORIGIN, "") or "/"
        cur = ' aria-current="true"' if lg == lang else ""
        out.append(
            '<a href="%s" hreflang="%s" lang="%s"%s><span class="sr-only">%s</span>'
            '<span aria-hidden="true">%s</span></a>'
            % (href, i18n.LOCALE[lg][0], i18n.LOCALE[lg][0], cur,
               _html.escape(i18n.LANG_NAME[lg]), i18n.LABEL[lg]))
    return "".join(out)


LANGS_SLOT_RE = re.compile(
    r'(<div class="langs[^"]*" data-langs[^>]*>)(.*?)(</div>)', re.S)


def fill_switcher(body, lang, rel):
    def repl(m):
        open_tag = m.group(1)
        # the group label is itself translated
        open_tag = re.sub(r'aria-label="[^"]*"',
                          'aria-label="%s"' % _html.escape(i18n.LANG_GROUP[lang]),
                          open_tag)
        return open_tag + switcher(lang, rel) + m.group(3)
    return LANGS_SLOT_RE.sub(repl, body)


# ============================================================
# head: lang, canonical, alternates, og:locale
# ============================================================
def alternates(rel):
    langs = langs_for(rel)
    if len(langs) < 2:
        return ""
    out = []
    for lg in langs:
        out.append('  <link rel="alternate" hreflang="%s" href="%s">'
                   % (i18n.LOCALE[lg][0], lang_url(lg, rel)))
    out.append('  <link rel="alternate" hreflang="x-default" href="%s">'
               % lang_url(i18n.DEFAULT, rel))
    return "\n".join(out) + "\n"


def fix_head(body, lang, rel):
    # <html lang="en"> -> the page's language
    body = re.sub(r'(<html[^>]*\blang=")[^"]*(")',
                  lambda m: m.group(1) + i18n.LOCALE[lang][0] + m.group(2),
                  body, count=1)
    # canonical and og:url point at this language's URL
    body = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
                  lambda m: m.group(1) + lang_url(lang, rel) + m.group(2),
                  body, count=1)
    body = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
                  lambda m: m.group(1) + lang_url(lang, rel) + m.group(2),
                  body, count=1)
    body = re.sub(r'(<meta property="og:locale" content=")[^"]*(")',
                  lambda m: m.group(1) + i18n.LOCALE[lang][1] + m.group(2),
                  body, count=1)
    # The page preloads the two latin subsets. Russian sets its body text in
    # Montserrat (Poppins has no Cyrillic), so Poppins is never used on that
    # page and the Cyrillic subset is the one the first paint waits for.
    if lang == "ru":
        body = body.replace(
            '<link rel="preload" as="font" type="font/woff2" '
            'href="/assets/fonts/poppins-latin.woff2" crossorigin>',
            '<link rel="preload" as="font" type="font/woff2" '
            'href="/assets/fonts/montserrat-cyrillic.woff2" crossorigin>')
    # drop any alternates from a previous run, then add this page's
    body = re.sub(r'^[ \t]*<link rel="alternate" hreflang="[^"]*"[^>]*>\n',
                  "", body, flags=re.M)
    alts = alternates(rel)
    if alts:
        body = re.sub(r'(<link rel="canonical"[^>]*>\n)',
                      lambda m: m.group(1) + alts, body, count=1)
    return body


# ============================================================
# translating one page
# ============================================================
# ============================================================
# THE JSON ISLAND ON /services
# ============================================================
# /services carries all twelve services as JSON so the panel can be re-rendered
# without a reload. unit_spans() does not look inside <script>, so that payload
# stayed English on every locale: the German page painted German, and the first
# click replaced it with English. Coverage reported 100% throughout, because the
# gate could not see the strings either -- which is the part worth fixing. The
# island is translated here AND counted in stats, so a future service added
# without its translation now fails the gate instead of shipping in English.
#
# Almost every string in the payload is already a unit: the same h1, lead and
# bullet text is rendered as HTML on that service's own page, so it was
# translated there. Only `deep` is a block of markup rather than one sentence,
# and that is handed to the same span-based substitution the page pass uses.

_ISLAND = re.compile(r'(<script type="application/json" id="srv-data">)(.*?)(</script>)',
                     re.S)


# ============================================================
# UNITS THE CLIENT CAN EDIT
# ============================================================
# i18n.CLIENT_COLLECTIONS says which collections the CMS hands to the client.
# A unit is his when its English text carries a value out of one of them --
# `in`, not `==`, because several of them are printed inside a longer line: a
# news category lands in "05 &middot; 25 Jul 2026 &middot; Industry" and an seo
# title inside "<title> ... ALPROJECTS Group". Edit the category and that whole
# line loses its key, so the whole line has to be allowed to fall back.
#
# Longest value first: "Industry" is a substring of "Industry news", and the id
# printed beside the unit should name the field that really produced it.
_CLIENT_INDEX = None


def _client_index():
    global _CLIENT_INDEX
    if _CLIENT_INDEX is None:
        pairs = []
        for name in i18n.CLIENT_COLLECTIONS:
            for cid, text in content.flatten(content.load(name)).items():
                if text.strip():
                    pairs.append((text, "%s.%s" % (name, cid)))
        pairs.sort(key=lambda pair: -len(pair[0]))
        _CLIENT_INDEX = pairs
    return _CLIENT_INDEX


# ============================================================
# TRANSLATIONS THE CLIENT CAN OWN
# ============================================================
# content/translations/<lang>.json holds, per content id, the translation and a
# fingerprint of the English it was made from. It exists because the client
# asked to be able to translate a vacancy into Russian, and the translations he
# would be writing lived in tools/lang_ru.py -- a Python file, which is the one
# thing this whole CMS is built to keep him out of. A translation is data; it
# belongs in data.
#
# The fingerprint is what makes an edit tellable from an omission:
#
#   fingerprint matches   use it
#   fingerprint differs   the English was edited after this was translated --
#                         fall back to English and say so. A stale translation
#                         can assert something that is no longer true, and on
#                         a page selling inspection work that is worse than an
#                         untranslated line.
#   no record             never translated; English, and on the work list
#
# tools/lang_*.py is left alone rather than migrated. 15 of the 93 client
# values also appear inside OTHER units -- "Shipbuilding" is a vacancy field
# and also sits in "Shipbuilding sector - ALPROJECTS Group" -- so deleting them
# from the string table would silently untranslate those. The two agree for
# every string nobody has edited, and the id-keyed one wins, so the redundancy
# costs nothing and the alternative was a list of exceptions.
_STORE = {}


def client_store(lang):
    """English text -> translation, plus the ids whose English was edited."""
    if lang not in _STORE:
        fresh, stale = {}, {}
        path = os.path.join(ROOT, "content", "translations", "%s.json" % lang)
        try:
            with io.open(path, encoding="utf-8") as fh:
                rec = _json.load(fh)
        except Exception:
            rec = {}
        for text, cid in _client_index():
            r = rec.get(cid)
            if not r or not r.get("t"):
                continue
            if r.get("en") == content.fingerprint(text):
                fresh[text] = r["t"]
            else:
                stale[cid] = text
        _STORE[lang] = (fresh, stale)
    return _STORE[lang]


def translate_unit(lang, key):
    """The string table first, then what the client owns.

    The table carries every unit on the site and is the normal answer. The
    store only ever has client-collection fields, and it is consulted second so
    that a page's own prose can never be overridden from the CMS."""
    dst = i18n.t(lang, key)
    if dst is not None:
        return dst
    return client_store(lang)[0].get(key)


def client_ids(key):
    """The content ids whose text this unit carries, longest match first."""
    return [cid for text, cid in _client_index() if text in key]


def note_missing(stats, key):
    """Record an untranslated unit as blocking, or as the client's to fill.

    His are kept separate so the gate can let the language through: he was
    promised a vacancy can go up without waiting for a translator, and one
    word edited in the CMS must not strand four languages with their old files
    still on disk."""
    ids = client_ids(key)
    if ids:
        stats["soft"][key] = ids
    else:
        stats["missing"].add(key)


def _sub_units(frag, lang, stats):
    """Substitute every translatable unit inside one HTML fragment."""
    spans, attr_spans = unit_spans(frag)
    edits = [(a, b, norm(frag[a:b]), True, False) for a, b in spans]
    for a0, b0, _name, val in attr_spans:
        if not any(s0 <= a0 and b0 <= e0 for s0, e0 in spans):
            edits.append((a0, b0, norm(_html.unescape(val)), False, True))
    for start, end, key, keep_ws, esc in sorted(edits, key=lambda e: -e[0]):
        if skip(key):
            continue
        stats["units"].add(key)
        if lang == i18n.DEFAULT:
            continue
        dst = translate_unit(lang, key)
        if dst is None:
            note_missing(stats, key)
            continue
        if tag_bag(key) != tag_bag(dst):
            stats["tag_mismatch"].append((key, dst, tag_bag(key), tag_bag(dst)))
            continue
        out = _html.escape(dst, quote=True) if esc else dst
        if keep_ws:
            raw = frag[start:end]
            out = (raw[:len(raw) - len(raw.lstrip())] + out
                   + raw[len(raw.rstrip()):])
        frag = frag[:start] + out + frag[end:]
    return frag


def _translate_string(val, lang, stats):
    """One payload value: a plain sentence, or markup to be walked."""
    if not val or not val.strip():
        return val
    key = norm(val)
    if not skip(key) and "<" not in val:
        stats["units"].add(key)
        if lang == i18n.DEFAULT:
            return val
        dst = translate_unit(lang, key)
        if dst is None:
            dst = i18n.t_clamped(lang, key)
        if dst is None:
            note_missing(stats, key)
            return val
        return dst
    return _sub_units(val, lang, stats)


def translate_island(body, lang, stats):
    m = _ISLAND.search(body)
    if not m:
        return body
    try:
        data = _json.loads(m.group(2))
    except Exception:
        return body                      # malformed: leave it rather than lose it

    # Prose fields are named, not detected. The first version walked every
    # string in the payload and so offered `slug` to the translator: twelve
    # identifiers that indexOfSlug() and the address bar both depend on, which
    # would have made the panel unclickable in three languages the moment
    # somebody "translated" them. Naming the prose keys also means a new
    # machine-readable field is left alone by default rather than by luck.
    PROSE = ("h1", "lead", "deep", "points")

    def walk(node, key=None):
        if isinstance(node, dict):
            return dict((k, walk(v, k)) for k, v in node.items())
        if isinstance(node, list):
            return [walk(v, key) for v in node]
        if isinstance(node, str):
            return (_translate_string(node, lang, stats)
                    if key in PROSE else node)
        return node

    # The payload sits inside <script>, so the one sequence that could close the
    # element early is escaped. json.dumps gives no other way out of the tag.
    payload = _json.dumps(walk(data), ensure_ascii=False,
                          separators=(",", ":")).replace("</", "<\\/")
    return body[:m.start(2)] + payload + body[m.end(2):]


def translate_page(src, lang, rel, stats):
    body = src

    # 1-4. Everything that is a source range -- text units, <title>, meta copy
    # and translatable attributes -- is collected first and spliced in ONE pass
    # from the end of the document backwards. Doing them in separate passes
    # meant the second pass held offsets into a string the first pass had
    # already changed.
    spans, attr_spans = unit_spans(body)
    edits = []   # (start, end, key, preserve_ws, escape)

    for start, end in spans:
        edits.append((start, end, norm(body[start:end]), True, False))

    # an attribute inside a unit is part of that unit's markup and is the
    # translator's business there, not a separate string
    def inside_unit(a, b):
        return any(s0 <= a and b <= e0 for s0, e0 in spans)

    for a0, b0, name, val in attr_spans:
        if not inside_unit(a0, b0):
            edits.append((a0, b0, norm(_html.unescape(val)), False, True))

    m = re.search(r"<title>(.*?)</title>", body, re.S)
    if m:
        edits.append((m.start(1), m.end(1), norm(m.group(1)), False, False))

    for ms, me, tag, val in meta_units(body):
        i = tag.find('content="')
        if i >= 0:
            a0 = ms + i + len('content="')
            edits.append((a0, a0 + len(val), norm(_html.unescape(val)),
                          False, True))

    for start, end, key, keep_ws, esc in sorted(edits, key=lambda e: -e[0]):
        if skip(key):
            continue
        stats["units"].add(key)
        if lang == i18n.DEFAULT:
            continue
        dst = translate_unit(lang, key)
        if dst is None:
            dst = i18n.t_clamped(lang, key)
        if dst is None:
            note_missing(stats, key)
            continue
        src_bag, dst_bag = tag_bag(key), tag_bag(dst)
        if src_bag != dst_bag:
            stats["tag_mismatch"].append((key, dst, src_bag, dst_bag))
            continue
        out = _html.escape(dst, quote=True) if esc else dst
        if keep_ws:
            raw = body[start:end]
            lead = raw[:len(raw) - len(raw.lstrip())]
            trail = raw[len(raw.rstrip()):]
            out = lead + out + trail
        body = body[:start] + out + body[end:]
        stats["done"] += 1

    # The same five vacancies were marked up on all four language versions --
    # twenty JobPosting records for five real jobs, which Google is entitled to
    # read as duplicates. The English page keeps them; the translations carry the
    # human-readable cards and no structured data.
    if lang != i18n.DEFAULT:
        body = re.sub(
            r'  <script type="application/ld\+json">\n  \{(?:(?!</script>).)*?'
            r'"@type": "JobPosting"(?:(?!</script>).)*?\n  \}\n  </script>\n',
            "", body, flags=re.S)

    # 5. head, links, switcher
    body = fix_head(body, lang, rel)

    # The title block's SHEET field states which language sheet you are on.
    # That is state, like <html lang>, not copy: the extractor already skips a
    # bare "EN", so left alone it would print EN on every locale.
    # Tag-agnostic on purpose: this matched <span class="stamp-lang"> and the
    # markup became a <p> two edits later, so it silently stopped firing and
    # every locale printed EN. Matching the class rather than the element
    # cannot go stale the same way.
    body = re.sub(r'(<(\w+) class="stamp-lang">)[^<]*',
                  lambda m: m.group(1) + lang.upper(), body)

    body = translate_island(body, lang, stats)

    # The translation runs 15-25% longer than the English it replaced, so the
    # cut has to be made again on this side of it -- the English page can be
    # inside the limit while its German twin is 70 characters over.
    body = i18n.clamp_page_desc(body)
    # index.html is hand-authored with relative asset paths (assets/logo.svg).
    # At the root they resolve; under /fr/ they become /fr/assets/... and every
    # image, stylesheet and font 404s. Root-relative them BEFORE prefixing, or
    # prefix_links never sees them -- it only matches paths starting with "/".
    body = rootify_assets(body)
    body = prefix_links(body, lang)
    body = fill_switcher(body, lang, rel)
    return body


# ============================================================
# sitemap
# ============================================================
# ------------------------------------------------------------------
# lastmod, by content rather than by build
#
# Asking git when a page last changed does not work here: the cache-busting
# stamp rewrites every HTML file whenever the CSS or the JS changes, so git
# sees all 160 pages touched by the same commit and the sitemap ends up with
# one date on every URL -- which tells a crawler nothing and, once it
# notices, teaches it to ignore the field.
#
# So the date comes from a manifest of content hashes with the version
# stamps normalised out. A page whose text did not change keeps its date
# however many times the build runs. The manifest is committed; delete it
# and every page dates from today, which is wrong but not broken.
# ------------------------------------------------------------------
LASTMOD_DB = os.path.join(ROOT, "tools", "lastmod.json")
try:
    with io.open(LASTMOD_DB, encoding="utf-8") as fh:
        _seen = _json.load(fh)
except Exception:
    _seen = {}
_today = datetime.date.today().isoformat()
_dirty = [False]

def last_changed(rel):
    try:
        with io.open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            body = fh.read()
    except Exception:
        return _today
    body = re.sub(r"\?v=[0-9a-f]{6,}", "", body)
    # The footer's REV field prints this very date, so it has to come out
    # before the hash is taken. Left in, the date would change the hash that
    # decides the date: every build would move every page's REV, and the
    # manifest this function exists to keep would churn on every run.
    body = re.sub(r'(<p class="stamp-v" data-rev>)[^<]*', r"\1", body)
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
    rec = _seen.get(rel)
    if rec and rec.get("hash") == digest:
        return rec.get("date", _today)
    _seen[rel] = {"hash": digest, "date": _today}
    _dirty[0] = True
    return _today


def save_lastmod(pages=None):
    """Only earns its keep if it is written back and committed.

    `pages` is the set of English pages that still exist. Entries for anything
    else are dropped: a record deleted in the CMS otherwise leaves its hash and
    date in here for good, and the file grows by one dead entry per deletion
    until somebody notices. Called without the argument nothing is pruned, so a
    partial build cannot empty the manifest."""
    if pages is not None:
        dead = [rel for rel in _seen if rel not in pages]
        for rel in dead:
            del _seen[rel]
        if dead:
            _dirty[0] = True
            for rel in dead:
                print("  dropped %s from lastmod.json -- page no longer exists"
                      % rel)
    if _dirty[0]:
        with io.open(LASTMOD_DB, "w", encoding="utf-8") as fh:
            _json.dump(_seen, fh, indent=1, sort_keys=True)


def sitemap(pages):
    rows = []

    for rel in pages:
        if rel == "404.html":
            continue
        lastmod = last_changed(rel)
        # per page, because a language may cover only some of them: the careers
        # page has a Russian version and nothing else does, so only that page's
        # entries carry a Russian URL and a Russian alternate.
        langs = langs_for(rel)
        for lg in langs:
            alts = "".join(
                '\n    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                % (i18n.LOCALE[a][0], lang_url(a, rel)) for a in langs)
            # x-default: without it Google picks for itself which version to
            # show a visitor whose language the site does not have -- a Dutch or
            # Norwegian buyer, which is most of the market this site is for.
            alts += ('\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                     % lang_url(i18n.DEFAULT, rel))
            rows.append(
                "  <url>\n    <loc>%s</loc>%s\n    <lastmod>%s</lastmod>\n  </url>"
                % (lang_url(lg, rel), alts, lastmod))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")


# ============================================================
# main
# ============================================================
def main():
    force = "--force" in sys.argv
    pages = source_pages()
    print("%d English pages\n" % len(pages))

    reports = {}
    for lang in i18n.LANGS:
        stats = {"units": set(), "missing": set(), "done": 0,
                 "tag_mismatch": [], "soft": {}}
        outputs = {}
        for rel in pages:
            # A language covering part of the site translates only its own
            # pages, and its coverage is counted over those pages only --
            # otherwise Russian would report 24% and look unfinished when it is
            # complete for everything it is meant to cover.
            if not i18n.covers(lang, rel):
                continue
            with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
                src = fh.read()
            outputs[rel] = translate_page(src, lang, rel, stats)
        total = len(stats["units"])
        missing = len(stats["missing"])
        soft = len(stats["soft"])
        # Coverage counts BOTH buckets. The soft ones do not block the build,
        # but a page with an English vacancy on it is not 100% translated and
        # the number must not claim it is.
        cov = 100.0 * (total - missing - soft) / total if total else 100.0
        reports[lang] = (cov, total, missing, stats)

        if lang == i18n.DEFAULT:
            # English is rewritten in place: it needs the switcher and the
            # alternates too, and nothing else about it changes.
            for rel, out in outputs.items():
                with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as fh:
                    fh.write(out)
            print("  en  %d units  (source)" % total)
            continue

        # The gate counts the blocking bucket only: stats["soft"] holds the
        # units the client can edit, and those fall back to English one at a
        # time rather than holding back the language. See note_missing().
        complete = (missing == 0 and not stats["tag_mismatch"])
        # Two separate gates: the translation has to be finished, AND somebody
        # has to have turned the language on. Checking PUBLISH here rather than
        # after writing -- the first version wrote the tree and then the
        # cleanup below deleted it again, which looked like a build failure.
        ok = complete and i18n.PUBLISH.get(lang)
        if not (ok or force):
            why = ("ready -- set PUBLISH[%r] = True to ship it" % lang
                   if complete else
                   "%d/%d translated" % (total - missing, total))
            print("  %s  %5.1f%%  %s  -- NOT written%s"
                  % (lang, cov, why,
                     "  (%d tag mismatches)" % len(stats["tag_mismatch"])
                     if stats["tag_mismatch"] else ""))
            continue
        for rel, out in outputs.items():
            dst = os.path.join(ROOT, lang, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "w", encoding="utf-8") as fh:
                fh.write(out)
        print("  %s  %5.1f%%  %d files written%s"
              % (lang, cov, len(outputs),
                 "  -- %d unit(s) in English, see below" % soft if soft else ""))

    # A page the English build no longer produces must not survive in the
    # translated trees either. build-pages.py sweeps its own output; this is
    # the same sweep one level down, and without it a news item the client
    # deleted stays live in three languages while 404-ing in English.
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT:
            continue
        root = os.path.join(ROOT, lang)
        if not os.path.isdir(root):
            continue
        keep = {os.path.join(root, rel) for rel in pages if i18n.covers(lang, rel)}
        for dirpath, _dirs, names in os.walk(root):
            for name in names:
                if not name.endswith(".html"):
                    continue
                full = os.path.join(dirpath, name)
                if full not in keep:
                    os.remove(full)
                    print("  %s  removed %s -- gone from the source"
                          % (lang, os.path.relpath(full, ROOT)))

    # languages that are not published must not leave an old tree behind
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT:
            continue
        d = os.path.join(ROOT, lang)
        if os.path.isdir(d) and not i18n.PUBLISH.get(lang) and not force:
            shutil.rmtree(d)
            print("  %s  removed stale tree" % lang)

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap(pages))
    save_lastmod(set(pages))

    # what still needs writing
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT:
            continue
        cov, total, missing, stats = reports[lang]
        if stats["tag_mismatch"]:
            print("\n%s TAG MISMATCH -- translation must keep the source's tags:"
                  % lang.upper())
            for key, dst, a, b in stats["tag_mismatch"][:5]:
                print("   src %s\n     %s\n   dst %s\n     %s" %
                      (a, key[:80], b, dst[:80]))

    # The translator's work list. This is the whole point of separating the two
    # buckets: the client edits English in the CMS, the site keeps building, and
    # what he changed comes out here by content id -- a field to re-translate,
    # not a page to go hunting through.
    todo = {}
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT or not reports[lang][3]["soft"]:
            continue
        for key, ids in reports[lang][3]["soft"].items():
            todo.setdefault((ids[0], key), []).append(lang)
    if todo:
        print("\nIN ENGLISH ON THE TRANSLATED PAGES -- %d field(s) to send out:"
              % len(todo))
        for (cid, key), langs in sorted(todo.items()):
            print("   %-52s %s" % (cid, ",".join(langs)))
            print("       %s" % key[:96].replace("\n", " "))
        print("\n   These do not block a build: they are in %s, which the client\n"
              "   edits himself. Send the list to the translator; until it comes\n"
              "   back those units render in English on every other language."
              % ", ".join(i18n.CLIENT_COLLECTIONS))

    # Told apart from the list above, because they are a different job. There a
    # translator writes something new; here somebody already translated the
    # field and then the English under it changed, so what is on file may now
    # say something the English no longer says. The build will not print it as
    # a translation and will not use it.
    stale = {}
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT or not i18n.PUBLISH.get(lang):
            continue
        for cid in client_store(lang)[1]:
            stale.setdefault(cid, []).append(lang)
    if stale:
        print("\nTRANSLATED, THEN THE ENGLISH CHANGED -- %d field(s) to check:"
              % len(stale))
        for cid, langs in sorted(stale.items()):
            print("   %-52s %s" % (cid, ",".join(langs)))
        print("\n   The translation on file was made from different English. It is\n"
              "   not used -- a stale line can assert something that is no longer\n"
              "   true, which on these pages is worse than an untranslated one.")
    return reports


def failed(reports):
    """The languages that are published, unfinished, and therefore not written.

    This has to be an exit code, not a printed line. A withheld language leaves
    its previous files on disk -- that is deliberate, so a half-translated tree
    is never served -- but it means a deploy run straight after an incomplete
    build ships the old translations beside the new English and nothing says so.
    Once a GitHub Action does the deploying, the printed warning is read by
    nobody. The client's own collections are not counted here: those fall back
    per unit and are listed as work, not as a failure.
    """
    return [lang for lang in i18n.LANGS
            if lang != i18n.DEFAULT and i18n.PUBLISH.get(lang)
            and (reports[lang][2] or reports[lang][3]["tag_mismatch"])]


if __name__ == "__main__":
    _reports = main()
    _bad = failed(_reports)
    if _bad and "--force" not in sys.argv:
        print("\nBUILD FAILED -- %s published but not written. The site still has\n"
              "the previous files for %s, so deploying now would ship them beside\n"
              "the new English. Translate what is listed above, or pass --force."
              % (", ".join(_bad), ", ".join(_bad)))
        sys.exit(1)

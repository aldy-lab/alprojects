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
import html as _html
import shutil
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n
from i18n_extract import unit_spans, meta_units, skip
from paths import rootify_assets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGIN = "https://alprojects.co"

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


def prefix_links(body, lang):
    """Prefix site-internal paths with the language directory."""
    if lang == i18n.DEFAULT:
        return body

    def repl(m):
        pre, path, tail, post = m.groups()
        if path.startswith(i18n.SHARED_PREFIXES):
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
    langs = [l for l in i18n.LANGS if i18n.PUBLISH.get(l)]
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
    langs = [l for l in i18n.LANGS if i18n.PUBLISH.get(l)]
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
        dst = i18n.t(lang, key)
        if dst is None:
            stats["missing"].add(key)
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

    # 5. head, links, switcher
    body = fix_head(body, lang, rel)
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
def sitemap(pages):
    langs = [l for l in i18n.LANGS if i18n.PUBLISH.get(l)]
    import datetime
    import subprocess
    rows = []

    def last_changed(rel):
        """When this page actually changed, not when the build ran.

        One date across every URL tells a crawler nothing -- it cannot tell the
        page that changed today from the twenty-nine that did not. Taken from
        git, which knows; falls back to the file's mtime outside a checkout."""
        try:
            out = subprocess.check_output(
                ["git", "log", "-1", "--format=%cs", "--", rel],
                cwd=ROOT, stderr=subprocess.DEVNULL).decode().strip()
            if out:
                return out
        except Exception:
            pass
        try:
            return datetime.date.fromtimestamp(
                os.path.getmtime(os.path.join(ROOT, rel))).isoformat()
        except Exception:
            return datetime.date.today().isoformat()

    for rel in pages:
        if rel == "404.html":
            continue
        lastmod = last_changed(rel)
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
                 "tag_mismatch": []}
        outputs = {}
        for rel in pages:
            with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
                src = fh.read()
            outputs[rel] = translate_page(src, lang, rel, stats)
        total = len(stats["units"])
        missing = len(stats["missing"])
        cov = 100.0 * (total - missing) / total if total else 100.0
        reports[lang] = (cov, total, missing, stats)

        if lang == i18n.DEFAULT:
            # English is rewritten in place: it needs the switcher and the
            # alternates too, and nothing else about it changes.
            for rel, out in outputs.items():
                with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as fh:
                    fh.write(out)
            print("  en  %d units  (source)" % total)
            continue

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
        print("  %s  %5.1f%%  %d files written" % (lang, cov, len(outputs)))

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
    return reports


if __name__ == "__main__":
    main()

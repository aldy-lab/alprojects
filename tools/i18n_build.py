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
from i18n_extract import BLOCKS, INLINE, ATTRS, skip
from paths import rootify_assets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGIN = "https://alprojects.co"

# Pages that make up the site, relative to the repo root.
def source_pages():
    out = []
    for pat in ("*.html", "news/*.html", "services/*.html", "sectors/*.html"):
        out += sorted(glob.glob(os.path.join(ROOT, pat)))
    keep = []
    for f in out:
        rel = os.path.relpath(f, ROOT)
        if rel.split(os.sep)[0] in i18n.LANGS and rel.split(os.sep)[0] != "en":
            continue
        keep.append(rel.replace(os.sep, "/"))
    return keep


# ============================================================
# finding the translatable units, with their offsets
# ============================================================
class Locator(HTMLParser):
    """Records (start, end) source offsets of every block's inner HTML."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        # offset of the first character of each line
        self.line_start = [0]
        for line in src.splitlines(keepends=True):
            self.line_start.append(self.line_start[-1] + len(line))
        self.spans = []          # (start, end, inner_html)
        self._open = []          # [tag, depth, content_start]
        self._depth = 0

    def _off(self):
        ln, col = self.getpos()
        return self.line_start[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        self._depth += 1
        if tag in BLOCKS:
            start = self._off() + len(self.get_starttag_text() or "")
            self._open.append([tag, self._depth, start])

    def handle_startendtag(self, tag, attrs):
        pass  # self-closing: no inner html, and depth is unchanged

    def handle_endtag(self, tag):
        if self._open and self._open[-1][0] == tag and \
                self._open[-1][1] == self._depth:
            _, _, start = self._open.pop()
            end = self._off()
            self.spans.append((start, end, self.src[start:end]))
        self._depth -= 1


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

    # 1. block units, spliced back to front so offsets stay valid
    loc = Locator(body)
    loc.feed(body)
    for start, end, inner in sorted(loc.spans, key=lambda s: -s[0]):
        key = norm(inner)
        if skip(key):
            continue
        stats["units"].add(key)
        if lang == i18n.DEFAULT:
            continue
        dst = i18n.t(lang, key)
        if dst is None:
            stats["missing"].add(key)
            continue
        a, b = tag_bag(key), tag_bag(dst)
        if a != b:
            stats["tag_mismatch"].append((key, dst, a, b))
            continue
        # keep the source's leading/trailing whitespace so indentation survives
        lead = inner[:len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        body = body[:start] + lead + dst + trail + body[end:]
        stats["done"] += 1

    # 2. <title>
    m = re.search(r"<title>(.*?)</title>", body, re.S)
    if m:
        key = norm(m.group(1))
        if not skip(key):
            stats["units"].add(key)
            if lang != i18n.DEFAULT:
                dst = i18n.t(lang, key)
                if dst is None:
                    stats["missing"].add(key)
                else:
                    body = body[:m.start(1)] + dst + body[m.end(1):]
                    stats["done"] += 1

    # 3. translatable attributes
    attr_re = re.compile(
        r'\b(%s)="([^"]*)"' % "|".join(sorted(ATTRS, key=len, reverse=True)))

    def attr_repl(m):
        name, val = m.group(1), m.group(2)
        key = norm(_html.unescape(val))
        if skip(key):
            return m.group(0)
        stats["units"].add(key)
        if lang == i18n.DEFAULT:
            return m.group(0)
        dst = i18n.t(lang, key)
        if dst is None:
            stats["missing"].add(key)
            return m.group(0)
        stats["done"] += 1
        return '%s="%s"' % (name, _html.escape(dst, quote=True))

    body = attr_re.sub(attr_repl, body)

    # 4. head, links, switcher
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
    today = datetime.date.today().isoformat()
    rows = []
    for rel in pages:
        if rel == "404.html":
            continue
        for lg in langs:
            alts = "".join(
                '\n    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                % (i18n.LOCALE[a][0], lang_url(a, rel)) for a in langs)
            rows.append(
                "  <url>\n    <loc>%s</loc>%s\n    <lastmod>%s</lastmod>\n  </url>"
                % (lang_url(lg, rel), alts, today))
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

        ok = (missing == 0 and not stats["tag_mismatch"])
        if not (ok or force):
            print("  %s  %5.1f%%  %d/%d translated  -- NOT written%s"
                  % (lang, cov, total - missing, total,
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

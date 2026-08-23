# -*- coding: utf-8 -*-
"""
Pull every translatable string out of the built English site.

Run this, not a hand-written list: the site is generated, so the only
trustworthy inventory of its copy is the HTML that actually shipped.

The unit of translation is a BLOCK element's inner HTML, not a text node.
"Offices in <strong>Lithuania</strong>, <strong>Poland</strong> and
<strong>Norway</strong> sit close to..." is one unit, tags included, because
French and German put those words in a different order and a translator
working on text-node fragments cannot move them.

    python3 tools/i18n_extract.py            # summary
    python3 tools/i18n_extract.py --dump     # every unit, as a Python dict
"""
import os
import re
import sys
import glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Never translate: technical values, proper nouns that stay put, code-ish text.
SKIP_EXACT = {
    "", "\u00b7", "\u2014", "\u2013", "/", "&middot;", "ALPROJECTS",
    "ALPROJECTS GROUP", "ALPROJECTS Group", "ISO", "EN", "FR", "DE", "IT",
    "B", "UAB", "LT", "DNV",
}
SKIP_RE = re.compile(
    r"^(?:"
    r"[\d\s,.:+\-\u2013\u2014/\u00d7x%()]*"   # pure numbers/punctuation
    r"|[A-Z]{1,4}[\s\-]?\d[\d\s\-:.]*"        # ISO 9001, EN 1090, 200X200
    r"|\d+\s*(?:min|mm|kg|m|h|t)"                 # units
    r"|[a-z0-9._%+\-]+@[a-z0-9.\-]+"              # emails
    r"|https?://\S+|/[\w\-/.#?=]*"               # urls and paths
    r"|\+?[\d\s()\-]{6,}"                       # phone numbers
    r")$", re.I)


def skip(s):
    t = re.sub(r"\s+", " ", s).strip()
    if not t or t in SKIP_EXACT:
        return True
    if SKIP_RE.match(t):
        return True
    # Test the visible text, not the markup: "<span></span>" is the burger
    # icon and has no copy in it, but "span" is letters and passed the test
    # below until the tags came off first.
    vis = re.sub(r"<[^>]*>", "", t)
    vis = re.sub(r"&[a-z]+;|&#\d+;", "", vis, flags=re.I).strip()
    if not vis or vis in SKIP_EXACT or SKIP_RE.match(vis):
        return True
    return not re.search(r"[A-Za-z\u00c0-\u024f]", vis)


# What counts as a unit
# ---------------------
# The first version listed the tags that could be units (p, h1, li, ...). That
# was wrong, and wrong in the worst way: the hero headline, every CTA button
# and the whole statistics row are not in any of those tags, so they were never
# extracted, never reported missing, and coverage read 100% while the page was
# still visibly English. A number that says "done" when it is not is worse than
# a low one.
#
# The rule now is structural, not a list: an element is a unit when it contains
# text and NO block-level descendant -- i.e. everything inside it is text or
# inline markup. That makes
#     <h1>We take the scope.<br>We also prove the work.</h1>   one unit
#     <a class="btn-solid">Send us the scope</a>               one unit
#     <div><b>300</b><span>certified specialists</span></div>  one unit
# and where such elements nest, the outermost one wins, so a sentence is never
# split at a tag boundary.
#
# <a> and <button> are the exception: they are unit BOUNDARIES. A link is a
# discrete label, and without this the mobile menu -- eight anchors and nothing
# else -- came out as one unit per page, so the same navigation had to be
# translated 31 times and each copy differed only by which link was current.
INLINE = {
    "a", "b", "strong", "i", "em", "span", "br", "small", "sup", "sub",
    "abbr", "code", "u", "s", "time", "mark", "wbr", "q", "cite", "bdi",
    "bdo", "data", "dfn", "kbd", "samp", "var", "ruby", "rt", "rp",
}
# NOT img. It is replaced content, not text: counting it as inline made
# <div class="euromap"><img ...><span class="pin">Norway</span></div> a single
# unit whose "translation" would have to carry the whole <img> tag. Treating it
# as a block leaves the pins as units and the alt text as an attribute.
# HTMLParser does not close these for us; without the list the element stack
# desynchronises at the first <br> and every span after it is wrong.
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}
# Never look inside these.
OPAQUE = {"script", "style", "svg", "template", "noscript", "head"}
# ...nor inside the language switcher: tools/i18n_build.py generates it, so
# extracting it would ask for a translation of markup the build already owns,
# and every page would report a dozen phantom missing units.
OPAQUE_ATTR = "data-langs"

# Attributes carrying user-facing text.
#
# NOT "value": <option value="Certified TIG Welder"> is what the form submits,
# and translating it would send the application in the visitor's language to a
# backend expecting one string. The option's visible text is a unit and is
# translated; the value stays English on purpose.
#
# NOT "content" in general: <meta content> carries "noindex", "#0a0a12",
# "summary_large_image" and "width=device-width" as often as it carries copy.
# Only the metas in META_TRANSLATE below are translated.
ATTRS = {"alt", "title", "aria-label", "placeholder", "aria-description"}

META_TRANSLATE = {
    "description", "og:title", "og:description", "og:image:alt",
    "twitter:title", "twitter:description",
}
META_RE = re.compile(r'<meta\b[^>]*>', re.I)


def meta_units(html):
    """(start, end, full_tag, content_value) for metas whose content is copy."""
    out = []
    for m in META_RE.finditer(html):
        tag = m.group(0)
        key = re.search(r'\b(?:name|property)="([^"]*)"', tag, re.I)
        val = re.search(r'\bcontent="([^"]*)"', tag, re.I)
        if key and val and key.group(1).lower() in META_TRANSLATE:
            out.append((m.start(), m.end(), tag, val.group(1)))
    return out


class Spans(HTMLParser):
    """Finds the source range of every translatable unit."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.line_start = [0]
        for line in src.splitlines(keepends=True):
            self.line_start.append(self.line_start[-1] + len(line))
        self.cands = []      # (start, end)
        self.attrs = []      # (start, end, name, value)
        # stack entries: [tag, content_start, has_text, has_block_child]
        self._st = []
        self._opaque = 0
        self._opaque_tag = None

    def _off(self):
        ln, col = self.getpos()
        return self.line_start[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        if self._opaque:
            if tag == self._opaque_tag:
                self._opaque += 1
            return
        if tag in OPAQUE or any(k == OPAQUE_ATTR for k, _ in attrs):
            self._opaque = 1
            self._opaque_tag = tag
            return
        raw = self.get_starttag_text() or ""
        for k, v in attrs:
            if k in ATTRS and v and not skip(v):
                i = raw.find('%s="' % k)
                if i >= 0:
                    a = self._off() + i + len(k) + 2
                    self.attrs.append((a, a + len(v), k, v))
        if tag in VOID:
            self._mark_inline(tag)
            return
        self._st.append([tag, self._off() + len(raw), False, False])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self._st and self._st[-1][0] == tag:
            self._st.pop()
            self._mark_inline(tag)

    BOUNDARY = {"a", "button"}

    def _mark_inline(self, tag):
        if self._st and tag not in INLINE:
            self._st[-1][3] = True

    def handle_endtag(self, tag):
        if self._opaque:
            if tag == self._opaque_tag:
                self._opaque -= 1
            return
        if tag in VOID:
            return
        # unwind to the matching tag; unbalanced markup must not desync us
        for i in range(len(self._st) - 1, -1, -1):
            if self._st[i][0] == tag:
                for _ in range(len(self._st) - 1 - i):
                    self._st.pop()
                name, cstart, has_text, has_block = self._st.pop()
                end = self._off()
                if has_text and not has_block:
                    self.cands.append((cstart, end))
                if self._st:
                    # A link's own text does not make its parent a unit: that
                    # is what stops a nav of eight anchors collapsing into one
                    # string. But a link must NOT mark the parent as a block --
                    # doing that lost every sentence with a link inside it,
                    # "Or write to <a>info@alprojects.eu</a>." among them,
                    # because the parent then qualified as neither.
                    if has_text and name not in self.BOUNDARY:
                        self._st[-1][2] = True
                    if has_block or name not in INLINE:
                        self._st[-1][3] = True
                return
        # stray close tag: ignore

    def handle_data(self, d):
        if not self._opaque and self._st and d.strip():
            self._st[-1][2] = True

    def _entity(self):
        if not self._opaque and self._st:
            self._st[-1][2] = True

    def handle_entityref(self, name):
        self._entity()

    def handle_charref(self, name):
        self._entity()


def unit_spans(src):
    """Outermost translatable spans, plus translatable attribute spans."""
    p = Spans(src)
    p.feed(src)
    p.close()
    cands = sorted(set(p.cands))
    out = []
    for a, b in cands:
        # drop anything nested inside another candidate: outermost wins
        if any(x <= a and b <= y and (x, y) != (a, b) for x, y in cands):
            continue
        if skip(re.sub(r"\s+", " ", src[a:b]).strip()):
            continue
        out.append((a, b))
    return out, p.attrs


def html_files():
    out = []
    for pat in ("*.html", "news/*.html", "services/*.html", "sectors/*.html"):
        out += sorted(glob.glob(os.path.join(ROOT, pat)))
    # language trees are output, never input
    return [f for f in out if not re.search(r"/(fr|de|it)/", f)]


def collect():
    seen, order, where = set(), [], {}
    for f in html_files():
        with open(f, encoding="utf-8") as fh:
            body = fh.read()
        # <title> and the meta description are translatable too
        for m in re.finditer(r"<title>(.*?)</title>", body, re.S):
            t = re.sub(r"\s+", " ", m.group(1)).strip()
            if not skip(t) and t not in seen:
                seen.add(t); order.append(t); where[t] = f
        for _, _, _, val in meta_units(body):
            t = re.sub(r"\s+", " ", val).strip()
            if not skip(t) and t not in seen:
                seen.add(t); order.append(t); where[t] = f
        p = Extract()
        p.feed(body)
        for _, v in p.units:
            if v not in seen:
                seen.add(v); order.append(v); where[v] = f
    return order, where


if __name__ == "__main__":
    units, where = collect()
    words = sum(len(u.split()) for u in units)
    if "--dump" in sys.argv:
        print("UNITS = [")
        for u in units:
            print("    %r," % u)
        print("]")
    else:
        print("%d translation units, %d words" % (len(units), words))
        longest = sorted(units, key=lambda u: -len(u))[:5]
        print("\nlongest units:")
        for u in longest:
            print("  (%d chars) %s..." % (len(u), u[:90]))
        print("\nshortest 10:")
        for u in sorted(units, key=len)[:10]:
            print("  %r" % u)

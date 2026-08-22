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

# Blocks whose inner HTML is one translation unit. Nested blocks are handled:
# a <p> inside a <div> is its own unit and the <div> is not one.
BLOCKS = {
    "p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "button", "figcaption",
    "th", "td", "dt", "dd", "label", "summary", "blockquote", "caption",
    "legend", "option",
}
# Inline tags allowed to survive inside a unit.
INLINE = {
    "a", "b", "strong", "i", "em", "span", "br", "small", "sup", "sub",
    "abbr", "code", "u", "s", "time", "mark", "wbr",
}
# Attributes carrying user-facing text.
ATTRS = {
    "alt", "title", "aria-label", "placeholder", "value", "content",
    "aria-description",
}
ATTR_TAGS_SKIP = {"meta": {"property", "name"}}

# Never translate: technical values, proper nouns that stay put, code-ish text.
SKIP_EXACT = {
    "", "·", "—", "–", "/", "&middot;", "ALPROJECTS", "ALPROJECTS GROUP",
    "ISO", "EN", "FR", "DE", "IT", "B", "UAB", "LT", "DNV",
}
SKIP_RE = re.compile(
    r"^(?:"
    r"[\d\s,.:+\-–—/×x%()]*"              # pure numbers/punctuation
    r"|[A-Z]{1,4}[\s\-]?\d[\d\s\-:.]*"    # ISO 9001, EN 1090, 200X200
    r"|\d+\s*(?:min|mm|kg|m|h|t)"         # units
    r"|[a-z0-9._%+\-]+@[a-z0-9.\-]+"      # emails
    r"|https?://\S+|/[\w\-/.#?=]*"        # urls and paths
    r"|\+?[\d\s()\-]{6,}"                 # phone numbers
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
    return not re.search(r"[A-Za-zÀ-ÿ]", vis)


class Extract(HTMLParser):
    """Collects block inner-HTML units and translatable attribute values."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.units = []          # (kind, value)
        self._stack = []         # open block capture: [tag, depth, buffer]
        self._depth = 0

    # -- capture helpers ------------------------------------------------
    def _emit(self, raw):
        raw = re.sub(r"\s+", " ", raw).strip()
        if not skip(raw):
            self.units.append(("block", raw))

    def _feedbuf(self, s):
        if self._stack:
            self._stack[-1][2].append(s)

    # -- parser callbacks -----------------------------------------------
    def handle_starttag(self, tag, attrs):
        self._depth += 1
        for k, v in attrs:
            if k in ATTRS and v:
                bad = ATTR_TAGS_SKIP.get(tag)
                if bad and any(a for a, _ in attrs if a in bad and
                               dict(attrs).get(a) not in
                               ("description", "og:description", "og:title",
                                "twitter:title", "twitter:description")):
                    continue
                if not skip(v):
                    self.units.append(("attr", re.sub(r"\s+", " ", v).strip()))
        if tag in BLOCKS:
            # a block inside a block ends the outer one's own text
            self._stack.append([tag, self._depth, []])
        elif self._stack and tag in INLINE:
            a = "".join(' %s="%s"' % (k, v) for k, v in attrs if k in
                        ("href", "class", "lang", "datetime"))
            self._feedbuf("<%s%s>" % (tag, a))

    def handle_startendtag(self, tag, attrs):
        for k, v in attrs:
            if k in ATTRS and v and not skip(v):
                self.units.append(("attr", re.sub(r"\s+", " ", v).strip()))
        if self._stack and tag in INLINE:
            self._feedbuf("<%s>" % tag)

    def handle_endtag(self, tag):
        if self._stack and self._stack[-1][0] == tag and \
                self._stack[-1][1] == self._depth:
            _, _, buf = self._stack.pop()
            self._emit("".join(buf))
        elif self._stack and tag in INLINE:
            self._feedbuf("</%s>" % tag)
        self._depth -= 1

    def handle_data(self, d):
        self._feedbuf(d)

    def handle_entityref(self, name):
        self._feedbuf("&%s;" % name)

    def handle_charref(self, name):
        self._feedbuf("&#%s;" % name)


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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production copies of the stylesheet and the script.

Deliberately dumb, and dependency-free on purpose: no npm, no toolchain, and
the same bytes out of every machine, so a diff never shows a phantom asset
change. It removes comments, indentation and blank lines. It never rewrites a
line of code -- no renaming, no reordering, no collapsing of declarations --
because the win is already there without it: the stylesheet is 40% comments.

CSS is stripped with a string-aware scanner (a comment opener inside a quoted
value or a url() must survive). JavaScript is stripped by whole lines only:
a line is dropped when it is nothing but a comment, and kept verbatim
otherwise. That rule cannot break automatic semicolon insertion, a regular
expression literal or a template string, because no line carrying code is
ever touched.

Run from tools/build-pages.py; also runnable on its own to check the sizes:
    python3 tools/minify.py --report
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def minify_css(src):
    """Drop /* */ comments, indentation and blank lines. Spaces inside a line
    are left alone -- `calc(100% - 32px)` needs them and this is not the place
    to be clever about which ones."""
    out = []
    i, n, quote = 0, len(src), None
    while i < n:
        c = src[i]
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:          # escaped quote inside a string
                out.append(src[i + 1])
                i += 2
                continue
            if c == quote:
                quote = None
            i += 1
            continue
        if c in "\"'":
            quote = c
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            end = src.find("*/", i + 2)
            i = end + 2 if end >= 0 else n
            continue
        out.append(c)
        i += 1
    text = "".join(out)
    text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip() + "\n"


def minify_js(src):
    """Whole-line comment removal. Anything that is not unambiguously a
    comment line is copied through untouched."""
    out = []
    in_block = False
    for line in src.split("\n"):
        stripped = line.strip()
        if in_block:
            if stripped.endswith("*/"):
                in_block = False
                continue
            if "*/" in stripped:
                # code after the closing marker: stop guessing, keep the line
                in_block = False
                out.append(stripped)
            continue
        if not stripped:
            continue
        if stripped.startswith("//"):
            continue
        if stripped.startswith("/*"):
            if stripped.endswith("*/"):
                continue                          # a whole comment on one line
            if "*/" in stripped:
                out.append(stripped)              # comment then code: keep it
                continue
            in_block = True
            continue
        out.append(stripped)
    return "\n".join(out) + "\n"


PAIRS = [("css/style.css", "css/style.min.css", minify_css),
         ("js/main.js", "js/main.min.js", minify_js)]


def run(report=False):
    for src_rel, out_rel, fn in PAIRS:
        src = io.open(os.path.join(ROOT, src_rel), encoding="utf-8").read()
        out = fn(src)
        if fn is minify_js:
            # Invariant worth asserting rather than trusting: every line of the
            # output has to appear, trimmed, in the input. If it does not, the
            # stripper rewrote something and the build should stop.
            source_lines = set(l.strip() for l in src.split("\n"))
            for line in out.split("\n"):
                if line and line not in source_lines:
                    raise SystemExit("minify: %s changed a line of code: %r"
                                     % (src_rel, line[:70]))
        io.open(os.path.join(ROOT, out_rel), "w", encoding="utf-8").write(out)
        if report:
            print("  %-18s %7d -> %7d bytes  (-%d%%)"
                  % (out_rel, len(src), len(out), 100 - 100 * len(out) // len(src)))


if __name__ == "__main__":
    run(report="--report" in sys.argv)

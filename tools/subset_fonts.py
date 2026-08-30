#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cut the web fonts down to the ranges this site actually sets.

The Montserrat latin-ext file arrived from Google Fonts as the whole extended
range -- 632 characters, 807 glyphs, 66.6 KB -- to deliver the four the site
needs today (E-dot, S-caron, u-ogonek). It is not lazy either: "KLAIPEDA" sits
in the hero eyebrow, so every page pays for it on the first screen, where the
LCP element is text and the fonts are what gate it.

The subset is Latin Extended-A entire (U+0100-017F), not the four characters
in use. Cutting to today's text is the same silent failure this repo keeps
running into: add a Lithuanian or Polish client name with one letter outside
the set and the browser drops that word to a system font mid-line, with
nothing to notice in a diff. Latin Extended-A covers every language the
company works in -- Lithuanian, Polish, Czech, Slovak, Hungarian, Croatian --
and costs 12 KB more than the minimum.

Run once, by hand, after replacing a font file:
    python3 tools/subset_fonts.py            # report only
    python3 tools/subset_fonts.py --write    # rewrite the files

Requires fonttools and brotli (pip3 install fonttools brotli). Not part of
build-pages.py: the fonts change when a typeface changes, which is roughly
never, and a build step that needs a dependency is a build step that breaks
on someone else's machine.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Latin Extended-A and nothing else. Extended-B (U+0180-024F) is 200 glyphs of
# African, Vietnamese and phonetic letters -- none of the markets the company
# works in -- and doubles the file. The dashes and quotes are already carried by
# the "latin" face, which declares U+2000-206F, so putting them here too would
# ship them twice.
EXT_RANGE = "U+0100-017F"

TARGETS = [
    ("assets/fonts/montserrat-latin-ext.woff2", EXT_RANGE),
    ("assets/fonts/poppins-latin-ext.woff2", EXT_RANGE),
    ("assets/fonts/poppins-500-latin-ext.woff2", EXT_RANGE),
]


def main(write=False):
    from fontTools import subset
    from fontTools.ttLib import TTFont

    total_before = total_after = 0
    for rel, unicodes in TARGETS:
        src = os.path.join(ROOT, rel)
        if not os.path.exists(src):
            print("  missing: %s" % rel)
            continue
        before = os.path.getsize(src)
        out = src + ".subset"
        subset.main([src,
                     "--flavor=woff2",
                     "--output-file=" + out,
                     "--unicodes=" + unicodes,
                     "--layout-features=*",   # keep kerning and ligatures
                     "--no-hinting",
                     "--desubroutinize"])
        after = os.path.getsize(out)
        font = TTFont(out, lazy=True)
        glyphs = font["maxp"].numGlyphs
        variable = "wght" if font.get("fvar") else "static"
        font.close()
        total_before += before
        total_after += after
        print("  %-38s %7.1f -> %6.1f KB   %4d glyphs   %s"
              % (os.path.basename(rel), before / 1024.0, after / 1024.0, glyphs, variable))
        if write:
            os.replace(out, src)
        else:
            os.unlink(out)
    print("  %-38s %7.1f -> %6.1f KB   (%.1f KB saved)%s"
          % ("total", total_before / 1024.0, total_after / 1024.0,
             (total_before - total_after) / 1024.0,
             "" if write else "   [report only -- pass --write]"))


if __name__ == "__main__":
    main(write="--write" in sys.argv)

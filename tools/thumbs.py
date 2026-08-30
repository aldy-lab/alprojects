#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Derive the /projects card covers from the opening plate of each case.

The card is a 4:3 window on to a photograph that is usually 3:4. Shipping the
whole plate and letting `object-fit: cover` throw away the top and bottom means
the browser downloads 1200x1600 to display 1200x900 -- 44% of every file
discarded before it is painted. Across seven cards on a 3x phone that was
1539 KB of card covers on one page.

So the crop happens here instead, once, and the card points at the result:

    01-1200.webp  1200x1600   the plate, untouched, used by the case page
    card-1200.webp  1200x900  the same crop the CSS was making anyway
    card-900.webp    900x675
    card-600.webp    600x450

Three widths rather than two because of where the card actually lands. On a
390px phone it measures 344 CSS px, so a 3x screen wants about 1030 real
pixels: with only 600 and 1200 on offer the browser has to take 1200 and six
of those load before the first scroll. 900 covers the same card at 2.6x, which
is past the point anyone can see, for a little over half the bytes.

The crop is centred, which is what `object-position: 50% 50%` does, so the
visible frame does not change -- only the bytes. Derived files: delete them and
this rebuilds them; the client's originals are never written to.

    python3 tools/thumbs.py           # only what is missing or stale
    python3 tools/thumbs.py --force   # all of them

Called from build-pages.py, so an added case gets its covers without anyone
remembering to run it.
"""

import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_DIR = os.path.join(ROOT, "assets", "projects", "cases")
RATIO = 4.0 / 3.0
WIDTHS = (1200, 900, 600)
# The card is a thumbnail, not the evidence, and these are files this script
# writes rather than anything the client sent -- so the quality is chosen by
# measurement, on the same rail tools/recompress.py uses: mean luminance
# difference at half display size, which must stay under 2.5 of 255. Measured
# across all seven covers, 80 -> 75 saves 15% at a worst case of 1.63. Below 75
# the curve flattens: 68 saves another 8% and is not worth the margin.
QUALITY = 75


def crop_cover(im, ratio):
    """The centred crop `object-fit: cover` would have made."""
    w, h = im.size
    if w / float(h) > ratio:          # too wide: trim the sides
        new_w = int(round(h * ratio))
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    new_h = int(round(w / ratio))     # too tall: trim top and bottom
    top = (h - new_h) // 2
    return im.crop((0, top, w, top + new_h))


def run(force=False, quiet=True):
    if not os.path.isdir(CASES_DIR):
        return 0
    made = 0
    for slug in sorted(os.listdir(CASES_DIR)):
        src = os.path.join(CASES_DIR, slug, "01-1200.webp")
        if not os.path.exists(src):
            continue
        for width in WIDTHS:
            dst = os.path.join(CASES_DIR, slug, "card-%d.webp" % width)
            if not force and os.path.exists(dst) \
                    and os.path.getmtime(dst) >= os.path.getmtime(src):
                continue
            im = crop_cover(Image.open(src).convert("RGB"), RATIO)
            if im.size[0] != width:
                im = im.resize((width, int(round(width / RATIO))), Image.LANCZOS)
            im.save(dst, "WEBP", quality=QUALITY, method=6)
            made += 1
            if not quiet:
                print("  wrote %s (%dx%d, %.0f KB)"
                      % (os.path.relpath(dst, ROOT), im.size[0], im.size[1],
                         os.path.getsize(dst) / 1024.0))
    return made


if __name__ == "__main__":
    n = run(force="--force" in sys.argv, quiet=False)
    print("  %d card cover(s) written" % n)

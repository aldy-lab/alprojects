#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Derive the /projects card covers from the opening plate of each case.

The card is a square window on to a photograph that is usually 3:4. Shipping
the whole plate and letting `object-fit: cover` throw away the top and bottom
means the browser downloads 1200x1600 to display 1200x1200 -- a quarter of
every file discarded before it is painted. Across seven cards on a 3x phone
the old 4:3 window wasted 44% of each file, 1539 KB on one page.

The window was 4:3 and is now 1:1, because the card is where these frames are
judged and a square is the bigger picture: 33% more area at the same column
width, and on the eight portrait plates it shows 75% of the frame's height
rather than 56%. It crops the two landscape plates instead, which is the
trade.

So the crop happens here instead, once, and the card points at the result:

    01-1200.webp  1200x1600   the plate, untouched, used by the case page
    card-1200.webp  1200x1200  the square window the card opens on it
    card-900.webp    900x900
    card-600.webp    600x600

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
RATIO = 1.0
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
            # Down only. A square window on a 1200x900 landscape plate is
            # 900x900, and asking for 1200 of it would print an upscale into
            # the file and then advertise it in srcset as if it were real
            # detail. Two of the ten plates are landscape; their largest card
            # is 900, and cases_html() offers whatever widths exist.
            if im.size[0] > width:
                im = im.resize((width, int(round(width / RATIO))), Image.LANCZOS)
            elif im.size[0] < width:
                # And if a width cannot be produced honestly, the file for it
                # must not survive from a previous ratio. Leaving it there is
                # how the two landscape cards kept a stale 1200x900 cover and
                # went on advertising it at 1200w under a square window.
                if os.path.exists(dst):
                    os.remove(dst)
                continue
            im.save(dst, "WEBP", quality=QUALITY, method=6)
            made += 1
            if not quiet:
                print("  wrote %s (%dx%d, %.0f KB)"
                      % (os.path.relpath(dst, ROOT), im.size[0], im.size[1],
                         os.path.getsize(dst) / 1024.0))
    return made


def news_variants(imgs, force=False, quiet=True):
    """A 900px copy of each news thumbnail, for the widths the card actually
    lands on.

    The news index used to show these in a three-up grid 371px wide and took
    the 600px file. Two-up they are 626px, so the browser reaches past 600 and
    takes the 1200 -- correct, and 40% heavier than it needs to be at 1x.
    A 900 in the middle covers a 626px plate at 1.44x, which is past what a
    2x screen resolves at that size.

    Only files wider than 900 get one; one of the six is a 900x1200 portrait
    whose -1200 name is about its height, and a "900" copy of it would be the
    same file under another name. The list comes from the caller because the
    article table lives in build-pages.py -- deriving one of these for every
    -1200.webp in assets/projects would write a dozen files nothing loads.
    """
    made = 0
    for rel in imgs:
        src = os.path.join(ROOT, "assets", rel)
        if not rel.endswith("-1200.webp") or not os.path.exists(src):
            continue
        dst = src[:-len("-1200.webp")] + "-900.webp"
        if not force and os.path.exists(dst) \
                and os.path.getmtime(dst) >= os.path.getmtime(src):
            continue
        im = Image.open(src).convert("RGB")
        if im.size[0] <= 900:
            continue
        im = im.resize((900, int(round(900 * im.size[1] / float(im.size[0])))),
                       Image.LANCZOS)
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-encode the photographs, but only where it is both free and worth it.

The WebP files were written at a quality that costs 0.15 to 0.29 bytes per
pixel. Photography for the web usually sits nearer 0.10. Re-encoding at 82
was measured across all 62 files above 60 KB and saved nothing at all -- a
third of them came out larger, which is what happens when you re-encode a
lossy file at the quality it already has. At 75 it saves 17%.

Two rails, because this is destructive and these are the only copies:

  * a file is only rewritten if the new one is at least MIN_GAIN smaller.
    Generation loss for no bytes is the worst possible trade.
  * the difference is measured at half size -- the scale these are actually
    displayed at, not 1:1, where artefacts nobody will ever see are visible
    -- and a file is skipped if the mean luminance difference exceeds
    MAX_DIFF. Measured worst case at quality 75 is 1.91 of 255, or 0.75%.

    python3 tools/recompress.py            # report only
    python3 tools/recompress.py --write

git restores the previous files; nothing here is unrecoverable, but nothing
here is reversible in place either.
"""

import glob
import os
import sys
import tempfile

from PIL import Image, ImageChops, ImageStat

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUALITY = 75
MIN_BYTES = 60 * 1024      # below this the saving is not worth a re-encode
MIN_GAIN = 0.05            # at least 5% smaller, or leave it alone
MAX_DIFF = 2.5             # mean luminance difference at display scale, of 255


def measure(original, candidate):
    half = (max(1, original.size[0] // 2), max(1, original.size[1] // 2))
    a = original.resize(half, Image.LANCZOS)
    b = candidate.resize(half, Image.LANCZOS)
    return ImageStat.Stat(ImageChops.difference(a, b).convert("L")).mean[0]


def main(write=False):
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "assets", "**", "*.webp"), recursive=True)
                   if os.path.getsize(f) >= MIN_BYTES)
    rewritten = skipped_gain = skipped_diff = 0
    before_total = after_total = 0
    for path in files:
        before = os.path.getsize(path)
        original = Image.open(path).convert("RGB")
        tmp = tempfile.mktemp(suffix=".webp")
        original.save(tmp, "WEBP", quality=QUALITY, method=6)
        after = os.path.getsize(tmp)
        gain = (before - after) / float(before)
        diff = measure(original, Image.open(tmp).convert("RGB"))
        rel = os.path.relpath(path, ROOT)
        if gain < MIN_GAIN:
            skipped_gain += 1
            os.unlink(tmp)
            continue
        if diff > MAX_DIFF:
            skipped_diff += 1
            print("  skipped (visible: %.2f) %s" % (diff, rel))
            os.unlink(tmp)
            continue
        rewritten += 1
        before_total += before
        after_total += after
        if write:
            os.replace(tmp, path)
        else:
            os.unlink(tmp)
    print("  %d files: %d rewritten, %d too little gain, %d too visible"
          % (len(files), rewritten, skipped_gain, skipped_diff))
    if rewritten:
        print("  %.0f -> %.0f KB, %.0f KB saved (%.0f%%)%s"
              % (before_total / 1024.0, after_total / 1024.0,
                 (before_total - after_total) / 1024.0,
                 100.0 * (before_total - after_total) / before_total,
                 "" if write else "   [report only -- pass --write]"))


if __name__ == "__main__":
    main(write="--write" in sys.argv)

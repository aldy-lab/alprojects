#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""An AVIF beside every WebP the pages show, when it is worth having.

Measured before this existed: on the eight heaviest photographs the site
serves, AVIF at the same visual quality was 54% lighter than the WebP --
1218 KB down to 565. The phone home page pulls ~800 KB, nearly all of it
photographs, so this is the largest single thing between a site that feels
instant on office wifi and one that feels instant on a site's 4G.

QUALITY IS MEASURED, NOT CHOSEN. The same rail tools/thumbs.py and
tools/recompress.py use: mean luminance difference at half display size. The
project's line is 2.5 of 255; this uses 2.2, because AVIF fails differently
from WebP -- it smooths texture away rather than blocking it -- and a weld bead
or a steel surface is exactly the texture it would take. The lowest quality
that stays under the line wins.

An AVIF is kept only if it is at least 10% smaller than its WebP. Below that
the extra <source> costs more in markup and decode than it saves. Those
decisions are remembered in tools/avif.json, keyed by a hash of the WebP, so
a build does not re-run the search for files it already judged.

The WebP stays the fallback for every browser without AVIF; nothing is
removed. Encoding is slow (a second or two per file), but it happens once:
afterwards ensure() is an mtime comparison. That is also what makes it safe
inside the GitHub Action -- a photograph the client uploads gets its AVIF on
the build that derives its WebP.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "tools", "avif.json")
RAIL = 2.2
QUALITIES = (40, 45, 50, 55, 60, 65, 70, 80)
MIN_SAVING = 0.10

_manifest = None
_dirty = [False]


def _load():
    global _manifest
    if _manifest is None:
        try:
            with io.open(MANIFEST, encoding="utf-8") as fh:
                _manifest = json.load(fh)
        except Exception:
            _manifest = {}
    return _manifest


def save():
    if _dirty[0]:
        with io.open(MANIFEST, "w", encoding="utf-8") as fh:
            json.dump(_load(), fh, indent=1, sort_keys=True)
            fh.write("\n")
        _dirty[0] = False


def available():
    try:
        from PIL import features
        return bool(features.check("avif"))
    except Exception:
        return False


def _diff(a, b):
    from PIL import Image, ImageChops, ImageStat
    w, h = a.size
    size = (max(1, w // 2), max(1, h // 2))
    a2 = a.convert("L").resize(size, Image.LANCZOS)
    b2 = b.convert("L").resize(size, Image.LANCZOS)
    return ImageStat.Stat(ImageChops.difference(a2, b2)).mean[0]


def _sha(path):
    import hashlib
    with open(path, "rb") as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def ensure(rel):
    """Return the AVIF's path relative to assets/ if one is worth serving.

    `rel` is a WebP path relative to assets/. None means "serve the WebP
    alone": no encoder, no source, or AVIF not meaningfully smaller.

    Freshness is decided by the WebP's CONTENT, never its mtime. The first
    version compared mtimes, and a git checkout -- which is how the GitHub
    Action gets the files -- stamps every file with the moment of checkout.
    On the runner each AVIF could look older than its WebP, and the build
    would either re-encode all 208 on every client save or, with no encoder
    there, stop wrapping and quietly take every AVIF off the site. A hash of
    the WebP survives a checkout; an mtime does not."""
    if not rel.endswith(".webp"):
        return None
    src = os.path.join(ROOT, "assets", rel)
    if not os.path.exists(src):
        return None
    out_rel = rel[:-5] + ".avif"
    out = os.path.join(ROOT, "assets", out_rel)
    sha = _sha(src)
    rec = _load().get(rel)

    if rec and rec.get("sha") == sha:
        if rec.get("skip"):
            return None
        if os.path.exists(out):
            return out_rel
    if not available():
        return None

    from PIL import Image
    im = Image.open(src).convert("RGB")
    size = os.path.getsize(src)
    chosen = None
    for q in QUALITIES:
        buf = io.BytesIO()
        im.save(buf, "AVIF", quality=q, speed=4)
        data = buf.getvalue()
        if _diff(im, Image.open(io.BytesIO(data))) < RAIL:
            chosen = (q, data)
            break
    if not chosen or len(chosen[1]) > size * (1 - MIN_SAVING):
        _load()[rel] = {"sha": sha, "skip": True}
        _dirty[0] = True
        if os.path.exists(out):
            os.remove(out)
        return None
    with open(out, "wb") as fh:
        fh.write(chosen[1])
    _load()[rel] = {"sha": sha, "quality": chosen[0],
                    "webp": size, "avif": len(chosen[1])}
    _dirty[0] = True
    return out_rel


if __name__ == "__main__":
    # Encode everything up front, so the first build after this lands is not
    # the one that spends ten minutes doing it.
    import glob
    files = sorted(os.path.relpath(p, os.path.join(ROOT, "assets"))
                   for p in glob.glob(os.path.join(ROOT, "assets", "**", "*.webp"),
                                      recursive=True))
    made = skipped = 0
    w = a = 0
    for i, rel in enumerate(files, 1):
        r = ensure(rel)
        if r:
            made += 1
            w += os.path.getsize(os.path.join(ROOT, "assets", rel))
            a += os.path.getsize(os.path.join(ROOT, "assets", r))
        else:
            skipped += 1
        if i % 20 == 0:
            save()
            print("  %d/%d" % (i, len(files)), flush=True)
    save()
    print("  avif: %d | webp only: %d | %d KB -> %d KB (%+d%%)"
          % (made, skipped, w // 1024, a // 1024,
             round(100 * (a - w) / w) if w else 0))
    sys.exit(0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill content/translations/<lang>.json from the tables in tools/lang_*.py.

Run once, and again whenever a client collection gains a field that I have
translated in the Python table rather than in the editor. It only ever adds
what the table can answer for the CURRENT English, so running it twice changes
nothing and running it after a client edit does not invent a translation.

Why the two live side by side at all: 15 of the 93 translatable values in
positions and articles also appear inside other units -- "Shipbuilding" is a
vacancy field and also sits inside "Shipbuilding sector - ALPROJECTS Group" --
so deleting them from the string table would silently untranslate those other
lines. See the note at client_store() in tools/i18n_build.py.
"""
import collections
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content
import i18n

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT:
            continue
        path = os.path.join(ROOT, "content", "translations", "%s.json" % lang)
        try:
            with io.open(path, encoding="utf-8") as fh:
                out = json.load(fh, object_pairs_hook=collections.OrderedDict)
        except Exception:
            out = collections.OrderedDict()
        added = 0
        for name in i18n.CLIENT_COLLECTIONS:
            flat = content.flatten(content.load(name))
            for cid in sorted(flat):
                english = flat[cid]
                if not english.strip():
                    continue
                key = "%s.%s" % (name, cid)
                fp = content.fingerprint(english)
                have = out.get(key)
                # Never overwrite a record that already matches: that one may
                # have come from the editor, and the table's version is the
                # older of the two.
                if have and have.get("en") == fp and have.get("t"):
                    continue
                t = i18n.t(lang, english)
                if t is None:
                    continue
                out[key] = collections.OrderedDict([("en", fp), ("t", t)])
                added += 1
        ordered = collections.OrderedDict((k, out[k]) for k in sorted(out))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        io.open(path, "w", encoding="utf-8").write(
            json.dumps(ordered, ensure_ascii=False, indent=2) + "\n")
        print("  %s  %d records (%d added this run)"
              % (os.path.relpath(path, ROOT), len(ordered), added))


if __name__ == "__main__":
    main()

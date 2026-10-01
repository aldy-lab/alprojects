#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off: give every translation record the English it was made from.

The stores used to keep a fingerprint of that English, which answered one
question -- has it changed -- and nothing else. The editor has to SHOW the
client the sentence a translation was made from, next to the one that replaced
it, so he can decide whether the translation still applies. A hash cannot be
shown. So the field becomes `src`, the English itself.

Two ways to recover it, both exact, neither a guess:
  the fingerprint matches the English in content/  -> that IS the source
  it does not                                     -> look the translation up
                                                     backwards in lang_*.py,
                                                     whose keys ARE the English
A record neither route can place keeps no `src` and stays stale, which is what
it is. Nothing is invented.

Safe to run again: a record that already has `src` is left alone.
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
    flat = {}
    for name in i18n.CLIENT_COLLECTIONS:
        for cid, text in content.flatten(content.load(name)).items():
            flat["%s.%s" % (name, cid)] = text

    for lang in i18n.LANGS:
        if lang == i18n.DEFAULT:
            continue
        path = os.path.join(ROOT, "content", "translations", "%s.json" % lang)
        if not os.path.exists(path):
            continue
        with io.open(path, encoding="utf-8") as fh:
            store = json.load(fh, object_pairs_hook=collections.OrderedDict)

        back = {}
        for en, tr in i18n.S.get(lang, {}).items():
            back.setdefault(tr, en)

        out = collections.OrderedDict()
        by_fp = by_table = unknown = 0
        for cid in sorted(store):
            r = store[cid]
            rec = collections.OrderedDict()
            src = r.get("src")
            if not src:
                english = flat.get(cid)
                if english is not None and r.get("en") == content.fingerprint(english):
                    src, by_fp = english, by_fp + 1
                elif r.get("t") and back.get(r["t"]):
                    src, by_table = back[r["t"]], by_table + 1
                else:
                    unknown += 1
            if src:
                rec["src"] = src
            rec["t"] = r.get("t", "")
            if r.get("by"):
                rec["by"] = r["by"]
            out[cid] = rec
        io.open(path, "w", encoding="utf-8").write(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n")
        print("  %s  %d records | from the fingerprint %d | from the table %d | unknown %d"
              % (lang, len(out), by_fp, by_table, unknown))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The site's copy, as data the client can edit.

WHY THIS EXISTS
Every word on the site used to live in tools/build-pages.py -- 3767 lines, most
of them text literals -- and in index.html. That is fine for a site only I
touch, and impossible for a client who wants to change a sentence. The text
moves out here, into JSON with a stable id per field, so an editor can put a
form in front of him and a diff can show exactly which sentence changed.

ONE SOURCE, NOT TWO
A file of "overrides" sitting beside the literals would have been half the work
and the wrong answer: two places holding the same sentence, and the one you
edit is the one that does nothing. So the literal LEAVES the Python when its
field moves here. build-pages.py keeps the structure -- slugs, ordering, image
sizes, dates, flags, markup -- and asks this module for the words.

IDS
An id is the record's own identity, never its position or its text:

    services.groups.inspection-access.label
    services.welding-services.lead
    services.welding-services.points.3

Position would move every time a section moves, so the groups are keyed by a
slug of their own rather than by "the first group". The text itself is what an
editor changes, so hashing it would rename the field on every edit -- and take
its three translations with it, which is exactly the failure this is meant to
make impossible.

Inside a list the index IS the id, because a bullet has no other identity. Move
a bullet and its translations are attached to the wrong line -- which the
fingerprint below catches on the next build and names, rather than shipping
quietly. That is the trade for not making the client invent an id per bullet.

A key starting with an underscore is structure, not copy: ordering, slugs,
flags. Nothing under one is offered to an editor or counted by the publish
gate.

TRANSLATIONS
en.json (this file's data) is the source. de/fr/it carry, per id, the text AND
the hash of the English it was made from, so an edited English string can be
told apart from a merely missing translation: the first is stale, the second
was never done. tools/i18n_build.py refuses to publish either.
"""

import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "content")


def path(name):
    return os.path.join(DIR, name + ".json")


def load(name):
    """The copy for one collection. Missing file is an error, not an empty
    dict: a silently empty collection would build a site with no words on it
    and nothing would say why."""
    with open(path(name), encoding="utf-8") as fh:
        return json.load(fh)


def save(name, data):
    os.makedirs(DIR, exist_ok=True)
    with open(path(name), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2, sort_keys=False)
        fh.write("\n")


def fingerprint(text):
    """What a translation records about the English it was made from. Ten hex
    characters is plenty to notice an edit and short enough to read in a diff."""
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]


def flatten(data, prefix=""):
    """Every leaf string in a collection, as id -> text.

    This is what the translator's file is keyed by and what the publish gate
    counts, so it has to see the same fields the templates read -- lists
    included, numbered from 1 because the ids end up in front of a human."""
    out = {}
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("_"):
                continue
            out.update(flatten(v, "%s.%s" % (prefix, k) if prefix else k))
    elif isinstance(data, list):
        for i, v in enumerate(data, 1):
            out.update(flatten(v, "%s.%d" % (prefix, i)))
    elif isinstance(data, str):
        if data.strip():
            out[prefix] = data
    return out


# ---------------- services ----------------
def services_groups(doc, deep=None):
    """SERVICE_GROUPS in the shape build-pages.py has always used, built from
    the copy plus the two things that are not copy: the raw HTML of a deep
    block, and the ordering, which lives in the file under _-keys."""
    deep = deep or {}
    groups = []
    for gid in doc["_group_order"]:
        g = doc["groups"][gid]
        svs = []
        for slug in g["_services"]:
            c = doc["services"][slug]
            sv = dict(slug=slug, nav=c["nav"], h1=c["h1"], lead=c["lead"],
                      points=list(c["points"]))
            if c.get("seo"):
                sv["seo"] = c["seo"]
            if slug in deep:
                sv["deep"] = deep[slug]
            svs.append(sv)
        groups.append((g["label"], svs))
    return groups

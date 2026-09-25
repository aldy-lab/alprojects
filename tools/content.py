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


# ---------------- the generic shape ----------------
# A collection file is one JSON document:
#
#   {"_order": ["slug", ...], "<slug>": {copy fields..., "_structural": ...}}
#
# Copy and structure live in the SAME file on purpose. The alternative was a
# JSON of words beside a Python table of everything else, and then every added
# record has to be added in two places -- which is the drift this whole move is
# supposed to end. The underscore is the whole convention: an editor and the
# publish gate see the keys without one, build-pages.py reads both.
def records(doc):
    """The records in their published order, as (slug, dict) pairs."""
    return [(slug, doc[slug]) for slug in doc["_order"]]


def sector_pages(doc):
    """SECTOR_PAGES as build-pages.py has always taken it: a tuple per sector
    of (slug, name, image stem, lead, service slugs)."""
    return [(slug, r["name"], r["_img"], r["lead"], list(r["_services"]))
            for slug, r in records(doc)]


def positions(doc):
    """POSITIONS, with the underscore taken off the structural keys.

    `discipline` is one of them, and that is deliberate: it has to match an
    option in DISCIPLINES exactly or the Apply button selects nothing in the
    form, so it is a value with a constraint rather than a sentence -- an
    editor gets it as a list to pick from, never as a text box."""
    out = []
    for slug, r in records(doc):
        p = {k: v for k, v in r.items() if not k.startswith("_")}
        p.update({k[1:]: v for k, v in r.items() if k.startswith("_")})
        p["id"] = slug
        out.append(p)
    return out


def articles(doc):
    """ARTICLES. `facts` is a list of triples in the template and a list of
    named objects in the file, because a three-item array in an editor is three
    unlabelled boxes."""
    out = []
    for slug, r in records(doc):
        a = {k: v for k, v in r.items() if not k.startswith("_")}
        a.update({k[1:]: v for k, v in r.items() if k.startswith("_")})
        a["slug"] = slug
        # Three fields, not two: label, value and the note printed under it.
        # The first pass here dropped the note, which the round-trip caught --
        # the page would have rendered two thirds of every fact.
        a["facts"] = [(f["label"], f["value"], f["note"])
                      for f in r.get("facts", [])]
        out.append(a)
    return out


def cases(doc):
    """CASES. Two nested shapes are flattened out for the editor and put back
    here:

      stages  (photo number, [paragraphs])  ->  {"_photo": n, "text": [...]}
      photos  (alt, caption, w, h)          ->  {"alt", "caption", "_w", "_h"}

    A stage's photo number and a frame's pixel size are structure; the alt text
    and the caption are copy, and they are two different sentences that used to
    sit next to each other in one anonymous tuple. Optional keys are rebuilt
    only if the file has them: the templates ask with .get(), so inventing an
    empty one would change what they render."""
    out = []
    for slug, r in records(doc):
        c = {"slug": slug}
        for k, v in r.items():
            if k.startswith("_") or k in ("stages", "photos"):
                continue
            c[k] = list(v) if isinstance(v, list) else v
        for k, v in r.items():
            if k.startswith("_"):
                c[k[1:]] = list(v) if isinstance(v, list) else v
        if "stages" in r:
            c["stages"] = [(s["_photo"], list(s["text"])) for s in r["stages"]]
        if "photos" in r:
            c["photos"] = [(p["alt"], p["caption"], p["_w"], p["_h"])
                           for p in r["photos"]]
        out.append(c)
    return out


# ---------------- site-wide odds ----------------
def site(doc):
    """The copy that belongs to no collection: the services cover, the page
    titles and meta descriptions, the form's option lists, the number words,
    the photo captions on /projects, and the organisation's own name.

    Returned in the shapes build-pages.py already used, so the call sites did
    not have to change shape when the literals left them."""
    # Rebuilt in the file's own key order, not in a convenient one. The first
    # version put @type and name first and the rest after, which is the same
    # Organization to every reader but a different byte sequence in the
    # JSON-LD -- and that turned up as 30 changed pages against the assertion
    # that this refactor changes nothing. The order is data now, so it stays.
    org = {}
    for k, v in doc["org"].items():
        org["@type" if k == "_type" else (k[1:] if k.startswith("_") else k)] = v
    return {
        "cover_h1": doc["services_cover"]["h1"],
        "cover_lead": doc["services_cover"]["lead"],
        "pages": doc["pages"],
        "disciplines": list(doc["form_options"]["disciplines"]),
        "certificates": list(doc["form_options"]["certificates"]),
        "rotations": list(doc["form_options"]["rotations"]),
        "countries": list(doc["form_options"]["countries"]),
        "experience": list(doc["form_options"]["experience"]),
        # 1-based in the template, a list in the file: a JSON object cannot
        # have integer keys, and "1".."12" as strings invites an off-by-one at
        # the one place that reads it.
        "count_word": {i: w for i, w in enumerate(doc["count_words"], 1)},
        "shots": [(s["_stem"], s["caption"], s["_w"], s["_h"])
                  for s in doc["shots"]],
        "org": org,
    }

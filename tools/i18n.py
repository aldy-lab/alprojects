# -*- coding: utf-8 -*-
"""
Every user-facing string on the site, in the four languages it sells in.

Only strings live here. The markup stays in build-pages.py and index.html, so
a layout change is made once rather than four times.

HOW A UNIT IS KEYED
    The key is the English source exactly as it appears in the built HTML,
    whitespace-collapsed -- including any inline tags inside it. Run
    `python3 tools/i18n_extract.py --dump` to get the current list; it reads
    the built site, so it can never drift from what actually shipped.

    Inline tags are part of the unit on purpose. "Offices in
    <strong>Lithuania</strong>, <strong>Poland</strong>, <strong>Germany</strong>
    and <strong>Norway</strong> sit close to our clients' yards" puts those
    words in a different order in German, and a translator working on text-node
    fragments cannot move them. Keep the same tags in the translation; the
    build checks that you did.

    Links keep their English paths in the translation (/company.html). The
    build prefixes them per language, so a translation never carries /de/.

PUBLISHING
    A language ships only at 100% coverage -- see PUBLISH below. A page that is
    half English is worse than no page in that language at all, and this is
    a company selling on precision.

⚠️ TRANSLATION REVIEW
    The technical vocabulary here is the part worth checking: welding process
    names, NDT method names, certification scopes and the inspection-
    independence wording are terms of art in each market, and getting one wrong
    is a credibility problem with exactly the clients this site is for. Have a
    native speaker in each market read the services, sectors and certification
    copy before go-live. The privacy policy is a legal text and should be
    reviewed by whoever signs it off.
"""

LANGS = ("en", "fr", "de", "it")
DEFAULT = "en"

# <html lang>, og:locale
LOCALE = {
    "en": ("en", "en_GB"),
    "fr": ("fr", "fr_FR"),
    "de": ("de", "de_DE"),
    "it": ("it", "it_IT"),
}
# the switcher label, and the accessible name of the link
LABEL = {"en": "EN", "fr": "FR", "de": "DE", "it": "IT"}
LANG_NAME = {"en": "English", "fr": "Français", "de": "Deutsch", "it": "Italiano"}

# "Language" for the switcher's group label, per language
LANG_GROUP = {"en": "Language", "fr": "Langue", "de": "Sprache", "it": "Lingua"}

# Flip to True once coverage reports 100% for that language. Anything False is
# not written, not linked, and not in the sitemap -- so a partial translation
# cannot reach a visitor.
PUBLISH = {"en": True, "fr": True, "de": False, "it": False}

# Paths that exist once and are shared by every language: never prefixed.
# 404.html is here because GitHub Pages serves the host's single /404.html for
# any unmatched path -- a /de/404.html would be a file nothing ever requests.
SHARED_PREFIXES = ("/assets/", "/css/", "/js/", "/sitemap.xml", "/robots.txt",
                   "/404.html", "/favicon", "/apple-touch-icon")

# ============================================================
# STRINGS
# Key = the English unit. Value = the translation.
# Populate with tools/i18n_extract.py --dump as the checklist.
# ============================================================

# One module per language, so a 500-entry dict does not sit in the middle of
# the configuration and each language can be reviewed on its own.
try:
    from lang_fr import S as _FR
except ImportError:
    _FR = {}
try:
    from lang_de import S as _DE
except ImportError:
    _DE = {}
try:
    from lang_it import S as _IT
except ImportError:
    _IT = {}

S = {"fr": _FR, "de": _DE, "it": _IT}


def t(lang, unit):
    """Translation for a unit, or None if it has not been written yet."""
    if lang == DEFAULT:
        return unit
    return S.get(lang, {}).get(unit)

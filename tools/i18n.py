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

import html as _html
import re
LANGS = ("en", "fr", "de", "it", "ru")
DEFAULT = "en"

# <html lang>, og:locale
LOCALE = {
    "en": ("en", "en_GB"),
    "fr": ("fr", "fr_FR"),
    "de": ("de", "de_DE"),
    "it": ("it", "it_IT"),
    "ru": ("ru", "ru_RU"),
}
# the switcher label, and the accessible name of the link
LABEL = {"en": "EN", "fr": "FR", "de": "DE", "it": "IT", "ru": "RU"}
LANG_NAME = {"en": "English", "fr": "Français", "de": "Deutsch",
             "it": "Italiano", "ru": "Русский"}

# "Language" for the switcher's group label, per language
LANG_GROUP = {"en": "Language", "fr": "Langue", "de": "Sprache",
              "it": "Lingua", "ru": "Язык"}

# Flip to True once coverage reports 100% for that language. Anything False is
# not written, not linked, and not in the sitemap -- so a partial translation
# cannot reach a visitor.
#
# ru is True so the page can be read on a preview -- nobody can sign off wording
# they cannot see. Two strings in tools/lang_ru.py are drafts, not authorised
# text: the application form's consent and the newsletter's. They name a 24
# month retention period, a controller and a deletion route, and the site relies
# on them to claim the box was ticked against a specific wording. Confirm those
# two before the Russian URL goes into a job advert.
PUBLISH = {"en": True, "fr": True, "de": True, "it": True, "ru": True}

# ============================================================
# WHAT THE CLIENT EDITS, AND WHY IT IS NOT GATED LIKE THE REST
# ============================================================
# The CMS gives the client these collections: vacancies and news. He was
# promised he can post a vacancy today without waiting for a translator, and
# that the English does not have to stay in step with the other languages.
#
# Everything else -- page prose, headings, the forms, the footer -- is mine, and
# there the 100% gate stays. An English sentence in the middle of a German page
# is a defect when I wrote the German, and a fact of life when the client just
# posted a vacancy at 18:00 on a Friday.
#
# So a unit whose English text comes from one of these collections falls back to
# English on its own and does not withhold the language. Without this, one word
# edited in the CMS drops all four languages below 100%, none of them are
# rewritten, the previous files stay on disk, and the site ships English saying
# one thing and four languages saying another -- with exit code 0. That was
# measured, not assumed, before this was written.
CLIENT_COLLECTIONS = ("positions", "articles")

# A language may cover only part of the site.
#
# Russian exists for the careers page and nothing else. The crews this company
# recruits are reached through Russian-language channels, and a job advert links
# straight to the page -- so the one page that has to be readable by a welder in
# his own language is the one that is, and the other forty stay in the four
# languages the clients read.
#
# Absent from this table means "every page", which is how the other three work.
#
# Three things follow from it and are implemented rather than assumed:
#   * the switcher offers RU only on the pages Russian covers, so it can never
#     be a link to a page that does not exist;
#   * hreflang likewise -- /ru/careers and /careers declare each other, and no
#     other page claims a Russian alternate;
#   * internal links inside a Russian page are NOT prefixed when the target has
#     no Russian version, so the header and footer lead to the English pages
#     instead of to forty 404s.
PAGES = {"ru": ("careers.html",)}


def covers(lang, rel):
    """Does this language have this page?"""
    pages = PAGES.get(lang)
    return pages is None or rel in pages

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
try:
    from lang_ru import S as _RU
except ImportError:
    _RU = {}

S = {"fr": _FR, "de": _DE, "it": _IT, "ru": _RU}


def t(lang, unit):
    """Translation for a unit, or None if it has not been written yet."""
    if lang == DEFAULT:
        return unit
    return S.get(lang, {}).get(unit)


def t_clamped(lang, unit):
    """Translation for a unit that is a truncated form of a longer one.

    A meta description is cut to length after the page is otherwise final, so
    the unit that reaches the translation table ends in an ellipsis and does
    not match the full sentence a translator was given. Rather than ask for the
    same paragraph twice -- once whole, once cut -- the full translation is
    looked up by its English prefix and cut with the same rule. The words are
    still the translator's; only the tail is dropped.

    Returns None if no full translation covers this prefix, so the coverage
    gate still fails on a description nobody has translated.
    """
    if not unit.endswith("\u2026"):
        return None
    stem = unit[:-1]
    for src, dst in S.get(lang, {}).items():
        if src.startswith(stem):
            return clamp_desc(dst)
    return None


# ============================================================
# META DESCRIPTION LENGTH
# ============================================================
# Every caller used to carry its own cut: 197 characters for a case lead, 152
# for a service page, nothing at all for the pages whose description is written
# by hand. Google shows about 160, so the long ones were being truncated by
# Google instead -- and the translations were worse than the English, because a
# French or German sentence runs 15-25% longer than the English it was cut from,
# and the cut happened before the translation. One page reached 236.
#
# So the rule lives here and both builds apply it after their own text is
# final: build-pages.py inside page(), i18n_build.py after substitution.
#
# The cut is made on the decoded text, not on the source, because the source
# contains entities -- &rsquo; is one character on screen and seven in the file,
# so a cut counted in source characters both measures wrong and can land inside
# an entity, which would put a bare "&rsq" in the head. Short descriptions are
# returned untouched, entities and all.

DESC_MAX = 160

_DESC_RE = re.compile(r'(<meta (?:name="description"|property="og:description") '
                      r'content=")(.*?)(">)', re.S)


def clamp_desc(text, limit=DESC_MAX):
    """Cut one description to `limit` displayed characters, on a word boundary."""
    plain = _html.unescape(text)
    if len(plain) <= limit:
        return text
    cut = plain[:limit - 1].rsplit(" ", 1)[0].rstrip(" ,.;:—–-")
    return (cut.replace("&", "&amp;").replace("<", "&lt;")
               .replace(">", "&gt;").replace('"', "&quot;") + "…")


def clamp_page_desc(html, limit=DESC_MAX):
    """Apply clamp_desc to the description meta tags in one page of HTML.

    og:description is clamped with the same rule so the two never disagree --
    a share card showing more than the search result reads as an oversight.
    """
    return _DESC_RE.sub(lambda m: m.group(1) + clamp_desc(m.group(2), limit) + m.group(3),
                        html)

# -*- coding: utf-8 -*-
"""
Path rewriting shared by the page generator and the translation build.

This lived inside build-pages.py until the language trees needed it too.
index.html is hand-authored with relative asset paths (assets/logo.svg), which
resolve correctly at the site root and nowhere else -- under /fr/ they become
/fr/assets/logo.svg, which is a 404 on every image, stylesheet and font. Both
builds have to apply the same fix, so it lives in one place.
"""
import re

# ------------------------------------------------------------------ the origin
# The site's own scheme and host, in one place.
#
# It was written out 46 times across build-pages.py, index.html, robots.txt and
# api/form.js -- canonicals, hreflang, og:url, eleven JSON-LD blocks, 160
# sitemap entries. Changing the domain meant 46 edits, and a canonical or an
# hreflang left pointing at the old host is exactly the kind of miss that
# ships: the page renders, Google reads a self-reference to a domain that
# redirects, and nothing anywhere says so.
#
# One line now. Everything that composes a URL asks for it, and origin_fix()
# below rewrites the literals in the hand-authored pages at write time, so
# index.html can keep reading like a normal HTML file.
#
# When the site moves to alprojects.eu: change this, rebuild, and check
# THE MAIL, not the pages. That domain's SPF is "v=spf1 a mx ip4:79.98.28.183
# ~all" -- the `a` mechanism authorises whatever the A record points at, so
# moving the web A record to a host silently hands that host permission to send
# mail as the domain, and removes it from the mail server. The ip4: term keeps
# the real one working, so nothing breaks loudly. Drop the `a` when the A
# record moves.
ORIGIN = "https://alprojects.eu"


# Every host this site has been served from. origin_fix() normalises any of
# them to ORIGIN, which is what makes the rewrite reversible: the first version
# returned early when ORIGIN was the default and only ever rewrote in one
# direction, so a domain drill rewrote index.html's eleven literals to the new
# host and changing the constant back left them there. A one-way rewrite of a
# hand-authored file is a trap, not a convenience.
#
# Scheme-qualified on purpose. The privacy policy names the website in a
# sentence -- "data collected through alprojects.co" -- and the footer carries
# info@alprojects.eu; neither has a scheme, so neither is touched here. That
# sentence is copy in four languages, and build-pages.py prints a note when it
# still names a host the site has left.
KNOWN_ORIGINS = (
    "https://alprojects.co",
    "https://www.alprojects.co",
    "https://alprojects.eu",
    "https://www.alprojects.eu",
)


def origin_fix(html, origin=None):
    """Any literal origin in hand-authored markup becomes the configured one.
    Idempotent, reversible, and it never touches a relative path."""
    origin = origin or ORIGIN
    for known in KNOWN_ORIGINS:
        if known != origin:
            html = html.replace(known, origin)
    return html


def rootify_assets(html):
    """Relative asset paths -> root-relative, so they survive any directory.

    Three syntaxes carry them, and only the first was handled until the
    language trees exposed the other two on the homepage:
        src="assets/x.webp"                      -- attributes
        srcset="assets/a.webp 600w, ..."         -- one path per candidate
        style="background-image:url('assets/x')" -- inline CSS
    A miss here is silent: the page renders, the image just is not there.
    """
    html = re.sub(r'(src|href)="(assets|css|js)/', r'\1="/\2/', html)
    html = re.sub(r'url\((\s*[\'"]?)(assets|css|js)/', r'url(\1/\2/', html)

    def _srcset(m):
        parts = []
        for cand in m.group(2).split(","):
            cand = cand.strip()
            parts.append(re.sub(r'^(assets|css|js)/', r'/\1/', cand))
        return '%s="%s"' % (m.group(1), ", ".join(parts))

    return re.sub(r'\b(srcset|imagesrcset)="([^"]*)"', _srcset, html)


def rootify_anchors(html):
    """Same-page anchors -> homepage anchors, for pages that are not the
    homepage.

    NB: skip #main (the skip-link) and #i-* (SVG sprite <use> refs). Rewriting
    the sprite refs to /#i-* silently breaks every icon on the page.
    """
    html = html.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#(?!main\b)(?!i-)([a-z-]+)"', r'href="/#\1"', html)


def rootify(html):
    """Both: what a generated sub-page needs."""
    return rootify_anchors(rootify_assets(html))

def clean_urls(html):
    """Drop the .html from internal links, canonicals and structured data.

    GitHub Pages already serves /company for /company.html -- verified against
    the live host, including under /fr/ -- so this is a link-and-canonical
    change, not a restructuring. Both spellings resolve, which is exactly why
    the canonical has to move with the links: otherwise every page is reachable
    at two URLs and points at the one nobody links to.

    404.html keeps its extension. GitHub Pages looks for that exact filename to
    serve a custom 404, and /404 is not a thing a browser ever requests.
    """
    def _href(m):
        attr, path, tail = m.group(1), m.group(2), m.group(3) or ""
        if path.endswith("/404"):
            return m.group(0)
        return '%s="%s%s"' % (attr, path, tail)

    # href="/company.html", href="/contacts.html#enquiry"
    html = re.sub(r'\b(href)="(/[^"#?]*?)\.html([#?][^"]*)?"', _href, html)
    # canonical, hreflang and JSON-LD carry the origin
    html = re.sub(r'(https://alprojects\.co/[^"\'\s<]*?)\.html(?![a-zA-Z])',
                  lambda m: m.group(0) if m.group(1).endswith("/404") else m.group(1),
                  html)
    return html

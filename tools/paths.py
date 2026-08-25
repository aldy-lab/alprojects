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

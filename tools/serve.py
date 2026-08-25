# -*- coding: utf-8 -*-
"""Local preview that behaves like GitHub Pages.

The site links to /company, not /company.html. GitHub Pages resolves that
itself -- verified against the live host, nested paths and language trees
included -- but `python -m http.server` does not: it returns 404 for every
link on the site, which looks like the build is broken when it is not.

    python3 tools/serve.py [port]        # default 8899

Two rules, matching what the host does:
  /company              -> company.html
  /news/                -> news/index.html   (already standard)
and anything missing falls back to 404.html with a real 404 status.
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        full = super().translate_path(path)
        if os.path.isfile(full):
            return full
        # <path>.html beats a directory of the same name. Both exist for
        # /services -- services.html and the services/ folder of the twelve
        # pages -- and the host serves the file: /services is the Services page
        # and /services/ is a 404 there. Checking isdir first gave a directory
        # listing instead, which is not a page this site has.
        if not os.path.splitext(full)[1] and os.path.isfile(full + ".html"):
            return full + ".html"
        return full

    def list_directory(self, path):
        """The host never serves a listing; a directory without index.html is
        a 404 there, so it is one here."""
        self.send_error(404)
        return None

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            page = os.path.join(ROOT, "404.html")
            if os.path.isfile(page):
                body = open(page, "rb").read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8899
    print("serving %s on http://localhost:%d  (clean URLs, like GitHub Pages)"
          % (ROOT, port))
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()

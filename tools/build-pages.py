#!/usr/bin/env python3
"""
Generates the sub-pages (privacy, careers, news articles) from the chrome in
index.html, so the header, footer and icon sprite never drift out of sync.

Not required to serve the site — the output is committed. Re-run it only after
editing the header or footer in index.html:

    python3 tools/build-pages.py
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
lines = src.split("\n")


def block(start_pat, end_pat, after=0):
    s = next(i for i, l in enumerate(lines) if re.search(start_pat, l))
    e = next(i for i, l in enumerate(lines[s + after:], s + after) if re.search(end_pat, l))
    return "\n".join(lines[s:e + 1])


HEADER = block(r'<a class="skip-link"', r'^\s*</nav>\s*$', after=40)
FOOTER = block(r'<footer class="site-footer"', r'^\s*</footer>\s*$')
SPRITE = block(r'<svg width="0" height="0"', r'^\s*</svg>\s*$')


def rootify(html):
    """Relative paths -> root-relative, and same-page anchors -> homepage anchors."""
    html = re.sub(r'(src|href)="(assets|css|js)/', r'\1="/\2/', html)
    html = html.replace('href="#top"', 'href="/"')
    html = re.sub(r'href="#(?!main\b)([a-z-]+)"', r'href="/#\1"', html)
    return html


HEADER_R, FOOTER_R, SPRITE_R = rootify(HEADER), rootify(FOOTER), rootify(SPRITE)


def page(title, description, body, noindex=False, canonical=None):
    robots = ('  <meta name="robots" content="noindex, follow">\n' if noindex
              else '  <meta name="robots" content="index, follow">\n')
    canon = ('  <link rel="canonical" href="https://alprojects.co%s">\n' % canonical
             if canonical else "")
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — ALPROJECTS Group</title>
  <meta name="description" content="{description}">
{canon}{robots}  <meta name="theme-color" content="#05060f">
  <meta property="og:site_name" content="ALPROJECTS Group">
  <meta property="og:title" content="{title} — ALPROJECTS Group">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <link rel="icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/montserrat-latin.woff2" crossorigin>
  <link rel="stylesheet" href="/css/fonts.css">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>

{header}

  <main id="main" class="page">
{body}
  </main>

{footer}

{sprite}

  <script src="/js/main.js"></script>
</body>
</html>
""".format(title=title, description=description, canon=canon, robots=robots,
           header=HEADER_R, footer=FOOTER_R, sprite=SPRITE_R, body=body)


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, "w", encoding="utf-8").write(html)
    print("wrote %s (%d bytes)" % (path, len(html)))


# ============================================================
# PRIVACY POLICY
# ============================================================
PRIVACY = """
    <div class="container page-head">
      <p class="eyebrow">Legal</p>
      <h1 class="page-title">Privacy Policy</h1>
      <p class="page-lead">How ALPROJECTS Group handles personal data collected through this website.</p>
      <p class="page-meta">Last updated: 15 August 2026</p>
    </div>

    <div class="container prose">
      <!-- NOTE(ALPROJECTS): this policy describes what the site technically does
           today. It has NOT been reviewed by a lawyer. Have it checked against your
           actual internal processes before relying on it. -->

      <h2>1. Who we are</h2>
      <p>ALPROJECTS, UAB (&ldquo;ALPROJECTS Group&rdquo;, &ldquo;we&rdquo;) is the controller of personal
      data collected through alprojects.co.</p>
      <ul>
        <li>ALPROJECTS, UAB — Silutes av. 2-536, LT-91110 Klaipeda, Lithuania</li>
        <li>Email: <a href="mailto:info@alprojects.eu">info@alprojects.eu</a></li>
        <li>Phone: <a href="tel:+37063663744">+370 636 63 744</a></li>
      </ul>

      <h2>2. What we collect</h2>
      <p>This website has no user accounts, no analytics and sets no cookies of its own.
      Data reaches us in three ways:</p>
      <ul>
        <li><strong>Newsletter.</strong> If you submit the newsletter form, we receive the
        email address you enter, in order to send you company and project updates.</li>
        <li><strong>Direct contact.</strong> If you email or call us, we receive whatever
        you choose to send — typically your name, contact details and the content of
        your enquiry.</li>
        <li><strong>Server logs.</strong> The site is hosted on GitHub Pages. GitHub
        records technical request data, including IP address and browser user-agent,
        for security and reliability.</li>
      </ul>

      <h2>3. Third parties that receive data</h2>
      <ul>
        <li><strong>GitHub, Inc.</strong> — website hosting and request logs.</li>
      </ul>
      <p>This site loads no third-party scripts, fonts, analytics or embeds. The
      typeface is served from our own domain, so browsing this site does not disclose
      your IP address to any advertising or analytics company.</p>

      <h2>4. Legal basis</h2>
      <ul>
        <li><strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription. You
        may withdraw it at any time.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)) — responding to enquiries,
        and keeping the site secure and available.</li>
      </ul>

      <h2>5. How long we keep it</h2>
      <p>Newsletter addresses are kept until you unsubscribe or ask us to remove them.
      Business correspondence is kept as long as needed for the enquiry or project and
      any statutory retention period that applies to it. Hosting logs are retained
      according to GitHub&rsquo;s own schedule.</p>

      <h2>6. Your rights</h2>
      <p>Under the GDPR you may request access to your data, correction, erasure,
      restriction of processing, portability, and you may object to processing based on
      legitimate interest. Write to
      <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> and we will respond
      within one month.</p>
      <p>If you believe we have handled your data improperly, you may lodge a complaint
      with the Lithuanian State Data Protection Inspectorate
      (Valstybine duomenu apsaugos inspekcija), L. Sapiegos g. 17, Vilnius.</p>

      <h2>7. Changes</h2>
      <p>If this policy changes, the revised version will be published on this page with
      a new date at the top.</p>

      <p class="back"><a class="btn-bracket" href="/">Back to homepage</a></p>
    </div>
"""

# ============================================================
# CAREERS
# ============================================================
CAREERS = """
    <div class="container page-head">
      <p class="eyebrow">Careers</p>
      <h1 class="page-title">Work with ALPROJECTS</h1>
      <p class="page-lead">We deliver mechanical contracting, welding, inspection and access
      services on industrial and offshore projects across Europe. The work is technical,
      certified and often on site.</p>
    </div>

    <div class="container prose">
      <h2>Disciplines we work in</h2>
      <p>Our project teams are built from these areas. We are always interested in
      qualified specialists in any of them:</p>
      <ul>
        <li>Welding services</li>
        <li>Pipe fitting</li>
        <li>Mechanical contracting</li>
        <li>Non-destructive testing (NDT)</li>
        <li>Rope access services</li>
        <li>Quality control and QAQC</li>
        <li>Rigging and technical support</li>
        <li>Project coordination and site supervision</li>
      </ul>

      <h2>What matters to us</h2>
      <ul>
        <li>Valid certification for your discipline, and the documentation to support it.</li>
        <li>Willingness to travel — our projects run in several countries.</li>
        <li>A serious approach to safety in complex and confined environments.</li>
        <li>Working English; Lithuanian, Russian or Polish are useful additions.</li>
      </ul>

      <h2>Open application</h2>
      <p>We do not always advertise individual vacancies. Send your CV and certificates
      and we will keep them on file and contact you when a project matches your profile.</p>
      <p>Email <a href="mailto:info@alprojects.eu?subject=Open%20application%20%E2%80%94%20careers">info@alprojects.eu</a>
      with your CV, your certifications and the disciplines you work in.</p>

      <!-- NOTE(ALPROJECTS): this page invites open applications and deliberately
           lists no specific vacancies, salaries or benefits. Add real openings here
           when there are some. -->

      <p class="back">
        <a class="btn-bracket" href="mailto:info@alprojects.eu?subject=Open%20application%20%E2%80%94%20careers">Send your CV</a>
        <a class="btn-bracket" href="/#team">Meet the team</a>
      </p>
    </div>
"""

# ============================================================
# NEWS ARTICLES  (structure only — real copy still to come)
# ============================================================
ARTICLES = [
    dict(slug="mechanical-installation-europe",
         num="01", date="26 Feb 2025", iso="2025-02-26", cat="Shipbuilding",
         img="news-1.webp", w=831, h=554,
         alt="Welder performing mechanical installation works",
         title="AL Projects delivers mechanical installation services for large-scale industrial facilities in Europe"),
    dict(slug="offshore-welding-pipe-fitting",
         num="02", date="05 Mar 2025", iso="2025-03-05", cat="Offshore",
         img="news-2.webp", w=1000, h=750,
         alt="Port cranes at sunset",
         title="Certified welding and pipe fitting specialists support complex offshore operations across Europe"),
    dict(slug="industrial-facilities-installation",
         num="03", date="26 Feb 2025", iso="2025-02-26", cat="Shipbuilding",
         img="news-3.webp", w=1000, h=562,
         alt="Precision welding on a workshop bench",
         title="AL Projects delivers mechanical installation services for large-scale industrial facilities in Europe"),
]

ARTICLE_BODY = """
    <div class="container page-head">
      <p class="eyebrow">{num} &middot; {cat}</p>
      <h1 class="page-title article-title">{title}</h1>
      <p class="page-meta"><time datetime="{iso}">{date}</time></p>
    </div>

    <div class="container">
      <img class="article-hero" src="/assets/{img}" alt="{alt}" width="{w}" height="{h}">
    </div>

    <div class="container prose">
      <div class="notice">
        <p><strong>Draft — not published.</strong> This page carries the headline, date and
        image already shown on the homepage. The article text has not been written yet, so
        the page is marked <code>noindex</code> and is not linked from the news cards.</p>
      </div>

      <!-- TODO(ALPROJECTS): replace this block with the real article copy. -->

      <p class="back"><a class="btn-bracket" href="/#news">Back to news</a></p>
    </div>
"""

write("privacy.html", page("Privacy Policy",
      "How ALPROJECTS Group handles personal data collected through this website.",
      PRIVACY, canonical="/privacy.html"))

write("careers.html", page("Careers",
      "Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.",
      CAREERS, canonical="/careers.html"))

for a in ARTICLES:
    write("news/%s.html" % a["slug"],
          page(a["title"][:60], a["title"], ARTICLE_BODY.format(**a), noindex=True))

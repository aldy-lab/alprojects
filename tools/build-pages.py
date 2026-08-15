#!/usr/bin/env python3
"""
Generates the sub-pages (privacy, careers, news articles) from the chrome in
index.html, so the header, footer and icon sprite never drift out of sync.

Not required to serve the site — the output is committed. Re-run it only after
editing the header or footer in index.html:

    python3 tools/build-pages.py
"""
import datetime, hashlib, io, os, re

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
    # NB: skip #main (skip-link) and #i-* (SVG sprite <use> refs) — rewriting
    # the sprite refs to /#i-* silently breaks every icon on the page.
    html = re.sub(r'href="#(?!main\b)(?!i-)([a-z-]+)"', r'href="/#\1"', html)
    return html


HEADER_R, FOOTER_R, SPRITE_R = rootify(HEADER), rootify(FOOTER), rootify(SPRITE)


def page(title, description, body, noindex=False, canonical=None, head_extra="", og="home"):
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
  <meta property="og:image" content="https://alprojects.co/assets/og/{og}.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://alprojects.co/assets/og/{og}.jpg">
  <link rel="icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/montserrat-latin.woff2" crossorigin>
  <link rel="stylesheet" href="/css/fonts.css">
  <link rel="stylesheet" href="/css/style.css">
{head_extra}</head>
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
           header=HEADER_R, footer=FOOTER_R, sprite=SPRITE_R, body=body,
           head_extra=head_extra, og=og)


# Stamped into <lastmod> in the sitemap on every build.
LASTMOD = datetime.date.today().isoformat()


# ---------------- cache busting ----------------
# GitHub Pages serves CSS with max-age=600 and no fingerprint, so a browser --
# iOS Safari especially -- can keep showing an old stylesheet long after a
# deploy, which reads as "the fix didn't work". Stamping the content hash into
# the URL makes every deploy a new URL, so a stale file can never win.
VERSIONED = ("css/style.css", "css/fonts.css", "js/main.js")
_hashes = {}


def asset_version(rel):
    if rel not in _hashes:
        blob = io.open(os.path.join(ROOT, rel), "rb").read()
        _hashes[rel] = hashlib.sha256(blob).hexdigest()[:8]
    return _hashes[rel]


def stamp(html):
    """Add or refresh ?v=<hash> on every versioned asset reference."""
    for rel in VERSIONED:
        pat = re.compile(r'(?<=["\'])(/?%s)(\?v=[0-9a-f]+)?(?=["\'])' % re.escape(rel))
        html = pat.sub(lambda m: m.group(1) + "?v=" + asset_version(rel), html)
    return html


def write(path, html):
    if path.endswith(".html"):
        html = stamp(html)
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
      <!-- If ANALYTICS_DOMAIN is switched on in js/main.js, delete the paragraph
           above, and uncomment the list item and paragraph below.
        <li><strong>Plausible Analytics</strong> — anonymous, cookieless visitor
        statistics.</li>
        <p>We use Plausible Analytics to count page views. It sets no cookies,
        collects no personal data and does not track visitors across websites or
        over time. No data is shared with advertising networks. The typeface is
        served from our own domain, so browsing this site does not disclose your
        IP address to any other company.</p>
      -->

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
# POSITIONS is the only block to edit when a vacancy opens or closes.
# Set `open: False` to move a role out of the live list without deleting it.
# ⚠️ Only add roles the company is actually recruiting for.
# ============================================================
POSITIONS = [
    dict(id="tig-welder",
         title="Certified TIG Welder",
         count="30 positions",
         location="Project sites across Europe",
         contract="Project-based",
         open=True,
         # --- Google for Jobs fields ---
         posted="2026-07-25",           # keep current; stale posts get demoted
         valid_through="2026-12-31",
         employment_type="CONTRACTOR",
         vacancies=30,
         countries=["LT", "BE", "NO"],
         summary="We are recruiting thirty certified TIG welders for upcoming project "
                 "scopes. This is the constraint on our current pipeline, so applications "
                 "are reviewed quickly.",
         needs=["Valid TIG welding certification with supporting documentation",
                "Willingness to travel and work on site across several countries",
                "Experience with pipe and steel structure welding",
                "Working English"]),
]

def positions_html():
    live = [p for p in POSITIONS if p.get("open")]
    if not live:
        return """      <div class="notice">
        <p><strong>No open positions right now.</strong> We still welcome open
        applications &mdash; use the form below and we will contact you when a project
        matches your profile.</p>
      </div>"""
    out = []
    for p in live:
        d = dict(p)
        d["needs"] = "\n".join("          <li>%s</li>" % n for n in p["needs"])
        out.append("""      <article class="position" id="{id}">
        <div class="position-head">
          <h3>{title}</h3>
          <p class="position-meta"><span>{count}</span><span>{location}</span><span>{contract}</span></p>
        </div>
        <p>{summary}</p>
        <p class="position-label">What we need</p>
        <ul>
{needs}
        </ul>
        <p><a class="btn-bracket" href="#apply" data-apply="{title}">Apply for this role</a></p>
      </article>""".format(**d))
    return "\n".join(out)


def position_options():
    opts = ['<option value="Open application">Open application</option>']
    for p in POSITIONS:
        if p.get("open"):
            opts.append('<option value="%s">%s</option>' % (p["title"], p["title"]))
    return "\n              ".join(opts)


CAREERS = """
    <div class="container page-head">
      <p class="eyebrow">Careers</p>
      <h1 class="page-title">Work with ALPROJECTS</h1>
      <p class="page-lead">We deliver mechanical contracting, welding, inspection and access
      services on industrial and offshore projects across Europe. The work is technical,
      certified and mostly on site.</p>
    </div>

    <div class="container prose">
      <h2>Open positions</h2>
%s

      <h2>We recruit regularly in these disciplines</h2>
      <p>Even when a role is not advertised, we keep qualified specialists on file and
      make contact when a project matches. These are the areas our project teams are
      built from:</p>
      <ul>
        <li>Welding services (TIG, MIG/MAG)</li>
        <li>Pipe fitting and piping prefabrication</li>
        <li>Mechanical contracting and installation</li>
        <li>Non-destructive testing (NDT)</li>
        <li>Rope access services</li>
        <li>Quality control and QAQC</li>
        <li>Rigging and technical support</li>
        <li>Project coordination and site supervision</li>
      </ul>

      <h2>What matters to us</h2>
      <ul>
        <li>Valid certification for your discipline, and the documentation to support it.</li>
        <li>Willingness to travel &mdash; our projects run in several countries.</li>
        <li>A serious approach to safety in complex and confined environments.</li>
        <li>Working English; Lithuanian, Russian or Polish are useful additions.</li>
      </ul>
    </div>

    <div class="container" id="apply">
      <div class="apply-panel">
        <div class="apply-intro">
          <p class="eyebrow">Apply</p>
          <h2>Send us your details</h2>
          <p>Tell us your discipline and certifications. We read every application and
          reply when a project matches your profile.</p>
          <p class="apply-note">Attach your CV and certificates to the email that opens
          when you submit &mdash; we do not accept file uploads through this page.</p>
        </div>

        <form id="applyForm" class="apply-form" novalidate>
          <div class="field">
            <label for="apName">Full name</label>
            <input id="apName" name="name" type="text" required autocomplete="name">
          </div>
          <div class="field">
            <label for="apEmail">Email</label>
            <input id="apEmail" name="email" type="email" required autocomplete="email">
          </div>
          <div class="field">
            <label for="apPhone">Phone <span class="opt">(optional)</span></label>
            <input id="apPhone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="apRole">Position</label>
            <select id="apRole" name="role">
              %s
            </select>
          </div>
          <div class="field">
            <label for="apCerts">Certifications <span class="opt">(optional)</span></label>
            <input id="apCerts" name="certifications" type="text"
                   placeholder="e.g. TIG 141, IRATA Level 2, VT/PT Level 2">
          </div>
          <div class="field field-wide">
            <label for="apMsg">Experience and availability</label>
            <textarea id="apMsg" name="message" rows="5" required
                      placeholder="Disciplines you work in, years of experience, and when you could start."></textarea>
          </div>
          <div class="field field-wide field-check">
            <input id="apConsent" name="consent" type="checkbox" required>
            <label for="apConsent">I agree that ALPROJECTS may store these details to
            consider me for current and future roles, as described in the
            <a href="/privacy.html">privacy policy</a>.</label>
          </div>
          <div class="field field-wide">
            <button type="submit" class="btn-solid">Send application</button>
            <p class="form-note" id="applyNote" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>
    </div>
""" % (positions_html(), position_options())

# ============================================================
# NEWS ARTICLES
# Written from ALprojects Group's own LinkedIn carousels, supplied by
# the client. The first three follow the slides closely; the last three
# came from post summaries and are less exact. Dates: LinkedIn reports
# posts relatively ("2d", "1w"), so those are derived from 15 Aug 2026 —
# verify before promoting. The award date is the certificate's own.
# ============================================================
ARTICLES = [
    dict(slug="we-do-not-certify-our-own-welds",
         num="01", date="13 Aug 2026", iso="2026-08-13", cat="Quality Control",
         img="news-3.webp", w=1000, h=562,
         alt="Weld profile gauge measuring a fillet weld",
         title="We do not certify our own welds",
         lead="Our NDT does not replace your inspector. We use it to catch our own mistakes first.",
         body=[
           "<strong>Where the line sits.</strong> Nobody should be signing off their own work, and we do not try to. Independent verification stays where the contract puts it, normally with the client or the class surveyor, and nothing we do changes that.",
           "Our own technicians come in before that. They go over the joint while the crew is still on the job, and if something has to come out, it comes out before anyone else is invited to look at it.",
           "<strong>Measured against the criteria.</strong> Cap height, width, undercut, profile. Each one is checked against the acceptance criteria for the job, and the joint is not presented until the numbers sit inside the limits.",
           "<strong>What the eye cannot pick up.</strong> Clean the weld, apply the penetrant, let the developer draw it back out. Surface cracks and porosity that nobody would catch by eye show up in red, and anything outside the limits is repaired on the spot.",
           "So there are two different things with the same equipment behind them. On our own jobs it is internal quality control, and it never counts as sign-off. On somebody else's welds it is independent NDT, because we did not weld it.",
         ],
         facts=[("On our own jobs", "Internal quality control", "It never counts as sign off"),
                ("On somebody else's welds", "Independent NDT", "We did not weld it")],
         cta="Send us the scope and we will come back with a price and crew dates."),

    dict(slug="piping-installation-engine-room",
         num="02", date="08 Aug 2026", iso="2026-08-08", cat="Shipbuilding",
         img="news-1.webp", w=831, h=554,
         alt="Engine room piping installation on board",
         title="Piping installation in the engine room",
         lead="Sea water, bilge, ballast and fuel lines going in on board right now.",
         body=[
           "Our crew is installing engine room systems on vessels under construction: seawater, bilge, ballast, fuel and service lines running from small bore up to DN200 around the main engine foundations.",
           "<strong>Drawn first, then built.</strong> Isometrics are checked before anything is cut. Spools are prefabricated in the shop, fitted on board and hung so the line can move without loading the welds.",
           "<strong>Manifolds, sea chests, tank connections.</strong> Gate valves, strainers and remote operated units set out and aligned on the tank top. Flange faces stay capped until the system is closed.",
           "<strong>Welded, tested, then closed.</strong> Welding under ISO 3834. Every joint is documented, and NDT and pressure testing are done before insulation and final coating go on.",
           "The order of work stays the same on every job. Most of the time in a machinery space goes on getting the routing right, not on the welding itself.",
         ],
         facts=[("Certified to", "ISO 3834", "Welding quality requirements"),
                ("Working from", "Lithuania, Belgium, Norway", "Offshore, shipbuilding and industry")],
         cta="Send us the drawings and we will come back with a price and crew dates."),

    dict(slug="strongest-in-lithuania-2025-2026",
         num="03", date="23 Jun 2026", iso="2026-06-23", cat="Company",
         img="news-2.webp", w=1000, h=750,
         alt="ALPROJECTS Group project site",
         title="Among the strongest companies in Lithuania",
         seo="Among Lithuania's strongest companies",
         lead="UAB \u201cALprojects\u201d has been awarded the Strongest in Lithuania 2025\u20132026 certificate by Creditinfo.",
         body=[
           "The certificate recognises companies with a high credit score and a proven record of financial stability. It is issued by Creditinfo Group and was awarded on 23 June 2026 for the 2025\u20132026 period.",
           "<strong>A stable partner is a safer project.</strong> In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through.",
           "That matters more than a logo on a wall. It is the difference between a contractor who can carry a scope to completion and one who cannot.",
         ],
         facts=[("Award", "Strongest in Lithuania", "2025\u20132026"),
                ("Issued by", "Creditinfo Group", "23 June 2026")],
         cta="Planning a project across shipbuilding, piping or industrial services? Let us talk."),

    dict(slug="transformer-mechanical-package",
         num="04", date="01 Aug 2026", iso="2026-08-01", cat="Industrial Projects",
         img="news-2.webp", w=1000, h=750,
         alt="Industrial installation works",
         title="A transformer mechanical package across five countries",
         seo="Transformer package, five countries",
         lead="Stainless steel piping, cooling systems and precision installation \u2014 repeated across five European sites.",
         body=[
           "A transformer mechanical package covers the stainless steel piping and cooling systems that keep the unit within its operating envelope. The tolerances are tight and the commissioning window is usually short.",
           "What made this scope demanding was not any single site but the repetition: the same package delivered across five European countries, each with its own site conditions, inspection regime and local requirements.",
           "Consistency across borders is a documentation problem as much as a fabrication one \u2014 which is where certified personnel and a single quality system earn their place.",
         ],
         facts=[], cta="Send us the scope and we will come back with a price and crew dates."),

    dict(slug="fuel-loading-terminal-completed",
         num="05", date="25 Jul 2026", iso="2026-07-25", cat="Energy Projects",
         img="news-2.webp", w=1000, h=750,
         alt="Port and terminal infrastructure",
         title="Fuel loading terminal completed",
         lead="September 2025 to April 2026. Twelve specialists. Over 11,000 hours on site.",
         body=[
           "The scope ran from September 2025 to April 2026 and was delivered by a team of twelve specialists, accumulating more than 11,000 hours on site.",
           "Fuel handling infrastructure concentrates every discipline we work in \u2014 mechanical installation, pipe fitting, welding, and the inspection and documentation that has to accompany all three when the medium is flammable.",
           "Numbers like 11,000 hours are worth stating plainly: they are what a project of this size actually costs in skilled labour, and planning against a lower figure is how schedules fail.",
         ],
         facts=[], cta="Send us the scope and we will come back with a price and crew dates."),

    dict(slug="europe-tig-welder-shortage",
         num="06", date="25 Jul 2026", iso="2026-07-25", cat="Industry",
         img="news-3.webp", w=1000, h=562,
         alt="Precision welding on a workshop bench",
         title="We needed 30 certified TIG welders. Europe could not supply them.",
         seo="We needed 30 certified TIG welders",
         lead="The skilled trades shortage is not an abstraction when it is your project that cannot start.",
         body=[
           "Recruiting thirty certified TIG welders for a single scope of work turned out to be materially harder than the engineering it supported.",
           "The shortage is discussed across European industry in general terms. It becomes concrete when a project is resourced, scheduled and funded, and the constraint is simply the number of people who hold the certification and are willing to travel.",
           "It is worth being direct about this, because the answer is not a recruitment campaign. It is training, certification pathways, and treating the trades as a career rather than a stopgap.",
         ],
         facts=[], cta="If you hold the ticket and you are willing to travel, we would like to hear from you."),
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
      <!-- NOTE(ALPROJECTS): written from your own LinkedIn carousel. Relative
           post dates ("2d", "1w") were resolved against 15 Aug 2026 — check them.
           The photo is stock from the original design, not the post's image. -->
      <p class="article-lead">{lead}</p>
{paras}
{factblock}
      <p class="article-cta">{cta}</p>
      <p class="back">
        <a class="btn-bracket" href="/contacts.html">Start a project</a>
        <a class="btn-bracket" href="/news/">All news</a>
      </p>
    </div>
"""

def facts_html(facts):
    if not facts:
        return ""
    cells = "\n".join(
        """        <div class="fact">
          <p class="fact-label">%s</p>
          <p class="fact-value">%s</p>
          <p class="fact-note">%s</p>
        </div>""" % f for f in facts)
    return '      <div class="fact-strip">\n%s\n      </div>' % cells


def news_index():
    cards = []
    for i, a in enumerate(ARTICLES):
        # The first row sits above the fold, so lazy-loading it delays the LCP
        # by a round trip. Everything from row two down stays lazy.
        eager = i < 3
        card = dict(a, loading="eager" if eager else "lazy",
                    prio=' fetchpriority="high"' if i == 0 else "")
        cards.append("""        <a class="news-card" href="/news/{slug}.html">
          <span class="news-top"><span class="num">{num}</span><span>{date} &middot; {cat}</span><span class="arr">&#8599;</span></span>
          <span class="thumb"><img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="{loading}"{prio}></span>
          <h2>{title}</h2>
        </a>""".format(**card))
    return """
    <div class="container page-head">
      <p class="eyebrow">Our news</p>
      <h1 class="page-title">Project Updates &amp; Engineering Insights</h1>
      <p class="page-lead">Work in progress, completed scopes, and what we are learning across
      shipbuilding, offshore, industrial and energy projects.</p>
    </div>

    <div class="container">
      <div class="news-grid">
%s
      </div>
    </div>
""" % "\n".join(cards)


# ============================================================
# COMPANY
# ============================================================
COMPANY = """
    <div class="container page-head">
      <p class="eyebrow">Company</p>
      <h1 class="page-title">A European provider of industrial services</h1>
      <p class="page-lead">ALPROJECTS Group serves the shipbuilding, offshore, industrial and
      energy sectors, from a head office in Klaipeda, Lithuania.</p>
    </div>

    <div class="container prose">
      <h2>What we do</h2>
      <p>We specialise in piping prefabrication and installation, steel fabrication and
      mechanical installation, and we provide certified technical personnel to projects
      across Europe. In practice that means we are engaged either to deliver a defined
      mechanical scope, or to supply the qualified people a project is short of &mdash;
      often both on the same site.</p>

      <h2>Sectors</h2>
      <ul>
        <li><strong>Shipbuilding</strong> — piping and mechanical installation on vessels under construction.</li>
        <li><strong>Offshore</strong> — inspection, access and mechanical works on offshore facilities.</li>
        <li><strong>Industrial</strong> — plant installation, transformer packages, process piping.</li>
        <li><strong>Energy and renewables</strong> — fuel handling infrastructure and wind energy support.</li>
      </ul>

      <h2>Certification</h2>
      <p>ALPROJECTS Group holds <strong>ISO 3834</strong> for welding quality requirements,
      alongside ISO 9001, ISO 14001 and ISO 45001 covering quality, environmental and
      occupational health and safety management. Certification is what allows a client to
      accept our documentation without re-doing the inspection themselves.</p>

      <h2>Strongest in Lithuania, 2025&ndash;2026</h2>
      <p>UAB &ldquo;ALprojects&rdquo; holds the <strong>Strongest in Lithuania</strong>
      certificate, awarded by Creditinfo Group on 23 June 2026 to companies with a high
      credit score and a proven record of financial stability.</p>
      <p>In heavy industry, projects run for months and commitments run for years.
      Independent proof of financial stability is proof that we will be there to see the
      work through &mdash; which is a different question from whether the welding is any
      good, and worth answering separately.
      <a href="/news/strongest-in-lithuania-2025-2026.html">More on the award</a>.</p>

      <h2>Where we work from</h2>
      <p>Head office in Klaipeda, Lithuania, with operations in <strong>Belgium</strong>
      and <strong>Norway</strong>, serving offshore, shipbuilding and industry across
      Northern and Western Europe.</p>

      <h2>Scale</h2>
      <p>The company employs between 51 and 200 people and works across multiple European
      countries. Projects are resourced from a pool of certified specialists rather than
      subcontracted on, which is what keeps the quality system meaningful.</p>

      <h2>Head office</h2>
      <p>ALPROJECTS, UAB<br>Silutes av. 2-536, LT-91110 Klaipeda, Lithuania<br>
      <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot;
      <a href="tel:+37063663744">+370 636 63 744</a></p>

      <p class="back">
        <a class="btn-bracket" href="/services.html">Our services</a>
        <a class="btn-bracket" href="/#team">Meet the team</a>
      </p>
    </div>
"""

# ============================================================
# SERVICES
# ============================================================
SERVICES = """
    <div class="container page-head">
      <p class="eyebrow">Services</p>
      <h1 class="page-title">Integrated Inspection &amp; Access Services</h1>
      <p class="page-lead">Five service lines that are usually bought separately and work
      better together — inspection, access, measurement, control and lifting.</p>
    </div>

    <div class="container prose">
      <h2>Non-destructive testing (NDT)</h2>
      <p>We inspect welds, materials and structures without interrupting operations, so
      defects are identified early rather than at handover. Cap height, width, undercut and
      profile are checked against the acceptance criteria for the job; penetrant goes on the
      butt welds to find surface cracks and porosity no one would catch by eye.</p>
      <p>There are two different things here, and we keep them apart deliberately:</p>
      <div class="fact-strip">
        <div class="fact">
          <p class="fact-label">On our own jobs</p>
          <p class="fact-value">Internal quality control</p>
          <p class="fact-note">It never counts as sign off</p>
        </div>
        <div class="fact">
          <p class="fact-label">On somebody else's welds</p>
          <p class="fact-value">Independent NDT</p>
          <p class="fact-note">We did not weld it</p>
        </div>
      </div>
      <p>Nobody should be signing off their own work, and we do not try to. Independent
      verification stays where the contract puts it — normally with the client or the
      class surveyor. Our technicians simply get there first, while the crew is still on the
      job. See <a href="/news/we-do-not-certify-our-own-welds.html">we do not certify our own welds</a>.</p>
      <p class="svc-industries">Offshore oil &amp; gas · Wind energy · Industrial facilities · Steel structures</p>

      <h2>Rope access services</h2>
      <p>Certified rope access lets inspection and mechanical work reach locations that
      would otherwise need scaffolding or a shutdown. It is faster to mobilise, cheaper
      than staging, and in many offshore situations the only practical option.</p>
      <p class="svc-industries">Offshore · Wind energy · Industrial plants · Marine facilities</p>

      <h2>3D laser scanning</h2>
      <p>We capture precise as-built geometry of structures and piping systems. The point
      cloud supports dimensional control, clash detection and retrofit engineering &mdash;
      which is what stops a perfectly fabricated spool from arriving at a compartment it
      does not fit.</p>
      <p class="svc-industries">Industrial plants · Offshore structures · Wind energy · Infrastructure</p>

      <h2>Quality control and QAQC</h2>
      <p>Quality control for piping and steel structures: inspection and verification
      against WPS, drawings and applicable standards, with traceability and documentation
      maintained throughout. Certification is only worth what the paperwork behind it can
      demonstrate.</p>
      <p class="svc-industries">Offshore &amp; marine · Energy · Heavy industry · Steel fabrication</p>

      <h2>Rigging and technical support</h2>
      <p>Lifting, rigging and installation works for industrial and offshore projects,
      including the planning, coordination and supervision that makes them safe. Work is
      performed under controlled procedures with safety compliance at every stage.</p>
      <p class="svc-industries">Offshore · Industrial construction · Energy projects · Marine facilities</p>

      <h2>Mechanical scopes</h2>
      <p>Alongside the inspection and access lines, we deliver piping prefabrication and
      installation, steel fabrication and mechanical installation as complete scopes, and
      supply certified technical personnel to projects that need them.</p>

      <p class="back">
        <a class="btn-bracket" href="/projects.html">Where we work</a>
        <a class="btn-bracket" href="/contacts.html">Discuss a project</a>
      </p>
    </div>
"""

# ============================================================
# PROJECTS
# ============================================================
PROJECTS = """
    <div class="container page-head">
      <p class="eyebrow">Projects</p>
      <h1 class="page-title">Where we work</h1>
      <p class="page-lead">Four project types, one set of disciplines. The engineering is
      largely the same; the environment, the standards and the consequences of getting it
      wrong are not.</p>
    </div>

    <div class="container prose">
      <h2>Shipbuilding</h2>
      <p>Piping and mechanical installation on vessels under construction — seawater,
      bilge and fuel systems routed through compartments that are already full of
      machinery, structure and other trades. Prefabrication and installation are handled
      together, because a spool built to drawing but not to the as-built compartment is
      scrap.</p>

      <h2>Offshore</h2>
      <p>Inspection, access and mechanical works on offshore facilities, where mobilising
      a team is expensive and a shutdown is more expensive still. Rope access and NDT
      carry most of this work; visual inspection plays a central role in confirming the
      safety and operational integrity of oil, gas and wind energy assets.</p>

      <h2>Industrial projects</h2>
      <p>Plant installation, process piping and mechanical packages. A recent example is a
      transformer mechanical package — stainless steel piping and cooling systems &mdash;
      <a href="/news/transformer-mechanical-package.html">delivered across five European
      countries</a>, where consistency across borders was as much a documentation problem
      as a fabrication one.</p>

      <h2>Renewable and energy projects</h2>
      <p>Fuel handling infrastructure and wind energy support. Our
      <a href="/news/fuel-loading-terminal-completed.html">fuel loading terminal scope</a>
      ran from September 2025 to April 2026 with twelve specialists and over 11,000 hours
      on site — a useful figure for anyone planning work of that size.</p>

      <p class="back">
        <a class="btn-bracket" href="/services.html">Our services</a>
        <a class="btn-bracket" href="/contacts.html">Start a project</a>
      </p>
    </div>
"""

# ============================================================
# CONTACTS
# ============================================================
CONTACTS = """
    <div class="container page-head">
      <p class="eyebrow">Contacts</p>
      <h1 class="page-title">Talk to us</h1>
      <p class="page-lead">Project enquiries, personnel requests and open applications all
      reach the same inbox — it is read by people who can answer technical questions.</p>
    </div>

    <div class="container prose">
      <h2>Head office</h2>
      <p>ALPROJECTS, UAB<br>
      Silutes av. 2-536<br>
      LT-91110 Klaipeda<br>
      Lithuania</p>

      <h2>Where we work from</h2>
      <p>Lithuania &middot; Belgium &middot; Norway &mdash; serving offshore, shipbuilding and
      industry across Northern and Western Europe.</p>

      <h2>Email</h2>
      <p><a href="mailto:info@alprojects.eu">info@alprojects.eu</a></p>

      <h2>Phone</h2>
      <ul>
        <li><a href="tel:+37063663744">+370 636 63 744</a></li>
        <li><a href="tel:+37067020654">+370 670 20654</a></li>
      </ul>

      <h2>What to include</h2>
      <p>Send us the scope or the drawings and we will come back with a price and crew
      dates. The fastest route to a useful answer is the scope, the location, the standards
      that apply and the window you are working to. For personnel requests, tell us the
      disciplines, certifications and headcount.</p>

      <p class="back">
        <a class="btn-bracket" href="mailto:info@alprojects.eu?subject=Project%20enquiry">Email us</a>
        <a class="btn-bracket" href="/careers.html">Careers</a>
      </p>
    </div>
"""


# ============================================================
# STRUCTURED DATA
# JobPosting puts open roles into Google for Jobs at no cost —
# the point of it here is the TIG welder shortage. Article and
# BreadcrumbList help the news pages surface properly.
# ============================================================
import json

ORG = {
    "@type": "Organization",
    "name": "ALPROJECTS Group",
    "sameAs": "https://alprojects.co/",
    "logo": "https://alprojects.co/assets/logo.png",
}

def _strip(o):
    """Google rejects null-valued properties — drop them rather than emit null."""
    if isinstance(o, dict):
        return {k: _strip(v) for k, v in o.items() if v is not None and v != []}
    if isinstance(o, list):
        return [_strip(v) for v in o]
    return o

def jsonld(obj):
    obj = _strip(obj)
    return ('  <script type="application/ld+json">\n  %s\n  </script>\n'
            % json.dumps(obj, indent=2, ensure_ascii=False).replace("\n", "\n  "))

def job_postings_ld():
    out = []
    for p in POSITIONS:
        if not p.get("open"):
            continue
        desc = ("<p>%s</p><p>What we need:</p><ul>%s</ul>"
                % (p["summary"], "".join("<li>%s</li>" % n for n in p["needs"])))
        out.append(jsonld({
            "@context": "https://schema.org",
            "@type": "JobPosting",
            "title": p["title"],
            "description": desc,
            "identifier": {"@type": "PropertyValue", "name": "ALPROJECTS Group", "value": p["id"]},
            "datePosted": p["posted"],
            "validThrough": p["valid_through"] + "T23:59",
            "employmentType": p["employment_type"],
            "totalJobOpenings": p.get("vacancies"),
            "hiringOrganization": ORG,
            "jobLocation": [{
                "@type": "Place",
                "address": {"@type": "PostalAddress",
                            "addressLocality": "Klaipeda",
                            "postalCode": "LT-91110",
                            "streetAddress": "Silutes av. 2-536",
                            "addressCountry": "LT"},
            }],
            "applicantLocationRequirements": [
                {"@type": "Country", "name": c} for c in p.get("countries", [])
            ],
            "directApply": True,
            "industry": "Industrial services, shipbuilding, offshore",
        }))
    return "".join(out)

def article_ld(a):
    return jsonld({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["lead"],
        "image": "https://alprojects.co/assets/" + a["img"],
        "datePublished": a["iso"],
        "dateModified": a["iso"],
        "author": ORG,
        "publisher": ORG,
        "mainEntityOfPage": "https://alprojects.co/news/%s.html" % a["slug"],
    })

def breadcrumb_ld(trail):
    return jsonld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": "https://alprojects.co" + u}
            for i, (n, u) in enumerate(trail)
        ],
    })

OG_CARDS = {"we-do-not-certify-our-own-welds", "piping-installation-engine-room",
            "strongest-in-lithuania-2025-2026"}

# ---------------- write everything ----------------
write("privacy.html", page("Privacy Policy",
      "How ALPROJECTS Group handles personal data collected through this website.",
      PRIVACY, canonical="/privacy.html"))

write("careers.html", page("Careers",
      "Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.",
      CAREERS, canonical="/careers.html", og="careers",
      head_extra=job_postings_ld() +
                 breadcrumb_ld([("Home", "/"), ("Careers", "/careers.html")])))

write("company.html", page("Company",
      "ALPROJECTS Group is a European provider of industrial services for the shipbuilding, offshore, industrial and energy sectors.",
      COMPANY, canonical="/company.html", og="company"))

write("services.html", page("Services",
      "NDT, rope access, 3D laser scanning, quality control and rigging for industrial and offshore projects across Europe.",
      SERVICES, canonical="/services.html", og="services"))

write("projects.html", page("Projects",
      "Shipbuilding, offshore, industrial and renewable energy projects delivered by ALPROJECTS Group across Europe.",
      PROJECTS, canonical="/projects.html", og="projects"))

write("contacts.html", page("Contacts",
      "Contact ALPROJECTS Group — Silutes av. 2-536, Klaipeda, Lithuania. Project enquiries and personnel requests.",
      CONTACTS, canonical="/contacts.html", og="contacts"))

write("news/index.html", page("News",
      "Project updates and engineering insights from ALPROJECTS Group.",
      news_index(), canonical="/news/", og="news"))

for a in ARTICLES:
    body = dict(a)
    body["paras"] = "\n".join("      <p>%s</p>" % p for p in a["body"])
    body["factblock"] = facts_html(a.get("facts"))
    write("news/%s.html" % a["slug"],
          page(a.get("seo", a["title"]), a["lead"], ARTICLE_BODY.format(**body),
               canonical="/news/%s.html" % a["slug"],
               og=(a["slug"] if a["slug"] in OG_CARDS else "news"),
               head_extra=article_ld(a) + breadcrumb_ld(
                   [("Home", "/"), ("News", "/news/"),
                    (a["title"], "/news/%s.html" % a["slug"])])))


# ---------------- sitemap ----------------
# Generated from the same page list that writes the HTML, so a renamed or
# added article can never leave a dead URL behind in the sitemap.
SITEMAP = [
    ("/",              "monthly", "1.0"),
    ("/services.html", "monthly", "0.9"),
    ("/projects.html", "monthly", "0.9"),
    ("/company.html",  "monthly", "0.8"),
    ("/news/",         "weekly",  "0.8"),
    ("/contacts.html", "yearly",  "0.7"),
    ("/careers.html",  "monthly", "0.6"),
    ("/privacy.html",  "yearly",  "0.2"),
] + [("/news/%s.html" % a["slug"], "yearly", "0.6") for a in ARTICLES]

def sitemap():
    urls = "\n".join(
        '  <url>\n'
        '    <loc>https://alprojects.co%s</loc>\n'
        '    <lastmod>%s</lastmod>\n'
        '    <changefreq>%s</changefreq>\n'
        '    <priority>%s</priority>\n'
        '  </url>' % (loc, LASTMOD, freq, pri)
        for loc, freq, pri in SITEMAP)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + urls + '\n</urlset>\n')

write("sitemap.xml", sitemap())


# index.html and 404.html are hand-maintained rather than generated, so stamp
# them in place -- otherwise they would be the pages that still serve stale CSS.
for _name in ("index.html", "404.html"):
    _path = os.path.join(ROOT, _name)
    _before = io.open(_path, encoding="utf-8").read()
    _after = stamp(_before)
    if _after != _before:
        io.open(_path, "w", encoding="utf-8").write(_after)
        print("stamped %s" % _name)

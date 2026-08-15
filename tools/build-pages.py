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
    # NB: skip #main (skip-link) and #i-* (SVG sprite <use> refs) — rewriting
    # the sprite refs to /#i-* silently breaks every icon on the page.
    html = re.sub(r'href="#(?!main\b)(?!i-)([a-z-]+)"', r'href="/#\1"', html)
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
# POSITIONS is the only block to edit when a vacancy opens or closes.
# Set `open: False` to move a role out of the live list without deleting it.
# ⚠️ Only add roles the company is actually recruiting for.
# ============================================================
POSITIONS = [
    dict(id="tig-welder",
         title="Certified TIG Welders",
         count="30 positions",
         location="Project sites across Europe",
         contract="Project-based",
         open=True,
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
# Written from ALprojects Group's own LinkedIn posts (retrieved
# 15 Aug 2026). ⚠️ Dates are APPROXIMATE — LinkedIn reports posts
# as "2 days ago" / "3 weeks ago", not as calendar dates. The
# wording is derived from those posts, not quoted verbatim.
# Have the client verify both before launch.
# ============================================================
ARTICLES = [
    dict(slug="ndt-independent-verification",
         num="01", date="13 Aug 2026", iso="2026-08-13", cat="Quality Control",
         img="news-3.webp", w=1000, h=562,
         alt="Precision welding inspected on a workshop bench",
         title="Why we verify welds we did not make",
         lead="Non-destructive testing only means something when the party inspecting the weld is not the party being graded on it.",
         body=[
           "Our NDT work is built around independent verification. When we inspect a weld, our job is to find the defect — not to certify our own workmanship. That separation is the entire value of the inspection.",
           "The practical effect is that defects surface before client sign-off rather than after it. A weld rejected at inspection is a repair; the same weld found after handover is a warranty claim, a delay, and in the wrong environment a safety event.",
           "It is a slower way to work and occasionally an uncomfortable one. It is also the only version of quality control that is worth paying for.",
         ]),
    dict(slug="engine-room-piping-installation",
         num="02", date="08 Aug 2026", iso="2026-08-08", cat="Shipbuilding",
         img="news-1.webp", w=831, h=554,
         alt="Welder performing mechanical installation works",
         title="Engine room piping on vessels under construction",
         lead="Seawater, bilge and fuel systems, installed in the most congested compartment on the ship.",
         body=[
           "Engine room piping is unforgiving work. Seawater, bilge and fuel systems all have to be routed through a compartment that is already full of machinery, structure and other trades — and each system carries its own material, pressure and testing requirements.",
           "Our teams handle prefabrication and installation together, which matters more here than almost anywhere else on a vessel: a spool that is fabricated to drawing but not to the as-built compartment is scrap.",
           "The work is carried out on vessels under construction, alongside the yard's own schedule.",
         ]),
    dict(slug="transformer-mechanical-package",
         num="03", date="01 Aug 2026", iso="2026-08-01", cat="Industrial Projects",
         img="news-2.webp", w=1000, h=750,
         alt="Port infrastructure at sunset",
         title="A transformer mechanical package across five countries",
         lead="Stainless steel piping, cooling systems and precision installation — repeated across five European sites.",
         body=[
           "A transformer mechanical package covers the stainless steel piping and cooling systems that keep the unit within its operating envelope. The tolerances are tight and the commissioning window is usually short.",
           "What made this scope demanding was not any single site but the repetition: the same package delivered across five European countries, each with its own site conditions, inspection regime and local requirements.",
           "Consistency across borders is a documentation problem as much as a fabrication one — which is where certified personnel and a single quality system earn their place.",
         ]),
    dict(slug="fuel-loading-terminal-completed",
         num="04", date="25 Jul 2026", iso="2026-07-25", cat="Energy Projects",
         img="news-2.webp", w=1000, h=750,
         alt="Port infrastructure at sunset",
         title="Fuel loading terminal completed",
         lead="September 2025 to April 2026. Twelve specialists. Over 11,000 hours on site.",
         body=[
           "The scope ran from September 2025 to April 2026 and was delivered by a team of twelve specialists, accumulating more than 11,000 hours on site.",
           "Fuel handling infrastructure concentrates every discipline we work in — mechanical installation, pipe fitting, welding, and the inspection and documentation that has to accompany all three when the medium is flammable.",
           "Numbers like 11,000 hours are worth stating plainly: they are what a project of this size actually costs in skilled labour, and planning against a lower figure is how schedules fail.",
         ]),
    dict(slug="europe-tig-welder-shortage",
         num="05", date="25 Jul 2026", iso="2026-07-25", cat="Industry",
         img="news-3.webp", w=1000, h=562,
         alt="Precision welding on a workshop bench",
         title="We needed 30 certified TIG welders. Europe could not supply them.",
         lead="The skilled trades shortage is not an abstraction when it is your project that cannot start.",
         body=[
           "Recruiting thirty certified TIG welders for a single scope of work turned out to be materially harder than the engineering it supported.",
           "The shortage is discussed across European industry in general terms. It becomes concrete when a project is resourced, scheduled and funded, and the constraint is simply the number of people who hold the certification and are willing to travel.",
           "It is worth being direct about this, because the answer is not a recruitment campaign. It is training, certification pathways, and treating the trades as a career rather than a stopgap.",
         ]),
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
      <!-- NOTE(ALPROJECTS): written from your LinkedIn post of approximately this
           date. The date is approximate and the wording is ours, not a verbatim
           quote of the post. Please verify both before promoting this page. -->
      <p class="article-lead">{lead}</p>
{paras}
      <p class="back"><a class="btn-bracket" href="/news/">All news</a></p>
    </div>
"""

def news_index():
    cards = []
    for a in ARTICLES:
        cards.append("""        <a class="news-card" href="/news/{slug}.html">
          <span class="news-top"><span class="num">{num}</span><span>{date} &middot; {cat}</span><span class="arr">&#8599;</span></span>
          <span class="thumb"><img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></span>
          <h4>{title}</h4>
        </a>""".format(**a))
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
      <p>ALPROJECTS Group holds ISO 9001, ISO 14001 and ISO 45001 certification, covering
      quality management, environmental management and occupational health and safety.
      Certification is what allows a client to accept our documentation without re-doing
      the inspection themselves.</p>

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
      defects are identified early rather than at handover. Our NDT is deliberately
      independent of the work being inspected — see
      <a href="/news/ndt-independent-verification.html">why we verify welds we did not make</a>.</p>
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

      <h2>Email</h2>
      <p><a href="mailto:info@alprojects.eu">info@alprojects.eu</a></p>

      <h2>Phone</h2>
      <ul>
        <li><a href="tel:+37063663744">+370 636 63 744</a></li>
        <li><a href="tel:+37067020654">+370 670 20654</a></li>
      </ul>

      <h2>What to include</h2>
      <p>For a project enquiry, the fastest route to a useful answer is the scope, the
      location, the standards that apply and the window you are working to. For personnel
      requests, tell us the disciplines, certifications and headcount.</p>

      <p class="back">
        <a class="btn-bracket" href="mailto:info@alprojects.eu?subject=Project%20enquiry">Email us</a>
        <a class="btn-bracket" href="/careers.html">Careers</a>
      </p>
    </div>
"""

# ---------------- write everything ----------------
write("privacy.html", page("Privacy Policy",
      "How ALPROJECTS Group handles personal data collected through this website.",
      PRIVACY, canonical="/privacy.html"))

write("careers.html", page("Careers",
      "Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.",
      CAREERS, canonical="/careers.html"))

write("company.html", page("Company",
      "ALPROJECTS Group is a European provider of industrial services for the shipbuilding, offshore, industrial and energy sectors.",
      COMPANY, canonical="/company.html"))

write("services.html", page("Services",
      "NDT, rope access, 3D laser scanning, quality control and rigging for industrial and offshore projects across Europe.",
      SERVICES, canonical="/services.html"))

write("projects.html", page("Projects",
      "Shipbuilding, offshore, industrial and renewable energy projects delivered by ALPROJECTS Group across Europe.",
      PROJECTS, canonical="/projects.html"))

write("contacts.html", page("Contacts",
      "Contact ALPROJECTS Group — Silutes av. 2-536, Klaipeda, Lithuania. Project enquiries and personnel requests.",
      CONTACTS, canonical="/contacts.html"))

write("news/index.html", page("News",
      "Project updates and engineering insights from ALPROJECTS Group.",
      news_index(), canonical="/news/"))

for a in ARTICLES:
    body = dict(a)
    body["paras"] = "\n".join("      <p>%s</p>" % p for p in a["body"])
    write("news/%s.html" % a["slug"],
          page(a["title"][:60], a["lead"], ARTICLE_BODY.format(**body),
               canonical="/news/%s.html" % a["slug"]))

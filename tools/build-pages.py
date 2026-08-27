#!/usr/bin/env python3
"""
Generates the sub-pages (privacy, careers, news articles) from the chrome in
index.html, so the header, footer and icon sprite never drift out of sync.

Not required to serve the site — the output is committed. Re-run it only after
editing the header or footer in index.html:

    python3 tools/build-pages.py
"""
import datetime, hashlib, html as _html, io, json as _json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


# rootify now lives in tools/paths.py: the translation build needs the same
# rewriting for the language trees, and two copies would drift.
from paths import rootify, clean_urls  # noqa: E402


HEADER_R, FOOTER_R, SPRITE_R = rootify(HEADER), rootify(FOOTER), rootify(SPRITE)


def page(title, description, body, noindex=False, canonical=None, head_extra="", og="home"):
    robots = ('  <meta name="robots" content="noindex, follow">\n' if noindex
              else '  <meta name="robots" content="index, follow">\n')
    canon = ('  <link rel="canonical" href="https://alprojects.co%s">\n' % canonical
             if canonical else "")
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Marks that scripting is available. The reveal animations start from
       opacity:0, so without this a JS failure would leave the page blank. -->
  <script>document.documentElement.className += " js";</script>
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
  <link rel="icon" type="image/svg+xml" href="/assets/logo.svg">
  <link rel="alternate icon" type="image/png" href="/assets/logo.png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
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
        html = clean_urls(stamp(html))
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
        <li>ALPROJECTS, UAB — Šilutės pl. 2-536, LT-91110 Klaipėda, Lithuania</li>
        <li>Email: <a href="mailto:info@alprojects.eu">info@alprojects.eu</a></li>
        <li>Phone: <a href="tel:+37063663744">+370 636 63 744</a></li>
      </ul>

      <h2>2. What we collect</h2>
      <p>This website has no user accounts, no analytics and sets no cookies of its own.
      Data reaches us in the following ways:</p>
      <ul>
        <li><strong>Newsletter.</strong> If you submit the newsletter form, we receive the
        email address you enter, in order to send you company and project updates.</li>
        <li><strong>Direct contact.</strong> If you email or call us, we receive whatever
        you choose to send — typically your name, contact details and the content of
        your enquiry.</li>
        <li><strong>Server logs.</strong> The site is hosted on GitHub Pages. GitHub
        records technical request data, including IP address and browser user-agent,
        for security and reliability.</li>
        <li><strong>Booking a call.</strong> If you open the scheduling calendar on the
        contacts page and book a slot, Calendly receives the name, email address and any
        notes you enter, together with your IP address and time zone.</li>
        <li><strong>Job applications.</strong> If you send the careers form we receive the
        details you enter &mdash; name, contact details, discipline, certificates,
        availability and any notes &mdash; together with any CV or certificate documents
        you attach.</li>
      </ul>

      <h2>3. Third parties that receive data</h2>
      <ul>
        <li><strong>GitHub, Inc.</strong> &mdash; website hosting and request logs.</li>
        <li><strong>Calendly LLC</strong> &mdash; the scheduling calendar on the contacts
        page, and only if you choose to open it.</li>
      </ul>
      <p>Simply browsing this site loads no third-party scripts, fonts, analytics or
      embeds. The typeface is served from our own domain, so reading these pages does not
      disclose your IP address to any advertising or analytics company.</p>
      <p>The one exception is the scheduling calendar on the contacts page. It is supplied
      by Calendly LLC and is <strong>not loaded until you press &ldquo;Open the
      calendar&rdquo;</strong>. Until you do, no request is made to Calendly and they
      receive nothing about you. Once you open it, Calendly receives your IP address and
      sets its own cookies in order to run the calendar, and the details you submit if you
      book a slot. Calendly is a US company and transfers are covered by the EU
      Standard Contractual Clauses; see
      <a href="https://calendly.com/privacy" target="_blank" rel="noopener">calendly.com/privacy</a>.
      You can book a call by email instead if you prefer not to use it.</p>
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

      <h2>3a. Recruitment data</h2>
      <p>Applications are held for <strong>24 months</strong> from the date you send them,
      so that we can contact you when a project matches your discipline. You can ask us to
      delete them at any time by writing to
      <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>, and we will do so without
      needing a reason.</p>
      <p>CVs and certificate documents are stored with the application and are seen only by
      the people resourcing projects. We do not pass them to third parties, and we do not
      use them for anything other than recruitment.</p>

      <h2>4. Legal basis</h2>
      <ul>
        <li><strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription,
        job applications, and loading the scheduling calendar, which happens only when you
        press the button. You may withdraw it at any time.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)) — responding to enquiries,
        and keeping the site secure and available.</li>
      </ul>

      <h2>5. How long we keep it</h2>
      <p>Job applications, including any CV and certificates, are kept for 24 months from
      the date you send them, or until you ask us to delete them.</p>
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
      (Valstybinė duomenų apsaugos inspekcija), L. Sapiegos g. 17, LT-10312 Vilnius, <a href="mailto:ada@ada.lt">ada@ada.lt</a>, <a href="https://vdai.lrv.lt" target="_blank" rel="noopener">vdai.lrv.lt</a>.</p>

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
         # ⚠️ BLOCKED ON CLIENT. These three are the first thing a rotation
         # worker looks for, and thirty welders will not be found without a
         # rate. A row with no value is omitted rather than printed as "to be
         # confirmed" -- fill these in and the rows appear.
         rotation="",
         start="",
         rate="",
         open=True,
         # --- Google for Jobs fields ---
         posted="2026-07-25",           # keep current; stale posts get demoted
         valid_through="2026-12-31",
         employment_type="CONTRACTOR",
         vacancies=30,
         countries=["LT", "BE", "NO"],
         summary="We are recruiting 30 certified TIG welders for upcoming project "
                 "scopes. This is the constraint on our current pipeline, so applications "
                 "are reviewed quickly.",
         needs=["Valid TIG welding certification with supporting documentation",
                "Willingness to travel and work on site across several countries",
                "Experience with pipe and steel structure welding",
                "Working level of English (B1 or better)"]),
]

DISCIPLINES = [
    "Welding (TIG)", "Welding (MIG/MAG)", "Pipe fitting", "Instrument pipe fitting",
    "Mechanical installation", "Shipbuilding", "Ship repair", "NDT inspection",
    "Rope access", "Quality control (QA/QC)", "Rigging", "Site supervision",
]
CERTIFICATES = [
    "EN ISO 9606 (welder)", "TIG 141", "MIG/MAG 131/135", "IRATA L1", "IRATA L2",
    "IRATA L3", "VCA / SCC", "NDT VT", "NDT PT/MT", "NDT UT", "GWO",
    "Medical certificate",
]
ROTATIONS = ["4 / 2", "3 / 3", "2 / 2", "6 / 2", "Continuous", "Local, no rotation"]
WORK_COUNTRIES = ["Norway", "Germany", "Netherlands", "United Kingdom",
                  "Lithuania", "Denmark", "Belgium", "Poland"]
EXPERIENCE = ["Less than 2 years", "2 to 5 years", "5 to 10 years", "More than 10 years"]


def chips(items, attr, cls="chip"):
    """A row of toggle buttons.

    aria-pressed rather than a class alone: to a screen reader a <button> that
    has silently changed class is a button that did nothing.
    """
    return "\n".join(
        '            <button type="button" class="%s" %s="%s" aria-pressed="false">%s</button>'
        % (cls, attr, _html.escape(v, quote=True), _html.escape(v))
        for v in items)


def spec_rows(p):
    """The job card's spec column.

    A row whose value is unknown is left out rather than printed as "to be
    confirmed". The client's mock had four of them in a column of six, and a
    card that answers nothing a rotation worker asks is worse than a shorter
    one. Fill the value in POSITIONS and the row appears.
    """
    rows = [("Positions", p.get("count")), ("Location", p.get("location")),
            ("Rotation", p.get("rotation")), ("Start", p.get("start")),
            ("Contract", p.get("contract")), ("Rate", p.get("rate"))]
    out = []
    for label, val in rows:
        if not val:
            continue
        out.append('          <div class="spec"><span>%s</span><b>%s</b></div>'
                   % (label, val))
    return "\n".join(out)


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
        d["needs"] = "\n".join("            <li>%s</li>" % n for n in p["needs"])
        d["specs"] = spec_rows(p)
        out.append("""      <article class="position" id="{id}">
        <div class="position-main">
          <p class="position-badge">Hiring now</p>
          <h3>{title}</h3>
          <p class="position-lead">{summary}</p>
          <p class="position-label">What we need</p>
          <ul class="position-needs">
{needs}
          </ul>
          <p><a class="btn-solid" href="#apply" data-apply="{title}">Apply for this role</a></p>
        </div>
        <div class="position-specs">
{specs}
        </div>
      </article>""".format(**d))
    return "\n".join(out)


def position_options():
    opts = ['<option value="Open application">Open application</option>']
    for p in POSITIONS:
        if p.get("open"):
            opts.append('<option value="%s">%s</option>' % (p["title"], p["title"]))
    return "\n                ".join(opts)


def _opts(items, placeholder):
    out = ['<option value="">%s</option>' % placeholder]
    out += ['<option>%s</option>' % _html.escape(v) for v in items]
    return "\n                ".join(out)


CAREERS = """
    <div class="container page-head">
      <p class="eyebrow">Careers</p>
      <h1 class="page-title">Work with ALPROJECTS</h1>
      <p class="page-lead">We deliver mechanical contracting, welding, inspection and access
      services on industrial and offshore projects across Europe. The work is technical,
      certified and mostly on site.</p>
      <div class="kpis">
        <div class="kpi"><b>30</b><span>Positions to fill</span></div>
        <div class="kpi"><b>6</b><span>Countries</span></div>
        <div class="kpi"><b>3</b><span>Working days to reply</span></div>
        <div class="kpi"><b>300</b><span>Specialists on our roster</span></div>
      </div>
    </div>

    <section class="container careers-block">
      <h2 class="eyebrow">Open position</h2>
""" + positions_html() + """
    </section>

    <section class="container careers-block">
      <h2 class="eyebrow">We recruit regularly in these disciplines</h2>
      <p class="careers-intro">Even when a role is not advertised we keep qualified
      specialists on file and make contact when a project matches. Select your discipline
      and it goes straight into the form below.</p>
      <div class="chips" id="discChips">
""" + chips(DISCIPLINES, "data-discipline") + """
      </div>
    </section>

    <div class="container" id="apply">
      <div class="apply-panel">
        <div class="apply-intro">
          <p class="eyebrow">Apply</p>
          <h2>Send us your details</h2>
          <p>Six fields are required. Everything else helps us match you faster, but
          the form will send without them.</p>
          <p>We read every application and reply within three working days when a project
          matches your profile.</p>
          <div class="apply-alt">
            <p class="eyebrow">Prefer not to fill in a form?</p>
            <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp +370 636 63 744</a>
            <a href="mailto:info@alprojects.eu?subject=Application">info@alprojects.eu</a>
            <a href="tel:+37063663744">Call +370 636 63 744</a>
          </div>
        </div>

        <form id="applyForm" class="apply-form" novalidate>
          <fieldset class="step">
            <legend><span class="step-n">01</span> Who you are</legend>
            <div class="field">
              <label for="apName">Full name</label>
              <input id="apName" name="name" type="text" required aria-required="true"
                     autocomplete="name" placeholder="Name and surname">
            </div>
            <div class="field">
              <label for="apEmail">Email</label>
              <input id="apEmail" name="email" type="email" required aria-required="true"
                     autocomplete="email" placeholder="name@email.com">
            </div>
            <div class="field">
              <label for="apPhone">Phone or WhatsApp</label>
              <input id="apPhone" name="phone" type="tel" required aria-required="true"
                     autocomplete="tel" placeholder="+370 ...">
            </div>
            <div class="field">
              <label for="apCountry">Country of residence <span class="opt">(optional)</span></label>
              <input id="apCountry" name="country" type="text" autocomplete="country-name"
                     placeholder="Lithuania">
            </div>
          </fieldset>

          <fieldset class="step">
            <legend><span class="step-n">02</span> Your trade</legend>
            <div class="field">
              <label for="apRole">Discipline</label>
              <select id="apRole" name="role" required aria-required="true">
                """ + _opts(DISCIPLINES + ["Other"], "Select your discipline") + """
              </select>
            </div>
            <div class="field">
              <label for="apYears">Years of experience <span class="opt">(optional)</span></label>
              <select id="apYears" name="years">
                """ + _opts(EXPERIENCE, "Select") + """
              </select>
            </div>
            <div class="field field-wide">
              <span class="label" id="certLabel">Certificates you hold
                <span class="opt">(optional, select all that apply)</span></span>
              <div class="chips chips-sm" id="certChips" role="group" aria-labelledby="certLabel">
""" + chips(CERTIFICATES, "data-cert", "chip chip-sm") + """
              </div>
              <p class="hint">Not on the list? Add it in the notes field below.</p>
            </div>
          </fieldset>

          <fieldset class="step">
            <legend><span class="step-n">03</span> Availability</legend>
            <div class="field">
              <label for="apFrom">Available from</label>
              <input id="apFrom" name="available" type="date" required aria-required="true">
            </div>
            <div class="field">
              <span class="label" id="rotLabel">Preferred rotation
                <span class="opt">(optional)</span></span>
              <div class="chips chips-sm" id="rotChips" role="group" aria-labelledby="rotLabel">
""" + chips(ROTATIONS, "data-rotation", "chip chip-sm") + """
              </div>
            </div>
            <div class="field field-wide">
              <span class="label" id="ctryLabel">Countries you can work in
                <span class="opt">(optional)</span></span>
              <div class="chips chips-sm" id="ctryChips" role="group" aria-labelledby="ctryLabel">
""" + chips(WORK_COUNTRIES, "data-country", "chip chip-sm") + """
              </div>
            </div>
            <div class="field field-wide">
              <label for="apMsg">Anything else <span class="opt">(optional)</span></label>
              <textarea id="apMsg" name="message" rows="4"
                        placeholder="Certificate numbers and expiry dates, projects you have worked on, when you could start."></textarea>
            </div>
          </fieldset>

          <fieldset class="step" id="docsStep">
            <legend><span class="step-n">04</span> Your documents</legend>
            <!-- The drop zone is always here. What happens to the files depends on
                 CAREERS_ENDPOINT: with one set they are uploaded with the form;
                 without one js/main.js names them in the email it opens, so the
                 applicant knows exactly what to attach. It never accepts a file
                 and then quietly loses it. -->
            <!-- A real <input> with a <label for> pointing at it, not a button
                 calling input.click(). The scripted click opens the picker in
                 Chrome and in headless WebKit but is at the mercy of each
                 browser's user-gesture rules; a label is how the platform does
                 it, needs no JavaScript at all, and cannot be blocked.

                 The input comes first so the label can be styled from its
                 focus state with a sibling selector -- it is visually hidden
                 but still focusable, so the drop zone shows a focus ring when
                 tabbed to. -->
            <input type="file" id="apFiles" name="files" multiple class="sr-file"
                   accept=".pdf,.jpg,.jpeg,.png,application/pdf,image/jpeg,image/png">
            <label class="drop" id="dropZone" for="apFiles">
              <b>Attach your CV and certificates</b>
              <span>Choose files, or drag them here. PDF, JPG or PNG, up to 10 MB each.</span>
            </label>
            <ul class="files" id="fileList"></ul>
            <p class="hint">Photographs of certificates taken with a phone are fine.</p>
            <p class="hint" id="docsAlt">You can also send them to
            <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a>
            or by <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.</p>
          </fieldset>

          <div class="field field-wide field-check">
            <input id="apConsent" name="consent" type="checkbox" required aria-required="true">
            <label for="apConsent">I agree that ALPROJECTS, UAB stores my details and
            documents for recruitment purposes for 24 months. I can ask for them to be
            deleted at any time by writing to info@alprojects.eu. See the
            <a href="/privacy.html">privacy policy</a>.</label>
          </div>
          <!-- Spam trap: a real applicant never sees this, a bot fills it in. -->
          <div class="hp" aria-hidden="true">
            <label for="apCompany">Company</label>
            <input id="apCompany" name="company" type="text" tabindex="-1" autocomplete="off">
          </div>
          <div class="field field-wide">
            <button type="submit" class="btn-solid">Send application</button>
            <p class="form-note" id="applyNote" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>
    </div>
"""

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
         date="13 Aug 2026", iso="2026-08-13", cat="Quality Control",
         img="projects/welding-tig-pipe-1200.webp", w=900, h=1200,
         alt="TIG root pass being welded on a prefabricated pipe spool",
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
         date="08 Aug 2026", iso="2026-08-08", cat="Shipbuilding",
         img="projects/sector-shipbuilding-1200.webp", w=1200, h=1017,
         alt="Fitters working inside a hull block under construction",
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
         date="23 Jun 2026", iso="2026-06-23", cat="Company",
         img="projects/engineer-drawings-1200.webp", w=1200, h=954,
         alt="ALPROJECTS engineer working from isometric drawings on site",
         title="Among the strongest companies in Lithuania",
         seo="Among Lithuania's strongest companies",
         lead="ALPROJECTS, UAB has been awarded the Strongest in Lithuania 2025\u20132026 certificate by Creditinfo Group.",
         body=[
           "The certificate recognises companies with a high credit score and a proven record of financial stability. It is issued by Creditinfo Group and was awarded on 23 June 2026 for the 2025\u20132026 period.",
           "<strong>A stable partner is a safer project.</strong> In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through.",
           "That matters more than a logo on a wall. It is the difference between a contractor who can carry a scope to completion and one who cannot.",
         ],
         facts=[("Award", "Strongest in Lithuania", "2025\u20132026"),
                ("Issued by", "Creditinfo Group", "23 June 2026")],
         cta="Planning a project across shipbuilding, piping or industrial services? Let us talk."),

    dict(slug="transformer-mechanical-package",
         date="01 Aug 2026", iso="2026-08-01", cat="Industrial Projects",
         img="projects/transformer-overhead-1200.webp", w=1200, h=900,
         alt="Stainless pipework and transformer package installed at a substation",
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
         date="25 Jul 2026", iso="2026-07-25", cat="Energy Projects",
         img="projects/terminal-rack-tanks-1200.webp", w=1200, h=900,
         alt="Completed pipe rack running to storage tanks at a fuel loading terminal",
         title="Fuel loading terminal completed",
         lead="September 2025 to April 2026. Twelve specialists. Over 11,000 hours on site.",
         body=[
           "The scope ran from September 2025 to April 2026 and was delivered by a team of 12 specialists, accumulating more than 11,000 hours on site.",
           "Fuel handling infrastructure concentrates every discipline we work in \u2014 mechanical installation, pipe fitting, welding, and the inspection and documentation that has to accompany all three when the medium is flammable.",
           "Numbers like 11,000 hours are worth stating plainly: they are what a project of this size actually costs in skilled labour, and planning against a lower figure is how schedules fail.",
         ],
         facts=[], cta="Send us the scope and we will come back with a price and crew dates."),

    dict(slug="europe-tig-welder-shortage",
         date="25 Jul 2026", iso="2026-07-25", cat="Industry",
         img="projects/sector-industry-1200.webp", w=1200, h=1017,
         alt="TIG welder working on a large-diameter stainless pipe",
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

# Newest first, and the number comes from that order rather than being typed in.
# The list was hand-ordered and hand-numbered, which put the June award third --
# between 08 August and 01 August -- and meant a seventh article would have
# renumbered every page that already carries its number in its own body.
ARTICLES.sort(key=lambda a: a["iso"], reverse=True)
for _i, _a in enumerate(ARTICLES, 1):
    _a["num"] = "%02d" % _i

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
          <span class="thumb"><img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="{loading}"{prio}><span class="corners" aria-hidden="true"><i></i><i></i><i></i><i></i></span></span>
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
    <section class="sector-hero co-hero">
      <img class="sector-hero-img" src="/assets/tia-hero.webp" alt="ALPROJECTS crew on a wind farm site"
           width="1900" height="814" fetchpriority="high" decoding="async">
      <span class="sector-hero-scrim" aria-hidden="true"></span>
      <div class="container sector-hero-in">
        <p class="eyebrow">Company</p>
        <h1 class="sector-hero-title">This is ALPROJECTS</h1>
        <p class="sector-hero-lead">What we are here to do, and the rules we work by. Written
        down so a client can hold us to them.</p>
      </div>
    </section>

    <!-- ================= VISION / MISSION ================= -->
    <div class="container">
      <div class="co-vm">
        <div class="reveal">
          <p class="eyebrow">Our vision</p>
          <p class="co-big">Industrial work that comes with its own evidence.</p>
          <p class="co-body">Europe has no shortage of contractors who can weld. It has a
          shortage of contractors who can hand over the evidence with the work, in a form the
          client, the surveyor and the auditor all accept.</p>
        </div>
        <div class="reveal reveal-d1">
          <p class="eyebrow">Our mission</p>
          <p class="co-big">Certified people on site, and independent proof of what they did.</p>
          <p class="co-body">We take mechanical scopes and deliver them with our own
          supervision. We supply the qualified people a project is short of. And we inspect the
          result with people who did not do the work.</p>
        </div>
      </div>
    </div>

    <!-- ================= WHAT WE DO ================= -->
    <div class="container co-sec">
      <p class="eyebrow">What we do</p>
      <div class="co-intro">
        <h2 class="sub-head co-vhead reveal">We deliver the scope, or we supply the people a
        scope is short of</h2>
        <p class="co-body reveal">Often both, on the same site. We specialise in piping
        prefabrication and installation, steel fabrication and mechanical installation, and we
        provide certified technical personnel to projects across Europe.</p>
      </div>
      <ul class="co-rows reveal">
        <li>
          <a href="/sectors/shipbuilding.html">
            <b>Shipbuilding</b>
            <span>Piping and mechanical installation on vessels under construction.</span>
            <em aria-hidden="true">&rarr;</em>
          </a>
        </li>
        <li>
          <a href="/sectors/offshore.html">
            <b>Offshore</b>
            <span>Inspection, access and mechanical works on offshore facilities.</span>
            <em aria-hidden="true">&rarr;</em>
          </a>
        </li>
        <li>
          <a href="/sectors/industrial.html">
            <b>Industrial</b>
            <span>Plant installation, transformer packages, process piping.</span>
            <em aria-hidden="true">&rarr;</em>
          </a>
        </li>
        <li>
          <a href="/sectors/renewables.html">
            <b>Energy and renewables</b>
            <span>Fuel handling infrastructure and wind energy support.</span>
            <em aria-hidden="true">&rarr;</em>
          </a>
        </li>
      </ul>
    </div>

    <!-- ================= PEOPLE ================= -->
    <div class="container co-sec">
      <p class="eyebrow">Our people</p>
      <div class="co-people">
        <div class="reveal">
          <h2 class="sub-head">Three hundred specialists, and a schedule that does not wait</h2>
          <p class="co-body">Welders, pipe fitters, shipbuilders, mechanics, NDT inspectors and
          rope access technicians. Most carry a second trade, which is why one of our people
          often covers what usually takes two.</p>
          <p class="co-body">They travel. A crew that mobilises to Norway on Monday can be in
          Rostock the following month. That is the job, and everyone who joins us knows it
          before the first rotation.</p>
          <p class="co-note">We keep the roster current. Certificates, medicals and
          availability are checked before anyone is offered to a project.</p>
          <p class="back">
            <a class="btn-solid" href="/careers.html">Work with us</a>
            <!-- Filled in from MANAGEMENT_URL in js/main.js. Removed while that is
                 empty, so a page that does not exist yet never ships as a dead link. -->
            <a class="btn-bracket" data-management hidden href="#">Meet the management</a>
          </p>
        </div>
        <figure class="co-people-img reveal reveal-d1">
          <img src="/assets/tia-people.webp" alt="Rope access technician working on a turbine blade"
               width="860" height="645" loading="lazy" decoding="async">
        </figure>
      </div>
      <div class="co-figs reveal">
        <div><span class="value" data-count="300" data-suffix="+">300+</span> <span class="label">Certified specialists on the roster</span></div>
        <div><span class="value" data-count="6">6</span> <span class="label">Countries we work in</span></div>
        <div><span class="value" data-count="4">4</span> <span class="label">Sectors, one set of disciplines</span></div>
        <div><span class="value" data-count="3">3</span> <span class="label">ISO management systems, certified by DNV</span></div>
      </div>
    </div>

    <!-- ================= VALUES ================= -->
    <div class="container co-sec">
      <p class="eyebrow">Our values</p>
      <h2 class="sub-head co-vhead reveal">Values are worth writing down only if someone can
      hold you to them. Ours are written so a client can.</h2>
      <div class="co-vals">
        <div class="co-val reveal">
          <span class="co-val-n">01</span>
          <div>
            <h3>We keep learning on every job</h3>
            <ul class="co-val-list">
            <li>We debrief after each mobilisation and write down what we would do differently.</li>
            <li>We share procedures between crews, so the second job runs faster than the first.</li>
            <li>We ask the client&rsquo;s supervisor what went wrong before they have to tell us.</li>
            <li>We bring people up to a second trade, because two skills in one person are worth more offshore.</li>
            </ul>
          </div>
        </div>
        <div class="co-val reveal">
          <span class="co-val-n">02</span>
          <div>
            <h3>We are responsible for the scope</h3>
            <ul class="co-val-list">
            <li>We take the work with our own supervision and our own quality control.</li>
            <li>When the mistake is ours, we say so and we correct it at our cost.</li>
            <li>We never hand a problem down to the next contractor in the chain.</li>
            <li>We get everyone home at the end of the rotation.</li>
            </ul>
          </div>
        </div>
        <div class="co-val reveal">
          <span class="co-val-n">03</span>
          <div>
            <h3>We look for the work others avoid</h3>
            <ul class="co-val-list">
            <li>We take scopes with difficult access, tight windows and unclear starting conditions.</li>
            <li>We answer enquiries that arrive at short notice, because that is when a client needs a contractor most.</li>
            <li>We invest in certification before the market starts asking for it.</li>
            <li>We build the business together, across offices and across crews.</li>
            </ul>
          </div>
        </div>
        <div class="co-val reveal">
          <span class="co-val-n">04</span>
          <div>
            <h3>We look after people and the site</h3>
            <ul class="co-val-list">
            <li>We work to the client&rsquo;s permit system and add our own where theirs is thinner.</li>
            <li>We leave the area cleaner than we found it.</li>
            <li>We ask for help early. Nobody on a rope is expected to manage alone.</li>
            <li>We follow the law and our own procedures when nobody is watching.</li>
            </ul>
          </div>
        </div>
        <div class="co-val reveal">
          <span class="co-val-n">05</span>
          <div>
            <h3>We keep the date we gave</h3>
            <ul class="co-val-list">
            <li>A mobilisation date is given only when the people are actually free.</li>
            <li>We plan so that the safe method is also the fast one.</li>
            <li>We remind the client of their deadlines as well as ours.</li>
            <li>A yard schedule does not move, so ours has to hold.</li>
            </ul>
          </div>
        </div>
        <div class="co-val reveal">
          <span class="co-val-n">06</span>
          <div>
            <h3>We say it early and we say it plainly</h3>
            <ul class="co-val-list">
            <li>We explain the scope and the risks before the work starts.</li>
            <li>A problem is reported the day it appears. Friday is too late.</li>
            <li>We confirm that we understood the client, and that he understood us.</li>
            <li>We write documentation a person can actually read.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= QUOTE BAND ================= -->
    <section class="co-band">
      <img src="/assets/tia-band.webp" alt="Rope access descent onto an offshore topside"
           width="1700" height="566" loading="lazy" decoding="async">
      <span class="co-band-scrim" aria-hidden="true"></span>
      <div class="container co-band-in">
        <blockquote>Anyone on our crew can stop a job.</blockquote>
        <cite>ALPROJECTS Group &middot; Value 02</cite>
      </div>
    </section>

    <!-- ================= HSEQ ================= -->
    <div class="container co-sec">
      <p class="eyebrow">HSEQ</p>
      <div class="co-hseq">
        <div class="reveal">
          <h2 class="sub-head">Zero harm is a target, and we report against it</h2>
          <p class="co-body">We work inside the client&rsquo;s permit system and add our own
          where theirs is thinner. Every scope gets a risk assessment and a method statement
          before mobilisation, and both are written for the actual site. Copying the paperwork
          from the last job is how people get hurt.</p>
          <p class="co-note">Our management systems are certified to ISO 9001, 14001 and
          45001, and our welding to ISO 3834. Certification is what lets a client accept our
          documentation without repeating the inspection.</p>
        </div>
      </div>
      <div class="co-zeros reveal">
        <div class="co-zero"><b>No injuries</b><span>to our people, to the client&rsquo;s people, or to anyone else on site.</span></div>
        <div class="co-zero"><b>No occupational illness</b><span>from the way we organise the work.</span></div>
        <div class="co-zero"><b>No spills</b><span>to the sea, to the ground or to the drain.</span></div>
        <div class="co-zero"><b>No damage</b><span>to the structure we were sent to work on.</span></div>
      </div>
      <p class="co-note co-zeros-note">We track hours worked, incidents and what we changed as a result, and we
      share the figures with clients on request. A target nobody measures is a
      slogan.</p>
      <div class="co-plates reveal">
        <div class="co-plate"><b>ISO 3834</b><span>Welding quality</span></div>
        <div class="co-plate"><b>ISO 9001</b><span>Quality</span></div>
        <div class="co-plate"><b>ISO 14001</b><span>Environment</span></div>
        <div class="co-plate"><b>ISO 45001</b><span>Health and safety</span></div>
      </div>
    </div>

    <!-- ================= STANDING ================= -->
    <div class="container co-sec">
      <p class="eyebrow">Standing</p>
      <div class="co-vm">
        <div class="reveal">
          <p class="co-big">Where we work from</p>
          <p class="co-body">Head office in Klaipėda, Lithuania, with project bases in
          <strong>six countries</strong>, serving offshore, shipbuilding
          and industry across Northern and Western Europe.</p>
          <p class="co-note">We draw on a roster of more than 300 certified specialists. Projects are resourced from that
          roster rather than subcontracted on, which is what keeps the quality system
          meaningful.</p>
        </div>
        <div class="reveal reveal-d1">
          <p class="co-big">Strongest in Lithuania, 2025&ndash;2026</p>
          <p class="co-body">ALPROJECTS, UAB holds the <strong>Strongest in
          Lithuania</strong> certificate, awarded by Creditinfo Group on 23 June 2026 to
          companies with a high credit score and a proven record of financial stability.</p>
          <p class="co-body">In heavy industry, projects run for months and commitments run for
          years. Independent proof of financial stability is proof that we will be there to see
          the work through &mdash; a different question from whether the welding is any good,
          and worth answering separately.</p>
          <p class="back">
            <a class="btn-bracket" href="/news/strongest-in-lithuania-2025-2026.html">More on the award</a>
          </p>
        </div>
      </div>
    </div>

    <!-- ================= CTA ================= -->
    <div class="container">
      <div class="co-cta">
        <div>
          <h2 class="sub-head reveal">If this is how you want your contractor to work, send us the scope</h2>
          <p class="co-note">We aim to reply to project enquiries within one working day.</p>
        </div>
        <div class="co-cta-act">
          <p class="co-addr">ALPROJECTS, UAB<br>Šilutės pl. 2-536, LT-91110 Klaipėda, Lithuania<br>
          <a href="mailto:info@alprojects.eu">info@alprojects.eu</a><br>
          <a href="tel:+37063663744">+370 636 63 744</a></p>
          <p class="back">
            <a class="btn-solid" href="/contacts.html#enquiry">Send us the scope</a>
            <a class="btn-bracket" href="/services.html">Our services</a>
            <a class="btn-bracket" href="/projects.html">See our projects</a>
          </p>
        </div>
      </div>
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

SHOTS = [
    ("welding-tig-pipe", 'TIG root pass on a prefabricated spool', 900, 1200),
    ("piping-roof-crew", 'Carbon steel lines being set out on a plant roof', 900, 1200),
    ("piping-roof-duct", 'Process lines run alongside insulated ductwork', 900, 1200),
    ("transformer-overhead", 'Stainless pipework around a transformer package', 1200, 900),
    ("substation-sky", 'Completed pipe runs at a substation', 1200, 900),
    ("facade-pipe-crane", 'Pipe runs erected along a plant facade', 900, 1200),
    ("transformer-bushing", 'Mechanical package installed beneath the bushings', 1200, 900),
    ("transformer-plant", 'Cooling and process lines at the transformer plant', 1200, 900),
    ("facade-tank-pipe", 'Vessel and pipe run carried along the building line', 1200, 900),
    ("terminal-rack-tanks", 'Pipe rack running to storage tanks at a fuel terminal', 1200, 900),
    ("terminal-pumps", 'Pump skids and valve stations, terminal loading area', 900, 1200),
    ("terminal-rack-trays", 'Pipe rack and cable trays on the loading gantry', 900, 1200),
    ("terminal-valves", 'Valve manifolds over the bund', 1200, 900),
    ("terminal-tankfarm", 'Completed tank farm pipe racks', 900, 1200),
]


def shots_html():
    """The site gallery.

    Every image keeps its own aspect ratio. They were all forced into a
    300px-tall landscape box before, and seven of the fourteen are 900x1200 --
    a portrait of a welder cropped to 45% of its frame, which is most of the
    subject. The layout is CSS columns rather than a row grid, so a tall
    photograph simply takes more column and nothing is cut.
    """
    out = []
    for n, (slug, alt, w, h) in enumerate(SHOTS, 1):
        tall = " shot-tall" if int(h) > int(w) else ""
        a = _html.escape(alt, quote=True)
        out.append(
            '        <figure class="shot%s">\n'
            '          <button type="button" class="shot-open" data-shot="%d">\n'
            '            <img src="/assets/projects/%s-1200.webp"\n'
            '                 srcset="/assets/projects/%s-600.webp 600w, /assets/projects/%s-1200.webp 1200w"\n'
            '                 sizes="(max-width: 700px) 92vw, (max-width: 1100px) 46vw, 31vw"\n'
            '                 alt="%s" width="%s" height="%s" loading="lazy" decoding="async">\n'
            '            <span class="corners" aria-hidden="true"><i></i><i></i><i></i><i></i></span>\n'
            '          </button>\n'
            '          <figcaption>%s</figcaption>\n'
            '        </figure>' % (tall, n, slug, slug, slug, a, w, h, _html.escape(alt)))
    return "\n".join(out)



# ============================================================
# PROJECT CASES
# ============================================================
# Four scopes the client photographed and wrote up. Everything here is his
# copy; nothing about a client, a site or a date is stated, because none of it
# was supplied and most offshore frame agreements forbid naming the customer
# anyway. The retoucher took the tag numbers and one customer logo off the
# frames before they were handed over -- see the notes in the drop folder.
#
# The page is a plate sequence, the way a job report is: each stage carries the
# paragraph that describes it and the one photograph that shows it. The pairing
# is written out per stage rather than zipped by position, because the client's
# paragraphs and his frame order do not run in step -- his fourth paragraph is
# about the clips coming off, and the frame that shows the clips is his fourth
# but his second paragraph's frame is his third.
#
# `photos[0]` is always the hero. Every other frame is used by exactly one
# stage, in ascending order, which is what keeps the lightbox sequence equal to
# the photo order -- the viewer numbers shots by DOM position, not by the
# data-shot attribute.
CASES = [
    dict(
        slug="tank-and-vessel-fabrication",
        title="Tank and vessel fabrication",
        kicker="Shop fabrication and welding",
        setting="Fabrication shop, under a crane",
        lead="We weld the nozzles into the courses before they go on the stack, weld out "
             "the seams under a crane, and cut and fit the bottoms on the shop floor.",
        intro=[],
        stages=[
            (2, ["Nozzles and manways go into the shell courses before they go on the "
                 "stack, while a course can still be worked from both sides. The welder "
                 "works downhand and can get at the back of the joint. By the time a "
                 "course goes on the stack the nozzles are already in it."]),
            (3, ["The first course goes on timber packing. The next comes down on it "
                 "under the crane, landed and held while the seam is tacked, and then "
                 "welded out."]),
            (4, ["The large tanks go together the other way up. The shell is held up on "
                 "packing and the next course goes on underneath it, with a row of "
                 "temporary clips round the inside holding it while the seams are welded "
                 "out.",
                 "Those clips and the lifting lugs come off when the shell is done, and "
                 "the places where they were welded are dressed back level with the "
                 "plate."]),
            (5, ["Lifting is done on the overhead crane, using slings and a spreader "
                 "beam. Bottom plates are cut and fitted on the shop floor."]),
            (6, ["In the shop the welding is done under cover and under a crane."]),
        ],
        note="",
        cta="Send us the drawings.",
        services=["welding-services", "pipe-fitting", "mechanical-contracting",
                  "quality-control"],
        photos=[
            ("Welder working under a tank shell held up and secured on timber packing, "
             "with bottom plates laid out on the shop floor",
             "Shell held up on packing, work going on underneath.", 1200, 1600),
            ("Vessel shell course being lowered onto the course below by overhead crane, "
             "with the nozzles already welded in",
             "The nozzles go in before the course goes on the stack.", 1200, 1600),
            ("Assembled vessel standing on blocks, with nozzles, a side manway and a "
             "drawing taped to the shell",
             "Vessel closed up.", 1200, 1600),
            ("Inside a tank shell, a long pipe on trestles and temporary clips welded "
             "round the courses above the bottom plates",
             "Inside the shell, with the temporary clips round the courses.", 1200, 1600),
            ("Tank shell lifted on slings from lugs welded to the top course",
             "Lifted on slings from welded lugs.", 1200, 1600),
            ("Fabrication hall with tank shells, a vessel on packing, and a spreader beam "
             "with slings on the floor",
             "The shop floor.", 1200, 900),
        ]),
    dict(
        slug="valve-station-tie-in-piping",
        title="Valve station and tie-in piping",
        kicker="Mechanical installation and welding &middot; tank farm",
        setting="Live plant, work front under cover",
        lead="A new valve station at the base of a storage tank. We set and levelled the "
             "valves, fitted the spools, welded and bolted the joints, and tied the run "
             "into the existing pipe rack.",
        # Two of the five delivered frames are not here. The customer's logo is
        # legible on the tarpaulin in both -- the retoucher cleaned three frames
        # and these two were missed -- so they are out of the repo entirely
        # until they come back cleaned. See README, "Still open on the case
        # pages". The three that remain carry no customer identification: the
        # "TENARIS" on the pipe in the tie-in frame is the mill's mark, which
        # the client asked to keep.
        intro=["A storage tank needed a new valve station and a connection into the "
               "existing pipe rack.",
               "The valves went on adjustable stands and we levelled them before "
               "anything was fixed. We did not tack until the run was straight and the "
               "flange faces were parallel."],
        stages=[
            (2, ["The close-up shows a finished root, taken down the bore from the open "
                 "end of a spool."]),
            (3, ["Some of the joints are welded, the rest are flanged and bolted. The "
                 "spools went in between them."]),
        ],
        note="The work front sat under temporary cover, with the plant live around it.",
        cta="Send us the scope.",
        services=["pipe-fitting", "welding-services", "mechanical-contracting",
                  "quality-control"],
        photos=[
            ("Valve station under temporary cover at the base of a storage tank",
             "Work front under temporary cover.", 1200, 1600),
            ("Finished root run on a butt weld, photographed down the pipe bore from the "
             "open end of a spool",
             "Finished root.", 1200, 900),
            ("Tie-in piping and flanged joints running from the valve station into the "
             "existing rack",
             "Tied into the existing rack.", 1200, 1600),
        ]),
    dict(
        slug="tank-internals-and-attachments",
        title="Tank internals, nozzles and attachments",
        kicker="Mechanical installation and welding",
        setting="Tank being fitted out",
        lead="Internal pipe off a shell nozzle, brackets on pad plates, roof rafters into "
             "the centre ring.",
        # The hero frame IS the close-up this paragraph points at, so it reads as
        # the lead-in to the sequence rather than as a stage of its own.
        intro=["On this job no bracket went straight onto the shell. Every attachment sat "
               "on a pad plate, and the pad was welded to the shell. The close-up above "
               "shows one. If the bracket ever has to come off, it comes off the pad and "
               "the shell is untouched."],
        stages=[
            (2, ["The internal pipe runs from a shell nozzle across the tank.",
                 "Pads went down on the bottom plates as well, the stands went on the "
                 "pads and the pipe sat on the stands. When the stands come off, the pads "
                 "take the damage instead of the bottom plates."]),
            (3, ["The roof goes on radial rafters into a centre ring."]),
        ],
        note="Temporary steel goes on and comes off all the way through a job like this. "
             "Every place it was welded is ground back flush before the tank is painted.",
        cta="Tell us what goes inside and we will price it.",
        services=["welding-services", "mechanical-contracting", "pipe-fitting",
                  "quality-control"],
        photos=[
            ("External bracket welded to a pad plate on the tank shell, with the pad "
             "welded all round",
             "The pad plate goes on before the bracket.", 1200, 1600),
            ("Internal pipe connected to a shell nozzle inside a tank, with bottom plates "
             "below",
             "Internal pipe off the shell nozzle.", 1200, 1600),
            ("Tank roof on radial rafters into the centre ring, with a nozzle opening cut",
             "Roof rafters into the centre ring.", 1200, 900),
        ]),
    dict(
        slug="agitator-replacement",
        title="Agitator replacement inside a storage tank",
        kicker="Mechanical installation",
        setting="Tank out of service",
        lead="The shaft runs from the drive mounting on the roof down to a bearing at the "
             "floor, with two impellers on it.",
        intro=["The agitator in this tank was being replaced. The shaft runs the full "
               "height of the tank, from the drive mounting on the roof down to a bearing "
               "at the floor. Two impellers on it, one low down and one near the roof.",
               "The fitting work was done inside the tank, with the tank out of service."],
        stages=[
            (2, ["The bearing at the floor went in first. We levelled it before any of the "
                 "shaft went in, and checked the shaft once it was down. Everything above "
                 "depends on that bearing."]),
            (3, ["We fitted the lower impeller from the tank floor and the upper one from "
                 "temporary access."]),
        ],
        note="",
        cta="Tell us what is going in and we will look at it.",
        services=["mechanical-contracting", "rigging-technical-support", "pipe-fitting",
                  "quality-control"],
        photos=[
            ("Agitator shaft running the full height of a storage tank up to the roof, "
             "with the upper impeller near the top",
             "Looking up the shaft to the roof.", 1200, 900),
            ("Agitator bearing at the tank floor, with levelling tools in place",
             "The bearing at the floor.", 1200, 1600),
            ("Lower agitator impeller bolted to the shaft inside a storage tank, with the "
             "bearing on the floor below it",
             "Lower impeller on the shaft.", 1200, 900),
        ]),
]

# Every frame has to appear exactly once, as the hero or as one stage's plate.
# Without this a re-ordered stage list silently drops a photograph -- the page
# still builds, the lightbox still works, and the frame is just gone.
for _c in CASES:
    _used = [n for n, _ in _c["stages"]]
    assert _used == sorted(_used), "%s: stages must run in photo order" % _c["slug"]
    assert _used == list(range(2, len(_c["photos"]) + 1)), \
        "%s: stages cover %s of %d frames" % (_c["slug"], _used, len(_c["photos"]))


def _plate(c, n, eager=False, sizes="(max-width: 900px) 92vw, 38vw"):
    """One numbered plate: the button the viewer picks up, its corner ticks and
    its caption. The number lives outside <figcaption> -- js/main.js reads the
    caption with textContent, so anything inside it is prefixed to the caption
    in the viewer.

    --ar carries the frame's own ratio so the button can be sized by height and
    still hug the photograph. object-fit then has nothing to crop, which is why
    the corner ticks sit on the image edge rather than on a letterboxed box."""
    alt, cap, w, h = c["photos"][n - 1]
    base = "/assets/projects/cases/%s/%02d" % (c["slug"], n)
    return (
        '          <figure class="plate%s" style="--ar:%d/%d">\n'
        '            <button type="button" class="shot-open" data-shot="%d">\n'
        '              <img src="%s-1200.webp"\n'
        '                   srcset="%s-600.webp 600w, %s-1200.webp 1200w"\n'
        '                   sizes="%s"\n'
        '                   alt="%s" width="%d" height="%d"\n'
        '                   loading="%s" decoding="async"%s>\n'
        '              <span class="corners" aria-hidden="true"><i></i><i></i><i></i><i></i></span>\n'
        '            </button>\n'
        '            <figcaption>%s</figcaption>\n'
        '          </figure>'
        % (" plate-tall" if h > w else "", w, h, n, base, base, base, sizes,
           _html.escape(alt, quote=True), w, h,
           "eager" if eager else "lazy",
           ' fetchpriority="high"' if eager else "",
           _html.escape(cap)))


def _sheet(dim, marks, where="tr"):
    """The drawing-sheet furniture from the homepage hero: the fine module, a
    few registration crosshairs and a dimension label. The label carries the
    frame's real pixel size rather than an invented number -- the drafting
    motif only works while it is telling the truth."""
    plus = "\n".join(
        '        <span class="sheet-plus" style="left:%s; top:%s" aria-hidden="true"></span>'
        % xy for xy in marks)
    return ('      <span class="sheet-grid" aria-hidden="true"></span>\n'
            '      <span class="sheet-furniture" aria-hidden="true">\n%s\n'
            '        <span class="sheet-dim sheet-dim-%s">%s</span>\n'
            '      </span>' % (plus, where, dim))


def _deck(c):
    """The stage sequence as the site's sticky card stack -- the same interaction
    the twelve service slides use on the homepage. Each card pins under the
    header and the next one rides up over it, so the photographs advance as you
    scroll instead of scrolling past.

    Card height is fixed rather than content-driven. A short card in a sticky
    stack does not fully cover the one beneath it, and the previous photograph
    peeks out along the bottom edge for the whole of the next card's travel."""
    n_total = len(c["stages"])
    out = []
    for i, (n, paras) in enumerate(c["stages"], 1):
        alt, cap, w, h = c["photos"][n - 1]
        pips = "".join('<i class="done"></i>' if k <= i else "<i></i>"
                       for k in range(1, n_total + 1))
        out.append(
            '      <article class="case-slide%(wide)s">\n'
            '%(sheet)s\n'
            '        <div class="slide-top">\n'
            '          <span class="slide-label">Stage</span>\n'
            '          <span class="slide-count">%(i)02d / %(tot)02d</span>\n'
            '        </div>\n'
            '        <div class="slide-body">\n'
            '          <div class="slide-txt">\n'
            '            <p class="slide-n" aria-hidden="true">%(i)02d</p>\n'
            '%(paras)s\n          </div>\n'
            '%(plate)s\n'
            '        </div>\n'
            '        <div class="slide-meta">\n'
            '          <div class="progress" aria-hidden="true">%(pips)s</div>\n'
            '        </div>\n'
            '      </article>'
            % dict(wide="" if h > w else " slide-wide",
                   sheet=_sheet("%dX%d" % (w, h),
                                (("9%", "14%"), ("31%", "6%"), ("31%", "30%")),
                                "tr"),
                   i=i, tot=n_total,
                   paras="\n".join("            <p>%s</p>" % p for p in paras),
                   plate=_plate(c, n, sizes="(max-width: 980px) 88vw, 40vw"),
                   pips=pips))
    return "\n".join(out)


def case_body(c, nxt):
    by_slug = {sv["slug"]: sv for sv in SERVICES_FLAT}
    links = "\n".join(
        '            <li><a href="/services/%s.html">%s</a></li>' % (s, by_slug[s]["nav"])
        for s in c["services"] if s in by_slug)
    _alt, _cap, _w, _h = c["photos"][0]

    intro = ""
    if c["intro"]:
        intro = ('    <div class="container case-intro">\n%s\n    </div>\n\n'
                 % "\n".join("      <p>%s</p>" % p for p in c["intro"]))
    note = ""
    if c["note"]:
        note = ('      <p class="case-note">%s</p>\n' % c["note"])

    return """
    <section class="case-hero%(tall)s">
%(hero_sheet)s
      <div class="container case-hero-in">
        <div class="case-hero-txt">
          <p class="eyebrow">Project &middot; %(kicker)s</p>
          <h1 class="case-title">%(title)s</h1>
          <p class="case-lead">%(lead)s</p>
        </div>
%(hero_plate)s
      </div>
    </section>

    <div class="container">
      <div class="fact-strip case-spec">
        <div class="fact">
          <p class="fact-label">Scope</p>
          <p class="fact-value">%(kicker)s</p>
        </div>
        <div class="fact">
          <p class="fact-label">Setting</p>
          <p class="fact-value">%(setting)s</p>
        </div>
        <div class="fact">
          <p class="fact-label">Plates</p>
          <p class="fact-value">%(n)d photographs</p>
        </div>
      </div>
    </div>

%(intro)s    <section class="case-seq">
      <div class="container seq-head">
        <h2 class="sub-head">How it was built</h2>
        <p class="sub-lead">One plate to a stage. Press a plate to open it full size.</p>
      </div>
      <div class="container case-deck">
%(stages)s
      </div>
    </section>

%(lightbox)s

    <section class="container case-close">
%(note)s      <div class="case-close-grid">
        <div>
          <p class="eyebrow">Disciplines on this job</p>
          <ul class="sector-services">
%(links)s
          </ul>
        </div>
        <div class="case-ask">
          <p class="case-ask-h">%(cta)s</p>
          <p>Send the drawings or the scope and we will come back with a price and crew
          dates. If it is a shutdown, tell us the window.</p>
          <p class="back">
            <a class="btn-solid" href="/contacts.html">Start a project</a>
          </p>
        </div>
      </div>
    </section>

    <nav class="container case-next" aria-label="More projects">
      <a class="case-next-link" href="/projects/%(nxt_slug)s.html">
        <span class="eyebrow">Next project</span>
        <span class="case-next-t">%(nxt_title)s</span>
        <span class="arr" aria-hidden="true">&#8599;</span>
      </a>
      <a class="case-next-link case-next-all" href="/projects.html">
        <span class="eyebrow">Index</span>
        <span class="case-next-t">All projects</span>
        <span class="arr" aria-hidden="true">&#8599;</span>
      </a>
    </nav>
""" % dict(tall=" case-hero-tall" if _h > _w else "",
           hero_sheet=_sheet("%dX%d" % (_w, _h),
                             # clear of the type block, which runs roughly
                             # x 5-50%, y 20-52%
                             (("53%", "20%"), ("41%", "72%"), ("15%", "82%"),
                              ("62%", "56%")), "bl"),
           kicker=c["kicker"],
           title=c["title"], lead=c["lead"], setting=c["setting"],
           hero_plate=_plate(c, 1, eager=True).replace('class="plate',
                                                       'class="case-fig plate'),
           n=len(c["photos"]), intro=intro, stages=_deck(c),
           lightbox=LIGHTBOX, note=note, links=links, cta=c["cta"],
           nxt_slug=nxt["slug"], nxt_title=_html.escape(nxt["title"]))


def cases_html():
    cards = []
    for i, c in enumerate(CASES):
        alt, _cap, w, h = c["photos"][0]
        cards.append(
            '        <a class="case-card" href="/projects/%s.html">\n'
            '          <span class="case-thumb">\n'
            '            <img src="/assets/projects/cases/%s/01-600.webp"\n'
            '                 alt="%s" width="%d" height="%d" loading="%s" decoding="async">\n'
            '            <span class="corners" aria-hidden="true"><i></i><i></i><i></i><i></i></span>\n'
            '          </span>\n'
            '          <span class="case-txt">\n'
            '            <span class="case-top">\n'
            '              <span class="case-num">%02d</span>\n'
            '              <span class="case-kicker">%s</span>\n'
            '            </span>\n'
            '            <h3>%s</h3>\n'
            '            <span class="case-blurb">%s</span>\n'
            '            <span class="case-more">Read the job <span class="arr">&#8599;</span></span>\n'
            '          </span>\n'
            '        </a>'
            % (c["slug"], c["slug"], _html.escape(alt, quote=True), w, h,
               "eager" if i < 2 else "lazy", i + 1, c["kicker"],
               _html.escape(c["title"]), c["lead"]))
    return "\n".join(cards)


# The gallery viewer, shared by /projects and every case page.
LIGHTBOX = """    <!-- The gallery viewer. Inert markup: js/main.js wires it, and with no
         JavaScript the thumbnails stay ordinary figures. -->
    <div class="lb" id="lightbox" hidden>
      <div class="lb-scrim" data-lb-close></div>
      <div class="lb-panel" role="dialog" aria-modal="true" aria-label="Project photograph">
        <figure class="lb-fig">
          <!-- no src= until a photograph is chosen: src="" makes some
               browsers re-request the page itself -->
          <img id="lbImage" alt="">
          <figcaption><span id="lbCaption"></span><span class="lb-count" id="lbCount"></span></figcaption>
        </figure>
        <button type="button" class="lb-btn lb-prev" id="lbPrev" aria-label="Previous photograph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 4 7 12l8 8" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </button>
        <button type="button" class="lb-btn lb-next" id="lbNext" aria-label="Next photograph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4l8 8-8 8" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </button>
        <button type="button" class="lb-btn lb-close" id="lbClose" aria-label="Close" data-lb-close>
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </button>
      </div>
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
      ran from September 2025 to April 2026 with 12 specialists and over 11,000 hours
      on site — a useful figure for anyone planning work of that size.</p>

    </div>

    <div class="container">
      <h2 class="sub-head">Recent work</h2>
      <p class="sub-lead">Four scopes, photographed as they were built.</p>
      <div class="case-grid">
""" + cases_html() + """
      </div>
    </div>

    <div class="container">
      <h2 class="sub-head">Selected key projects</h2>
      <p class="sub-lead">Offshore and renewable energy.</p>
      <ul class="kp-list">
        <li class="kp-row">
          <span class="kp-num">01</span>
          <span class="kp-name">SylWin Alpha Converter Platform</span>
          <span class="kp-scope">Offshore bridge repairs, steel fitting and structural welding works.</span>
        </li>
        <li class="kp-row">
          <span class="kp-num">02</span>
          <span class="kp-name">Thor Offshore Wind Farm</span>
          <span class="kp-scope">Cable installation, rigging and offshore support services.</span>
        </li>
        <li class="kp-row">
          <span class="kp-num">03</span>
          <span class="kp-name">Ostwind Offshore Wind Farm</span>
          <span class="kp-scope">Cable jointers, jointer&rsquo;s mates and rigging support.</span>
        </li>
        <li class="kp-row">
          <span class="kp-num">04</span>
          <span class="kp-name">Hywind Tampen</span>
          <span class="kp-scope">Rotational team support for offshore pull-in operations.</span>
        </li>
      </ul>
    </div>

    <div class="container">
      <h2 class="sub-head">Where we have delivered</h2>
      <p class="sub-lead">Onshore project experience.</p>
      <div class="on-grid">
        <div class="on-col">
          <p class="on-country">Germany</p>
          <p class="on-tag">3 locations</p>
          <div class="on-item"><p class="on-site">Rostock</p><p class="on-scope">Cruise &amp; river vessels · piping systems · pressure testing · structural welding</p></div>
          <div class="on-item"><p class="on-site">Frankfurt</p><p class="on-scope">Railway bridges · steel fitting · structural repairs · pipe welding, 5G position</p></div>
          <div class="on-item"><p class="on-site">Hamburg</p><p class="on-scope">Industrial maintenance · equipment &amp; hydro-turbine repairs</p></div>
        </div>
        <div class="on-col">
          <p class="on-country">Netherlands</p>
          <p class="on-tag">Offshore / North Sea</p>
          <div class="on-item"><p class="on-site">HKZ Alpha &amp; Beta — Petrofac</p><p class="on-scope">Offshore commissioning &amp; installation support</p></div>
          <div class="on-item"><p class="on-site">Thermo Fisher</p><p class="on-scope">Gas pipeline fabrication &amp; installation</p></div>
          <div class="on-item"><p class="on-site">Seafox</p><p class="on-scope">Jack-up vessel maintenance &amp; repair works</p></div>
        </div>
        <div class="on-col">
          <p class="on-country">United Kingdom</p>
          <p class="on-tag">1 location</p>
          <div class="on-item"><p class="on-site">Newcastle</p><p class="on-scope">Jack-up structures · steel erection · welding · offshore support</p></div>
        </div>
        <div class="on-col">
          <p class="on-country">Lithuania</p>
          <p class="on-tag">Headquarters</p>
          <div class="on-item"><p class="on-site">BLRT Group · Klaipėda</p><p class="on-scope">Offshore reel manufacturing · ship repair · piping systems · industrial maintenance</p></div>
        </div>
        <div class="on-col">
          <p class="on-country">Norway</p>
          <p class="on-tag">2 locations</p>
          <div class="on-item"><p class="on-site">Ålesund</p><p class="on-scope">Refrigeration systems · industrial modifications</p></div>
          <div class="on-item"><p class="on-site">Orkanger</p><p class="on-scope">Spool base &amp; offshore platforms · pipeline welding · fabrication · offshore support</p></div>
        </div>
      </div>
    </div>

    <div class="container">
      <h2 class="sub-head">From site</h2>
      <p class="sub-lead">Photographs from delivered and in-progress scopes.</p>
      <div class="shot-grid">
""" + shots_html() + """
      </div>
    </div>

""" + LIGHTBOX + """

    <div class="container prose">
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

    <div class="container">
      <!-- Filled in from BOOKING_URL in js/main.js. Stays hidden while that is
           empty, so an unconfigured calendar never ships as a dead panel. -->
      <section class="booking" data-booking-embed hidden aria-labelledby="booking-h">
        <span class="booking-corner" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
        <div class="booking-in">
          <p class="eyebrow">Book a call</p>
          <h2 id="booking-h">Take a 30-minute slot</h2>
          <p class="booking-lead">Straight into the diary of someone who can answer
          technical questions — scope, standards, crew dates.</p>
          <p class="booking-note">The calendar is hosted by Calendly. It loads only when
          you press the button, so nothing reaches them before you ask for it.</p>
          <button class="btn-bracket" type="button" data-booking-load>Open the calendar</button>
        </div>
        <p class="booking-alt">Or write to
        <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>.</p>
      </section>
    </div>


    <div class="container" id="enquiry">
      <div class="apply-panel">
        <div class="apply-intro">
          <p class="eyebrow">Enquiries</p>
          <h2>Send us a message</h2>
          <p>Send us the scope or the drawings and we will come back with a price and crew
          dates. The fastest route to a useful answer is the scope, the location, the
          standards that apply and the window you are working to.</p>
          <p>For personnel requests, tell us the disciplines, the certifications and the
          headcount.</p>
          <p class="apply-note">Applying for a job? The application form on the
          <a href="/careers.html">careers page</a> takes your CV and certificates with it.</p>
          <div class="apply-alt">
            <p class="eyebrow">Prefer not to fill in a form?</p>
            <a href="mailto:info@alprojects.eu?subject=Project%20enquiry">info@alprojects.eu</a>
            <a href="tel:+37063663744">Call +370 636 63 744</a>
            <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp +370 636 63 744</a>
          </div>
        </div>

        <form id="contactForm" class="apply-form" novalidate>
          <fieldset class="step">
            <div class="field">
              <label for="ctGroup">Service group</label>
              <select id="ctGroup" name="group" required aria-required="true">
                <option value="">Select a service group</option>
                <option>Mechanical & Industrial</option>
                <option>Marine</option>
                <option>Inspection & Access</option>
                <option>Not sure yet</option>
              </select>
            </div>
            <div class="field">
              <label for="ctTopic">Type of enquiry</label>
              <select id="ctTopic" name="topic" required aria-required="true">
                <option value="">Select a type of enquiry</option>
                <option>Project enquiry</option>
                <option>Request for personnel</option>
                <option>Inspection, NDT or rope access</option>
                <option>Invoicing or administration</option>
                <option>Something else</option>
              </select>
            </div>
            <div class="field">
              <label for="ctFirst">First name</label>
              <input id="ctFirst" name="first" type="text" required aria-required="true"
                     autocomplete="given-name" placeholder="First name">
            </div>
            <div class="field">
              <label for="ctLast">Last name</label>
              <input id="ctLast" name="last" type="text" required aria-required="true"
                     autocomplete="family-name" placeholder="Last name">
            </div>
            <div class="field">
              <label for="ctEmail">Email</label>
              <input id="ctEmail" name="email" type="email" required aria-required="true"
                     autocomplete="email" placeholder="name@company.com">
            </div>
            <div class="field">
              <label for="ctPhone">Phone <span class="opt">(optional)</span></label>
              <input id="ctPhone" name="phone" type="tel" autocomplete="tel"
                     placeholder="+370 ...">
            </div>
            <div class="field field-wide">
              <label for="ctCompany">Company <span class="opt">(optional)</span></label>
              <input id="ctCompany" name="company" type="text" autocomplete="organization"
                     placeholder="Company name">
            </div>
            <div class="field field-wide">
              <label for="ctMessage">How can we help?</label>
              <textarea id="ctMessage" name="message" rows="6" required aria-required="true"
                        placeholder="Scope, location, standards and dates."></textarea>
            </div>
          </fieldset>

          <div class="field field-check">
            <input id="ctConsent" name="consent" type="checkbox" required aria-required="true">
            <label for="ctConsent">I agree that ALPROJECTS, UAB may store these details in
            order to answer my enquiry. See the <a href="/privacy.html">privacy policy</a>.</label>
          </div>
          <!-- Spam trap: a real visitor never sees this, a bot fills it in. Named
               "website" and not "company" because company is a real field here. -->
          <div class="hp" aria-hidden="true">
            <label for="ctWebsite">Website</label>
            <input id="ctWebsite" name="website" type="text" tabindex="-1" autocomplete="off">
          </div>
          <div class="field">
            <button type="submit" class="btn-solid">Send the enquiry</button>
            <p class="form-note" id="contactNote" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>
    </div>

    <div class="container prose">
      <h2>Head office</h2>
      <p>ALPROJECTS, UAB<br>
      Šilutės pl. 2-536<br>
      LT-91110 Klaipėda<br>
      Lithuania</p>

      <h2>Where we work from</h2>
      <p>Lithuania &middot; Norway &middot; United Kingdom &middot; Netherlands &middot; Germany &middot; Belgium &mdash; offshore, shipbuilding and
      industry across Northern and Western Europe.</p>

      <h2>Email</h2>
      <ul class="contact-emails">
        <li><span class="contact-label">Project enquiries</span>
        <a href="mailto:info@alprojects.eu">info@alprojects.eu</a></li>
        <li><span class="contact-label">General</span>
        <a href="mailto:office@alprojects.eu">office@alprojects.eu</a></li>
      </ul>

      <h2>Phone</h2>
      <ul>
        <li><a href="tel:+37063663744">+370 636 63 744</a></li>
        <li><a href="tel:+37067020654">+370 670 20654</a></li>
      </ul>

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
    "logo": "https://alprojects.co/assets/logo-1200.png",
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
                            "addressLocality": "Klaipėda",
                            "postalCode": "LT-91110",
                            "streetAddress": "Šilutės pl. 2-536",
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


# ============================================================
# SERVICES — 12 services in 3 groups.
# Copy supplied by the client, 22 Aug 2026, used verbatim.
# ⚠️ Their own brief closes with: "All technical standards and
# process numbers to be confirmed by QA before publishing."
# ISO 4063 process numbers (141/131/135) are deliberately absent:
# the copy file in the client's own handover pack
# (04_Teksty/alprojects-services-copy.md, 22 Aug 2026) drops them,
# which settles the contradiction with the earlier paste.
# Still unconfirmed: ISO 3834 has no certificate on file, and
# IRATA/SOFT are unverified.
# ============================================================
SERVICE_GROUPS = [
    ("Mechanical & Industrial", [
        dict(slug="welding-services", nav="Welding Services", h1="Welding services",
             lead="A weld is only as good as the paperwork behind it. We weld structural steel "
                  "and piping systems by TIG (141), MAG (135) and flux-cored (136) processes, under an ISO 3834-2 "
                  "quality system. The welders hold current qualifications and the procedure is "
                  "approved before the first arc is struck.",
             points=["TIG for piping, root runs and stainless work",
                     "MAG (135) for structural steel fill and capping passes; MIG (131) for aluminium and non-ferrous work",
                     "Structural steel, pressure-retaining piping and pipe supports",
                     "Welder qualifications to EN ISO 9606-1, verified before mobilisation",
                     "WPS to EN ISO 15609-1, qualified by WPQR to EN ISO 15614-1, written for the project standard",
                     "Welding coordination and traceability under ISO 3834-2",
                     "Structural steel welding to EN 1090-1 and EN 1090-2, execution classes EXC2 and EXC3",
                     "Pressure piping to EN 13480 and PED 2014/68/EU, with pressure testing before insulation"]),
        dict(slug="pipe-fitting", nav="Pipe Fitting", h1="Pipe fitting",
             lead="Most delays in piping start with a bad fit-up. We supply fitters for process, "
                  "utility and engine room systems, instrument fitters for small-bore work, and "
                  "workshop crews who build spools straight from the isometrics. The dimensions "
                  "are checked before the welder arrives, not after.",
             points=["Process and utility piping in carbon steel and stainless steel, small bore to large bore",
                     "Instrument pipe fitters: small-bore, tubing, impulse lines and instrument hook-ups",
                     "Marine pipe fitters: engine room and system piping on newbuilds and repair",
                     "Spool prefabrication from isometrics, marked and traceable to the drawing",
                     "Fit-up, alignment and dimensional control before welding",
                     "Site installation, flange assembly and support during pressure testing"]),
        dict(slug="mechanical-contracting", nav="Mechanical Contracting", h1="Mechanical contracting",
             lead="Some clients need the whole scope taken off their hands. We install plant and "
                  "equipment, fabricate steel and build transformer packages, with our own "
                  "supervisors on site.",
             points=["Steel fabrication and mechanical installation",
                     "Transformer packages: bushings, coolers, conservators and connecting pipework",
                     "Equipment alignment and mechanical completion",
                     "One contract, one schedule, one point of contact",
                     "Our supervisors and our QA/QC engineers on site",
                     "Steel fabrication to EN 1090, mechanical completion documented and handed over as a package"]),
        dict(slug="heavy-equipment-relocation", nav="Heavy Equipment Relocation",
             h1="Heavy equipment relocation",
             lead="Moving a production line is a scheduling problem before it is a lifting problem. "
                  "We dismantle, move, reinstall and align it, inside a running plant or between "
                  "two countries.",
             points=["Dismantling, skidding, jacking and positioning on SPMT or hydraulic gantry",
                     "Disconnection and reconnection of piping and utilities",
                     "Foundation preparation, chocking, grouting and laser shaft alignment",
                     "Site-to-site moves across Europe",
                     "Abnormal load permits, escort and cargo securing to EN 12195-1, with CMR cover"]),
        dict(slug="mobile-repair-teams", nav="Mobile Repair Teams",
             h1="Mobile repair teams",
             lead="Every hour a unit stays down has a price. Our crews mobilise at short notice for "
                  "turnarounds, shutdowns and breakdowns, and they carry welding, fitting and "
                  "mechanical skills in the same team.",
             points=["Short-notice mobilisation",
                     "One crew, several trades",
                     "Turnarounds, shutdowns and breakdown repairs",
                     "Work under the plant&rsquo;s permit and safety regime"]),
    ]),
    ("Marine", [
        dict(slug="shipbuilding", nav="Shipbuilding", h1="Shipbuilding",
             lead="Yard schedules move, and the penalty lands on the subcontractor. We plan "
                  "for that, and take engine room piping, structural steel and outfitting "
                  "as complete scopes.",
             points=["Engine room piping: fuel, lube oil, cooling water, ballast and bilge systems, including spool prefabrication",
                     "Hull structural fitting and welding to class-approved procedures",
                     "Outfitting and mechanical installation",
                     "Scopes delivered to the yard&rsquo;s schedule and class-approved drawings"]),
        dict(slug="ship-repair", nav="Ship Repair", h1="Ship repair",
             lead="Repair work is decided in days, not months. We take steel renewal, piping "
                  "replacement and mechanical repairs to class and to the owner&rsquo;s requirements.",
             points=["Steel renewal and piping replacement",
                     "On-board mechanical repairs",
                     "Drydock and afloat (alongside) repair scopes",
                     "Fast mobilisation to the vessel"]),
    ]),
    ("Inspection & Access", [
        dict(slug="non-destructive-testing", nav="Non-Destructive Testing",
             h1="Non-destructive testing",
             lead="Nobody should be signing off their own work. UT, PT and MT let us inspect "
                  "while the plant keeps running; radiography is planned around production "
                  "windows. We report to the client, not to the contractor who did the welding.",
             points=["Visual testing (VT) to EN ISO 17637 and penetrant testing (PT) to EN ISO 3452",
                     "Magnetic particle testing (MT) to EN ISO 17638 and ultrasonic testing (UT) to EN ISO 17640",
                     "Phased array (PAUT) and TOFD where radiography is not practical",
                     "Technicians certified to ISO 9712 Level II and Level III",
                     "Acceptance to EN ISO 5817 and ISO 10675, or to the project specification",
                     "Inspection with the plant running, where the method allows it",
                     "Independent third-party verification, reported to the client in their format"]),
        dict(slug="rope-access-services", nav="Rope Access Services", h1="Rope access services",
             lead="Scaffolding costs more in downtime than in steel. Certified technicians reach the "
                  "same place on rope, inspect it and repair it while the plant keeps running.",
             points=["IRATA-certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site",
                     "Inspection and mechanical work at height",
                     "Rescue plan and supervision on every job",
                     "Often without scaffolding, and usually without a shutdown"]),
        dict(slug="3d-laser-scanning", nav="3D Laser Scanning", h1="3D laser scanning",
             lead="Old drawings lie. We measure what is really there and hand the data to your "
                  "engineers, so the clash shows up on a screen instead of on site.",
             points=["As-built survey of existing installations",
                     "Dimensional control of structures and piping",
                     "Clash detection before fabrication",
                     "Data in the client&rsquo;s CAD format"]),
        dict(slug="quality-control", nav="Quality control (QA/QC)", h1="Quality assurance and quality control (QA/QC)",
             lead="Quality is what you can prove afterwards. We inspect piping and steel structures "
                  "and leave documentation that holds up when the client, the surveyor or the "
                  "auditor asks for it.",
             points=["Piping and steel structure verification",
                     "Traceability down to the individual weld",
                     "Support at client and third-party hold and witness points",
                     "Inspection and Test Plans (ITP) with hold, witness and review points agreed before work starts",
                     "Quality system certified to ISO 9001; welding under ISO 3834-2",
                     "Manufacturing Record Book (MRB) assembled as the work goes, not at the end"]),
        dict(slug="rigging-technical-support", nav="Rigging &amp; Technical Support",
             h1="Rigging and technical support",
             lead="Lifts go wrong at the planning stage. We plan them, and we send the people who "
                  "run them on site.",
             points=["Lift planning and execution",
                     "Load handling and installation support",
                     "Site coordination and supervision",
                     "Offshore and industrial projects"]),
    ]),
]

ROPE_DEEP = """
      <div class="srv-deep-band">
        <img src="/assets/tia-band.webp" alt="Rope access technician descending onto an offshore topside above open water"
             width="1700" height="566" loading="lazy" decoding="async">
        <span class="srv-deep-scrim" aria-hidden="true"></span>
      </div>

      <div class="container srv-deep-in">
        <p class="eyebrow">What it is</p>
        <div class="srv-deep-grid">
          <div>
            <h2 class="srv-deep-head">The scaffold costs more than the repair</h2>
            <p class="srv-deep-body">Nobody buys rope access because they want ropes. They buy it
            because the alternative is a scaffold, a crane, a vessel day or a shutdown. Each of
            those costs more than the work itself.</p>
            <p class="srv-deep-body">Our technicians hold IRATA and SOFT certification and most of
            them carry a second trade: inspection, welding or mechanical fitting. One person on the rope
            replaces a scaffold crew and an inspector standing behind them.</p>
            <p class="srv-deep-note">Every crew works with a written rescue plan and a supervisor
            on site. Without both, the job does not start.</p>
          </div>
          <dl class="srv-spec">
            <div><dt>Certification</dt><dd>IRATA and SOFT</dd></div>
            <div><dt>Typical mobilisation</dt><dd>short notice, crews of 2&ndash;6</dd></div>
            <div><dt>Sectors</dt><dd>offshore wind, oil and gas, industry, marine</dd></div>
            <div><dt>Deliverable</dt><dd>report in the client&rsquo;s format</dd></div>
          </dl>
        </div>

        <div class="srv-deep-photos">
          <figure>
            <img src="/assets/tia-people.webp" alt="Rope access technician working on a wind turbine blade"
                 width="860" height="645" loading="lazy" decoding="async">
          </figure>
          <figure>
            <img src="/assets/tia-hero.webp" alt="Three technicians on a wind farm site at first light"
                 width="1900" height="814" loading="lazy" decoding="async">
          </figure>
        </div>
        <p class="srv-deep-note srv-deep-caption">The same crew works offshore topsides, turbine
        blades and onshore wind. Rope access is how they get there; the trade they carry is what
        they do once they arrive.</p>
      </div>
"""


SERVICES_FLAT = [sv for _, group in SERVICE_GROUPS for sv in group]
for _i, _sv in enumerate(SERVICES_FLAT, 1):
    _sv["num"] = "%02d" % _i

# A service may carry a longer block below the shell. Only rope access has one;
# the rest render nothing there. It travels in the JSON payload with everything
# else, because switching services never reloads the page -- appended straight
# into the document it would still be sitting under "Welding services" one click
# later.
DEEP_BLOCKS = {"rope-access-services": ROPE_DEEP}
for _sv in SERVICES_FLAT:
    _sv["deep"] = DEEP_BLOCKS.get(_sv["slug"], "")



def service_nav(active_slug):
    """Left column: the twelve services in their three groups."""
    out = ['        <p class="eyebrow">All services</p>']
    for label, group in SERVICE_GROUPS:
        out.append('        <div class="srv-group">')
        out.append('          <p class="srv-group-label">%s</p>' % label)
        out.append('          <ul class="srv-list">')
        for sv in group:
            cls = "srv-link is-active" if sv["slug"] == active_slug else "srv-link"
            aria = ' aria-current="page"' if sv["slug"] == active_slug else ''
            out.append('            <li><a class="%s" href="/services/%s.html" data-service="%s"%s>'
                       '<span class="srv-n">%s</span><span class="srv-name">%s</span></a></li>'
                       % (cls, sv["slug"], sv["slug"], aria, sv["num"], sv["nav"]))
        out.append('          </ul>')
        out.append('        </div>')
    return "\n".join(out)


def service_panel(sv):
    points = "\n".join('            <li>%s</li>' % p for p in sv["points"])
    return ('        <article class="srv-item" data-panel="{slug}">\n'
            '          <p class="srv-count">{num} / 12</p>\n'
            '          <h1 class="srv-title">{h1}</h1>\n'
            '          <p class="srv-lead">{lead}</p>\n'
            '          <ul class="srv-points">\n{points}\n          </ul>\n'
            '          <a class="srv-cta" href="/contacts.html">Discuss a project '
            '<span aria-hidden="true">&rarr;</span></a>\n'
            '        </article>').format(slug=sv["slug"], num=sv["num"],
                                        h1=sv["h1"], lead=sv["lead"], points=points)


def service_page_body(sv):
    """The two-column block with one service open. Only the active service is
    rendered as HTML -- one h1 per page, and no twelve-fold duplicate content
    across twelve URLs. The rest travel as JSON so switching is instant."""
    payload = _json.dumps(
        [{k: x[k] for k in ("slug", "num", "h1", "lead", "points", "deep")} for x in SERVICES_FLAT],
        ensure_ascii=False, separators=(",", ":"))
    return ('\n    <section class="srv-shell">\n'
            '      <div class="container srv">\n'
            '        <nav class="srv-nav" aria-label="Services">\n'
            '{nav}\n'
            '        </nav>\n'
            '        <div class="srv-panel">\n'
            '{panel}\n'
            '          <div class="srv-controls">\n'
            '            <button class="srv-arrow" type="button" data-srv-prev '
            'aria-label="Previous service">&larr;</button>\n'
            '            <button class="srv-arrow" type="button" data-srv-next '
            'aria-label="Next service">&rarr;</button>\n'
            '            <span class="srv-pos" aria-live="polite">{num} / 12</span>\n'
            '          </div>\n'
            '        </div>\n'
            '      </div>\n'
            '    </section>\n'
            '    <section class="srv-deep" id="srvDeep">{deep}</section>\n'
            '    <script type="application/json" id="srv-data">{payload}</script>\n'
            ).format(nav=service_nav(sv["slug"]), panel=service_panel(sv),
                     num=sv["num"], deep=sv["deep"], payload=payload)


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

# --- services: one URL per service, plus /services.html as the index ---
def _service_desc(sv):
    d = re.sub(r"<[^>]+>", "", sv["lead"]).replace("&rsquo;", "'")
    return (d[:152].rsplit(" ", 1)[0] + "...") if len(d) > 155 else d


for _sv in SERVICES_FLAT:
    write("services/%s.html" % _sv["slug"],
          page(_sv["h1"], _service_desc(_sv), service_page_body(_sv),
               canonical="/services/%s.html" % _sv["slug"], og="services",
               head_extra=breadcrumb_ld([("Home", "/"), ("Services", "/services.html"),
                                         (_sv["h1"], "/services/%s.html" % _sv["slug"])])))

# /services.html shows the first service, and is the entry point people link to
write("services.html", page("Services",
      "Welding, pipe fitting, mechanical contracting, marine works, NDT, rope access and "
      "quality control for industrial and offshore projects across Europe.",
      service_page_body(SERVICES_FLAT[0]), canonical="/services.html", og="services"))

write("projects.html", page("Projects",
      "Shipbuilding, offshore, industrial and renewable energy projects delivered by ALPROJECTS Group across Europe.",
      PROJECTS, canonical="/projects.html", og="projects"))

# --- one page per project case, under /projects/ ---
# /projects.html wins over the /projects/ directory on GitHub Pages, the same
# way /services.html does, so the index keeps its URL and the cases sit under it.
for _i, _c in enumerate(CASES):
    write("projects/%s.html" % _c["slug"],
          page(_c["title"], _c["lead"][:152].rsplit(" ", 1)[0] + "...",
               case_body(_c, CASES[(_i + 1) % len(CASES)]),
               canonical="/projects/%s.html" % _c["slug"],
               og="projects",
               head_extra=breadcrumb_ld([("Home", "/"), ("Projects", "/projects.html"),
                                         (_c["title"], "/projects/%s.html" % _c["slug"])])))

write("contacts.html", page("Contacts",
      "Contact ALPROJECTS Group — Šilutės pl. 2-536, Klaipėda, Lithuania. Project enquiries and personnel requests.",
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



# ---------------- sector pages (TZ §4.2: each card its own page) ----------------
SECTOR_PAGES = [
    ("shipbuilding", "Shipbuilding", "sector-shipbuilding",
     "Yard schedules move, and the penalty lands on the subcontractor. We plan for "
     "that, and take engine room piping, structural steel and outfitting as complete "
     "scopes, on newbuilds and on repair.",
     ["welding-services", "pipe-fitting", "shipbuilding", "ship-repair", "quality-control"]),
    ("offshore", "Offshore", "sector-offshore",
     "Mobilising a team offshore is expensive and a shutdown is more expensive still. "
     "Rope access and NDT carry most of this work, with mechanical scopes alongside.",
     ["rope-access-services", "non-destructive-testing", "rigging-technical-support",
      "welding-services", "quality-control"]),
    ("industrial", "Industrial", "sector-industry",
     "Plant installation, process piping and mechanical packages, delivered as a whole "
     "scope with our own supervisors and our own QA on site.",
     ["mechanical-contracting", "pipe-fitting", "heavy-equipment-relocation",
      "mobile-repair-teams", "3d-laser-scanning"]),
    ("renewables", "Renewables", "sector-wind",
     "Cable installation, rigging and offshore support on wind farms, plus the fuel "
     "handling infrastructure that sits behind them.",
     ["rigging-technical-support", "welding-services", "rope-access-services",
      "mechanical-contracting", "non-destructive-testing"]),
]


def sector_body(slug, name, img, lead, service_slugs):
    by_slug = {sv["slug"]: sv for sv in SERVICES_FLAT}
    links = "\n".join(
        '            <li><a href="/services/%s.html">%s</a></li>' % (s, by_slug[s]["nav"])
        for s in service_slugs if s in by_slug)
    return """
    <section class="sector-hero">
      <img class="sector-hero-img" src="/assets/projects/%(img)s-1200.webp"
           alt="" width="1204" height="1017" fetchpriority="high" decoding="async">
      <span class="sector-hero-scrim" aria-hidden="true"></span>
      <div class="container sector-hero-in">
        <p class="eyebrow">Sector</p>
        <h1 class="sector-hero-title">%(name)s</h1>
        <p class="sector-hero-lead">%(lead)s</p>
      </div>
    </section>

    <div class="container sector-body">
      <div class="sector-cols">
        <div>
          <h2 class="sub-head">What we do here</h2>
          <ul class="sector-services">
%(links)s
          </ul>
        </div>
        <div class="sector-aside">
          <p>Send the drawings or the scope and we will come back with a price and crew
          dates. If it is a shutdown, tell us the window.</p>
          <p class="back">
            <a class="btn-solid" href="/contacts.html">Send us the scope</a>
            <a class="btn-outline" href="/projects.html">See our projects</a>
          </p>
        </div>
      </div>
    </div>
""" % dict(img=img, name=name, lead=lead, links=links)


for _slug, _name, _img, _lead, _svcs in SECTOR_PAGES:
    write("sectors/%s.html" % _slug,
          page(_name, _lead[:150], sector_body(_slug, _name, _img, _lead, _svcs),
               canonical="/sectors/%s.html" % _slug, og="projects",
               head_extra=breadcrumb_ld([("Home", "/"), ("Projects", "/projects.html"),
                                         (_name, "/sectors/%s.html" % _slug)])))

# ---------------- sitemap ----------------
# Generated from the same page list that writes the HTML, so a renamed or
# added article can never leave a dead URL behind in the sitemap.
SITEMAP = [
    ("/",              "monthly", "1.0"),
    ("/services", "monthly", "0.9"),
] + [("/services/%s" % sv["slug"], "monthly", "0.7") for sv in SERVICES_FLAT] \
  + [("/sectors/%s" % s0, "monthly", "0.7") for s0, _n, _i, _l, _v in SECTOR_PAGES] + [
    ("/projects", "monthly", "0.9"),
] + [("/projects/%s" % c["slug"], "monthly", "0.7") for c in CASES] + [
    ("/company.html",  "monthly", "0.8"),
    ("/news/",         "weekly",  "0.8"),
    ("/contacts", "yearly",  "0.7"),
    ("/careers.html",  "monthly", "0.6"),
    ("/privacy.html",  "yearly",  "0.2"),
] + [("/news/%s" % a["slug"], "yearly", "0.6") for a in ARTICLES]

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

# The sitemap has two authors. This one knows every page; tools/i18n_build.py
# knows the hreflang alternates. Whichever ran last used to win, so a bare
# `python3 tools/build-pages.py` silently replaced a 136-alternate sitemap with
# an EN-only one -- verified: x-default went from 136 occurrences to 0, with no
# error and nothing in the diff to notice. Hand the job to i18n_build whenever a
# language is published, so the order of the two commands stops mattering.
def _write_sitemap():
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import i18n
        if any(i18n.PUBLISH.get(l) for l in i18n.LANGS if l != i18n.DEFAULT):
            import i18n_build
            write("sitemap.xml", i18n_build.sitemap(i18n_build.source_pages()))
            return
    except Exception as exc:                      # never block the page build
        print("sitemap: falling back to the English-only map (%s)" % exc)
    write("sitemap.xml", sitemap())


_write_sitemap()


# index.html and 404.html are hand-maintained rather than generated, so stamp
# them in place -- otherwise they would be the pages that still serve stale CSS.
for _name in ("index.html", "404.html"):
    _path = os.path.join(ROOT, _name)
    _before = io.open(_path, encoding="utf-8").read()
    _after = clean_urls(stamp(_before))
    if _after != _before:
        io.open(_path, "w", encoding="utf-8").write(_after)
        print("stamped %s" % _name)

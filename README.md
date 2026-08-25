# ALPROJECTS Group — website

Static site (HTML/CSS/JS, no build step). Built from the Figma design. Made by ALDY.

## Structure

```
index.html         — the homepage (all sections, matching the Figma frame)
company.html       — about the company
services.html      — the five service lines in depth
projects.html      — shipbuilding / offshore / industrial / renewable
contacts.html      — address, email, both phone numbers
careers.html       — careers / open application
privacy.html       — privacy policy
404.html           — custom not-found page (GitHub Pages serves it automatically)
news/index.html    — news listing
news/*.html        — five article pages
css/style.css      — design tokens + all styles, responsive down to mobile
css/fonts.css      — self-hosted Montserrat @font-face
js/main.js         — config block, nav, reveals, counters, newsletter
assets/            — images (WebP) and fonts
tools/build-pages.py — regenerates the sub-pages from index.html's header/footer
```

The sub-pages are committed as plain HTML — nothing needs to run to serve the
site. Re-run `python3 tools/build-pages.py` only after editing the header or
footer in `index.html`, so the copies don't drift.

## Mobile

Audited with real device emulation (Playwright, DPR 3, touch) at 360x740,
375x667, 390x844, 412x915 and 430x932 — Chrome's headless window clamps at
500px, so these widths could not be tested any other way.

Every page reports zero horizontal overflow, no tap target under the 24px
WCAG 2.2 minimum, and no text-entry field under 16px. That last one is
functional, not typographic: iOS Safari zooms the page when a focused input is
smaller than 16px.

What the audit changed:

- form fields to 16px on mobile (the desktop rules use `input[type=...]`
  selectors, so the mobile override has to match that specificity or it loses);
- 44px burger with `flex: none`, since a flex item shrinks below its width;
- vertical padding on inline links, which were 15-20px tall;
- the header "Book a call" wrapped to two lines and crowded the logo on a
  phone, so below 560px it moves into the menu as a full-width action;
- `scroll-margin-top` on anchor targets — `#apply` and friends were landing
  underneath the fixed header, on desktop as well;
- crosshairs and card corner brackets are hidden on touch: they are hover-only
  decoration and were the last thing extending past their parent's box.

Verified by driving the phone, not just measuring it: the menu opens and
closes, `aria-expanded` toggles, body scroll locks and restores, all seven
links navigate, and the careers form validates.

## Contrast

Body and label colours are checked against WCAG 2.2 AA (4.5:1 for normal text,
3:1 for large). `--gray-150` was originally sampled at `#5f5e70`, which measured
2.9-3.2:1 on the dark grounds and was the single cause of all 56 contrast
failures across the site. It was raised to `#828195` — same hue and saturation,
lifted until it clears 4.5:1 on the darkest panel with margin (4.8:1) — which
keeps it visibly quieter than `--muted` at 6.2:1, so the type hierarchy is
unchanged. If you re-sample the palette from Figma, re-check this one.

### The header is transparent, and two things keep the nav readable

There is no header background at any scroll position — the nav floats over
whatever is passing under it. Scrolled fully bare, that measured **1.06:1** on
`/careers.html`: photographs, the white certificate scans and the light panels
all pass beneath it. Two things replace the bar, and removing either one breaks
the nav on the bright sections:

- `.site-header::after` — a scrim fixed to the top of the viewport, 132px tall,
  fading to nothing. Because it ends on zero there is no edge anywhere, so it
  reads as the screen being darker at the top rather than as a bar.
- `.main-nav a` is `#b0b7c8`, deliberately lighter than `--muted` and set only
  here. On the brightest section the ground still reads 68 out of 255 through
  the scrim; at `--muted` that is 3.3:1, at this colour 4.9:1.

Worst case across every page and scroll position is now 4.83:1 (the
certificates on the home page); everything else is 5:1 to 9.8:1. `html.menu-open`
puts a solid ground back while the mobile panel is open, since that panel is
opaque and starts at the header's bottom edge.

## Accessibility

Audited across every page with a headless probe: one `<h1>` per page, no
heading-level jumps, no images without `alt`, no links without an accessible
name, no duplicate `id`s, and no JavaScript errors. Card, team-member and footer
headings are levelled to keep the outline continuous — the CSS targets those
levels directly, so changing a heading level means changing both.

## No horizontal scrolling — how it's enforced

`overflow-x` lives on `<html>`, not `<body>`. Setting it on `<body>` makes body a
scroll container, which changes how `position: sticky` resolves in the services
section. `overflow-x: clip` is used where supported (it clips without creating a
scroll container) with `hidden` as the fallback for older Safari.

That is the safety net, not the fix. The actual guarantee comes from:

- grid/flex children get `min-width: 0` — they default to `min-width: auto` and
  refuse to shrink below their content, which is the usual cause of sideways
  scroll on narrow screens;
- `overflow-wrap: break-word` on body, so a long email or URL can't push the
  layout wider;
- no `100vw` anywhere (it includes the scrollbar and overflows by its width).

Measured at 500/768/1024/1440/1920: `document.scrollWidth` equals the viewport
and **zero elements extend past the right edge**. Before this change the partner
marquee put 16–20 elements past it, hidden only by the clip.

## Technical drawing motif

The grid and "+" registration marks from the Figma frame are a reusable system
rather than hero-only decoration:

- `.tech-grid` paints the drafting grid on a section and fades it in when the
  section scrolls into view;
- `.xhair` corner marks are injected by JS into panels that can carry them.

Both are applied from `js/main.js` (`GRID_SECTIONS` / `CROSSHAIR_TARGETS`), so
the generated sub-pages pick them up with no markup changes — edit those two
arrays to change where the motif appears. Everything respects
`prefers-reduced-motion`.

### Hidden: blueprint mode

Press **B** anywhere on the site to overlay the full drafting sheet — stronger
grid, registration marks, dashed outlines, and the real pixel size of each card
rendered as a dimension label, in the spirit of the `200x200` annotation in the
design. Press B again to exit; the state is remembered for the tab only, and the
key is ignored while typing in a form field.

**Then drag anywhere to measure.** A dimension line with end caps and a live
pixel readout follows the cursor — the drafting tool the rest of the motif
implies. Mouse only (never interferes with touch scrolling), suppressed over
links and form fields, cleared with Escape. There is also a short console note
for anyone who opens dev tools.

It is deliberately undiscoverable by accident: nothing on the page advertises it,
so it reads as a detail for people who go looking rather than a gimmick.

## Hero spacing

The hero is `100vh` with the bottom bar pinned by `margin-top: auto`, which used
to pool every pixel of leftover height into one gap under the project cards
(209px at 1512x895). Three changes distribute it instead:

- the cards grid flex-grows into the spare height (capped, so it keeps roughly
  the design's proportion), and the renders scale with it rather than sitting
  small in a tall box;
- `.hero-tags` carries `margin-bottom: auto` as well, so two auto margins split
  the remaining slack evenly above and below the cards instead of one pooling it;
- the hero's bottom padding scales with viewport height.

Measured gap under the cards: 0-15px at 1024x681, 1440x813, 1512x895, 1920x993
and 1920x1113 — down from 209px at the worst size.

## Viewport notes

The hero's vertical rhythm comes from the 1920x1200 Figma frame. On a laptop
that is taller than the fold, so `css/style.css` ends with two short-viewport
blocks (`max-height: 920px` and `max-height: 700px`) that compress the hero
spacing, title size and card height. Measured overflow is 0 at 1920x1113,
1512x773 (MacBook Pro 14"), 1512x613, 1440x693 and 1280x713. Below roughly
560px of viewport height the hero no longer fits and the page scrolls, which
is expected.

## Performance notes

- All photographs are WebP (37% smaller than the original JPEGs: 1.39 MB → 875 KB).
  `assets/hero-bg.jpg` is kept **only** as the `og:image`, since some social
  scrapers still handle WebP poorly.
- Montserrat is self-hosted from `assets/fonts/` as a variable font (two subset
  files, latin + latin-ext). This removes the render-blocking round trip to
  fonts.googleapis.com *and* the disclosure of visitor IPs to Google — which is
  why the privacy policy can state the site loads no third-party resources.
- HTML/CSS/JS are served gzipped by GitHub Pages (7.4 / 6.8 / 3.2 KB).
- `cache-control: max-age=600` is GitHub Pages' fixed default and cannot be
  changed on this host. A CDN in front would be the only way to improve it.

## Cache busting

GitHub Pages serves CSS and JS with `max-age=600` and no fingerprint in the
filename, so a browser can keep using an old stylesheet after a deploy. On iOS
Safari this is stubborn enough that a fixed layout can still look broken on a
phone while it is provably correct on the server — which reads as "the fix
didn't work" and costs a debugging round trip.

`tools/build-pages.py` therefore stamps `?v=<first 8 of the file's sha256>` onto
every reference to `css/style.css`, `css/fonts.css` and `js/main.js`, in the
generated pages *and* in the two hand-maintained ones (`index.html`, `404.html`).
Change the CSS, re-run the generator, and every page points at a URL the browser
has never seen. **Re-run `python3 tools/build-pages.py` after editing CSS or JS**,
or the stamp goes stale and the old file keeps being served.

## Deploy (GitHub Pages)

Repo: `git@github.com:aldy-lab/alprojects.git` — the `main` branch is the site.
Domain: **alprojects.co** (registered at GoDaddy). The `CNAME` file in the repo
root tells Pages about it — don't delete it, or the custom domain resets.

1. Push to `main`.
2. Repo → Settings → Pages → Source: `Deploy from a branch`, `main`, `/ (root)`.
3. GoDaddy → the alprojects.co domain → DNS. Delete the parked/forwarding
   records GoDaddy adds by default, then add:

   | Type  | Name | Value                  |
   |-------|------|------------------------|
   | A     | @    | 185.199.108.153        |
   | A     | @    | 185.199.109.153        |
   | A     | @    | 185.199.110.153        |
   | A     | @    | 185.199.111.153        |
   | CNAME | www  | aldy-lab.github.io.    |

4. Wait for DNS to propagate (GoDaddy is usually minutes, can be up to an hour),
   then tick **Enforce HTTPS** in Pages settings once the certificate is issued.

Any static host works the same way (Netlify/Cloudflare Pages: drag the folder in).

## Design system

`css/style.css` opens with the Figma style sheet as CSS custom properties —
the palette, the semantic roles built on it, and the type scale. Change a
value there and the whole site follows.

```
Colors      --white --gray-50 --gray-100 --gray-150 --gray-200
            --black --blue --beige
Roles       --bg --text --muted --muted-2 --accent (beige) --accent-deep (blue)
Typography  --h1 … --h6, --text-xl/l/m/s, --tag, --numbers
```

⚠️ The colour values were **sampled by eye from the style-sheet image**, not
exported from Figma. They are close but not guaranteed exact — paste the real
hex codes into the palette block before launch.

Two notes on adopting the scale:

- Three near-identical heading sizes (max 56/52/48px) were unified to a single
  `--h2` (52px), and the one off-scale 14px body size became `--text-l` (15px).
  That is the point of the scale, but it does mean a few headings shifted a
  couple of pixels from the original Figma frame.
- `BLUE` tints the certifications panel glow. **`BEIGE` is deliberately unused**:
  it was tried as the accent and read cheap against this palette — ALPROJECTS'
  own LinkedIn carousels use white and cool light steel on deep navy and never a
  warm accent for text. `--accent` is `--gray-50`; the beige token stays defined
  in case it is wanted for print.

## Services

Twelve services in three groups, from the client's brief of 22 Aug 2026. The
data lives in `SERVICE_GROUPS` in `tools/build-pages.py`; the copy there is
theirs, verbatim.

**Every service has its own URL** — `/services/welding-services.html` and so on
— and `/services.html` is the index, opening on the first. Only the open
service is rendered as HTML, so each page has one `h1` and there is no
twelve-fold duplicate content across twelve URLs; the other eleven travel as
JSON in `#srv-data` and the panel is re-rendered client-side with `pushState`.
With JavaScript off the links are ordinary links to real pages and everything
still works.

⚠️ **Their own brief ends: "All technical standards and process numbers to be
confirmed by QA before publishing."** Three specific items are unresolved:

- The ISO 4063 process numbers (141 / 131 / 135) are live because the final
  copy carries them, but the accompanying rationale said they had been removed.
  One of the two documents is out of date.
- The welding copy states work is done "under an ISO 3834 quality system".
  There is still no ISO 3834 certificate among the three DNV documents.
- Rope access claims "IRATA and SOFT certified technicians" — unverified.

Also unresolved from the brief itself: it flags that **Heavy Equipment
Relocation (04) and Rigging (12) overlap** and must be separated, but the copy
supplied still describes both with overlapping scope. That is a decision for
the client, not a copy edit.

## Motion and controls

Both were ad-hoc and are now tokenised in `:root`.

```css
--dur-1: 150ms;  /* colour, border, opacity        */
--dur-2: 260ms;  /* buttons, links, small moves    */
--dur-3: 420ms;  /* card lifts, image zoom         */
--dur-4: 700ms;  /* entrances and reveals          */
--btn-h: 48px;   /* every button, no exceptions    */
--lift: -5px;    /* every card hover               */
--zoom: 1.04;    /* every image hover              */
```

There were **fourteen** different transition durations before; 50 declarations
now resolve to those four. Button height varied by *context* rather than by
kind — `.btn-bracket` measured 49px on the homepage but 51px inside `.prose`,
`.btn-solid` 45px in the header but 41px on the careers form — because both
inherited line-height from their wrapper. They share a base rule with
`line-height: 1` and `min-height: var(--btn-h)`, so the box no longer depends on
what wraps it. ⚠️ `.menu-cta` is excluded: it is a menu row, not a button.

`--lift` and `--zoom` become `0` / `1` under `prefers-reduced-motion`, so hover
motion stands down along with the entrance animations.

**Reveals are progressive, not load-bearing.** An inline script in `<head>` adds
`js` to `<html>`, and only `.js .reveal` starts at `opacity: 0`. Without it a
blocked or failed `main.js` left 47 of 50 blocks invisible — a blank page. Keep
that script first in `<head>` on any new page.

## Europe map

`assets/europe-outline.png` is traced from the client's own Company Profile map
(page 3). That artwork had four countries filled solid white, so the fills were
removed morphologically and each filled country's border rebuilt from the edge
of its own fill — otherwise Norway, Germany, Poland and Lithuania came back with
no outline at all.

Hovering a country fills it blue, from a per-country alpha mask in `assets/map/`.
The masks come from labelling the enclosed regions of the outline; each was
confirmed by checking whether that region was filled white in the original
artwork (only Norway, Lithuania, Poland and Germany were).

⚠️ **Four of the five countries fill; Lithuania is marker-only.** In the source
artwork Poland and Lithuania are one shape with no border drawn between them —
proven, not assumed: no binarisation threshold separates them, and reinstating
the internal seams recovered Germany but never split those two. Filling
"Lithuania" would fill Poland with it. Send a country-level vector map (SVG or
GeoJSON) and all five can fill properly.

Marker labels only show for the country being pointed at: statically, "United
Kingdom", "Netherlands" and "Germany" collide on this projection at any map size
that fits the layout. The list beside the map names them all anyway.

The map sits beside the country list rather than above it. Stacked, the
footprint section ran 1995px — 2.1 screens — with the map alone taking 791px;
it is 1160px now. Hovering or focusing a country row lifts its marker and dims
the others, and hovering a marker highlights its row. Both carry the same
information independently, so the link is enhancement only.

Marker positions are percentages verified against the measured region bounding
boxes of the outline itself (`Germany x[253-338] y[295-411]`, `UK x[133-212]
y[217-348]`, `Norway x[265-352] y[102-243]`), not eyeballed.

## Configuration

All go-live values live in one block at the top of `js/main.js`. Fill a URL in
and the link switches on; **leave it `""` and the link is removed from the page
entirely**, so no dead `href="#"` links ever ship.

```js
var BOOKING_URL = "https://calendly.com/aleksandr-alprojects/30min";
                                    // header "Book a call" + the contacts calendar
var SOCIAL       = { instagram, linkedin, facebook }; // header + footer (filled in)
var MEMBER_SOCIAL = { "aleksandr-vasiljev": {...}, … } // team cards
var FORM_ENDPOINT = "";             // newsletter POST target
var CAREERS_ENDPOINT = "";          // job application POST target
var ANALYTICS_DOMAIN = "";          // cookieless analytics — see below
```

**Analytics** is off, and "off" means no third-party request is made at all —
no cookie banner is required and nothing needs disclosing. To switch it on, set
`ANALYTICS_DOMAIN` to the domain you registered with Plausible; the loader
appends their script at runtime. ⚠️ **If you enable it you must also update the
privacy policy** — `tools/build-pages.py` already holds the replacement wording
as an HTML comment right below the "loads no third-party scripts" paragraph in
the PRIVACY block: delete that paragraph, uncomment the two below it, re-run the
generator. Plausible is used rather than Google Analytics because it sets no
cookies and stores no personal data, which keeps the GDPR position simple.

**Open positions** live in `POSITIONS` at the top of `tools/build-pages.py` —
one dict per role. Set `open=False` to take a role off the live page without
deleting it; when none are open the page shows an "open applications welcome"
notice instead. Edit the list, run `python3 tools/build-pages.py`, commit.

⚠️ Only list roles the company is actually recruiting for. The one role
currently listed (30 certified TIG welders) comes from ALprojects Group's own
LinkedIn post and should be removed once it is filled.

## Content source: the client's presentations

`assets/downloads/` holds the two PDFs the client supplied — the Company
Profile (16pp) and Reference Projects (8pp). They are the authority for company
facts, and most of the homepage now mirrors their priorities: the four sector
photographs, the five-country footprint, the ten named clients, the "qualified
specialists" personnel split, ISO 3834 alongside 9001/14001/45001, and the named
offshore projects on `projects.html`.

The photography on the site is extracted from those PDFs and from the 14 site
photographs the client sent — `tools/` has no extractor script because it was a
one-off, but the method was: JPEGs inside the Reference Projects PDF are plain
`DCTDecode` streams (scan for `FFD8...FFD9`), while the Company Profile wraps
them as `[/FlateDecode /DCTDecode]`, so those need a `zlib.decompress` first.
⚠️ **Caption honestly.** Photographs are captioned by what is visibly happening,
not by the client or project name, unless the profile actually evidences it.

## Search & sharing

- **Structured data** (JSON-LD, generated in `tools/build-pages.py`):
  `Organization` on every page, `JobPosting` on `careers.html` (this is what
  makes the roles eligible for **Google for Jobs** — the free jobs panel in
  search results), `Article` on each news post, and `BreadcrumbList` on both.
  `_strip()` drops empty fields before serialising, because Google rejects a
  block containing `null`. Validate at `search.google.com/test/rich-results`.
- **Share images** — each page has its own 1200×630 card in `assets/og/`,
  rendered by `python3 tools/make-og.py` from `tools/og-template.html` (headless
  Chromium via Playwright). Title and eyebrow come from the page list at the top
  of that script; titles over 38 characters get a `.long` class that steps the
  size down. Re-run it after renaming a page, then point `og=` at the new card
  in `build-pages.py`.
- **Page titles** are kept under 60 characters, the point at which Google
  truncates. `" — ALPROJECTS Group"` costs 19 of that, so an article whose real
  headline is longer carries a short `seo=` field in `ARTICLES`; the full title
  still runs as the `<h1>`.
- **Sitemap** — `sitemap.xml` is generated by `build-pages.py` from the same
  article list that writes the HTML, so a renamed article can no longer leave a
  dead URL behind. Don't hand-edit it.

## Image resolution

⚠️ The four hero renders, the six advantage icons, the logo and the LVEA mark
are all **below retina resolution** — measured displayed size against intrinsic
size at DPR 2. Worst is `render-offshore.webp` at 152x127 in a 356x200 box: 32%
of what a 2x screen needs, and upscaled even at 1x. There is no better source in
the repo — the original Figma exports were 720x361 canvases whose *subject* was
only 152x127, so the crop to bbox was lossless and nothing was thrown away.

Fixing it needs fresh exports:

| Asset | Have | Export as |
|---|---|---|
| 4 direction renders | 152-324px | PNG ~1000x600, transparent |
| logo, LVEA, 6 icons | 53-280px | SVG (vector in Figma) |
| DNV certificate | 300x424 | rescan ~1200px tall |

Already at or above retina, leave alone: all five team photos, `news-2`,
`news-3`, `photo-welding`.

## Careers form

Rebuilt from the client's mock in `02_Makety/careers-page.html`. Four steps,
chip pickers for discipline / certificates / rotation / countries, six required
fields, and a GDPR consent naming a 24-month retention that `privacy.html`
section 3a now actually states.

**The drop zone is always there. Where the files go depends on
`CAREERS_ENDPOINT`:**

| | |
|---|---|
| endpoint set | the form posts as `multipart/form-data` with the files attached |
| endpoint empty | `mailto:` opens and the note names the exact files to attach |

GitHub Pages cannot receive a file, and `mailto:` cannot carry an attachment.
So with no endpoint the drop zone still earns its place: it checks the size,
rejects duplicates, and tells the applicant precisely which files to attach —
"Your mail app opened — now attach: cv.pdf, irata-l2.jpg", and the same list
goes in the email body. **What it never does is accept a file and quietly lose
it.**

Verified both ways: with a stubbed endpoint, `POST multipart/form-data` with
all eleven fields and both attachments, then form, chips and file list reset;
without one, an 11 MB file refused by name, a duplicate ignored, removal
working, and the file names reaching both the note and the email.

To switch it on you need a form service that accepts file uploads — Formspree
(paid), Basin, Netlify Forms, or a small serverless function. **This is the one
hosting decision left on this site.**

The honeypot field is positioned off-screen rather than `display:none`, so a
bot that filters on `display` still fills it in. Submissions with it filled are
dropped silently.


## Languages

English at the root; French, German and Italian each get their own directory
of real static pages. No client-side switching: these are industrial buyers
arriving from search, and a page that is English until JavaScript rewrites it
is a page Google indexes in English.

```
python3 tools/build-pages.py && python3 tools/i18n_build.py
```

| file | what it is |
|---|---|
| `tools/i18n_extract.py` | reads the **built** site and lists every translatable unit |
| `tools/i18n.py` | languages, locales, and `PUBLISH` |
| `tools/lang_{fr,de,it}.py` | the strings, one file per language |
| `tools/i18n_build.py` | builds the language trees from the English output |
| `tools/paths.py` | path rewriting both builds share |

**A language ships only at 100% coverage.** Below that it is not written, not
linked, not in the sitemap, and any stale tree is deleted. Coverage is
measured against the built HTML, so it cannot drift from what shipped. After
editing copy, re-run the build: any new or changed English string appears as
missing, and that language stops shipping until it is translated. That is the
intended behaviour, not a failure.

The unit of translation is an element's inner HTML, inline tags included, not
a text node — German puts words in a different order and a translator working
on fragments cannot move them. The build rejects a translation that does not
carry the same tags as its source. Links keep English paths in the language
files; the build prefixes them, so no translation can hard-code `/de/`.

`js/main.js` takes its language from `<html lang>` and carries the ~14 strings
it writes at runtime in all four languages.

⚠️ **The translations need a native review before go-live.** The trade
vocabulary is the part that matters — welding processes, NDT methods,
certification scopes and the inspection-independence wording are terms of art
in each market, and one wrong term is a credibility problem with exactly the
buyers this site is for. Terminology notes are at the top of each language
file. The privacy policy is a legal text and should be reviewed by whoever
signs it off.

To add a language: add it to `LANGS`, `LOCALE`, `LABEL`, `LANG_NAME` and
`LANG_GROUP` in `tools/i18n.py`, create `tools/lang_xx.py`, and run the build
to get the list of what is missing.


## TODO before go-live (client input needed)

- [x] **Calendly** — `BOOKING_URL` is set to
      `https://calendly.com/aleksandr-alprojects/30min`. It drives both the header
      "Book a call" button and the calendar panel on `/contacts.html`.

      The header button opens Calendly's **popup** over the page
      (`Calendly.initPopupWidget`), so nobody leaves the tab; the contacts panel
      uses the inline widget, since there is nothing behind it to return to.
      Both share one loader. Same pattern as the litprofit repo.

      **The calendar is click-to-load and must stay that way.** Calendly's embed
      sets cookies and sees the visitor's IP, so loading it on every page view
      would put the site into consent-banner territory. Nothing is requested from
      `calendly.com` until the visitor presses the button — verified: 0 requests
      before the click, 17 after. Section 3 of `privacy.html` discloses Calendly
      on exactly those terms, so if the embed is ever changed to load
      automatically, that section has to be rewritten and a consent banner added.

      The buttons stay plain `href` links to Calendly with no `target`, so they
      work with JavaScript off, with the script blocked, and on cmd-click. If the
      fetch fails the original link is followed instead — nothing is ever
      trapped behind a script that did not load.
- [x] **Company social links** — LinkedIn, Instagram and Facebook are wired up,
      taken from the Wayback snapshot of the old alprojects.eu (which is now a
      "coming soon" placeholder). The design's X/Twitter slot became Facebook,
      as no X account exists.
- [ ] **Team member links** — `MEMBER_SOCIAL` is still blank, so the per-person
      Instagram/LinkedIn icons stay hidden. A likely match for Aleksandr is
      linkedin.com/in/aleksandr-vasiljev-067549aa (listed as ALprojects Norge
      AS) — unconfirmed, so not wired in.
- [ ] **Project bases figure** — the footprint now lists six countries and nine
      locations (Norway 2, UK 1, Netherlands 1, Germany 3, Lithuania HQ,
      Belgium 1), so the counters read 6 / 9. The previous 5 / 7 was the same
      arithmetic with the Netherlands counted as an offshore area rather than a
      base. ⚠️ Confirm 9 is how the client counts a "project base".
- [ ] **Which countries have offices** — ⚠️ the two pages disagree. The homepage
      footprint says offices in **Lithuania, Poland, Germany and Norway**; the
      Company page says head office in Klaipėda with operations in **Belgium and
      Norway**. Both came from client material and both are still on the site.
      Poland and Germany against Belgium is not a wording difference — confirm
      the real list and make the two match.
- [ ] **Second phone number** — the old site also listed +370 670 20654 next to
      +370 636 63744. Only the latter is on the new site.
- [ ] **Newsletter backend** — set `FORM_ENDPOINT` (Formspree, Buttondown,
      Mailerlite…). Without it the form opens the visitor's mail app with a
      pre-filled request to info@alprojects.eu.
- [ ] **Clients** — the "Trusted by industry leaders" section was removed at
      the client's request (22 Aug 2026). The ten names the Company Profile
      lists — Smulders, MEYER Turku, Neptune Werft, Petrofac, Axess Group,
      BLRT Group, Seafox, GE Renewable Energy, Vattenfall, TenneT — are no
      longer anywhere on the site. ⚠️ That is the strongest third-party proof
      the company has; worth re-proposing as a single line under the hero
      rather than a full section. Logos would need each client's permission.
- [ ] **Certificates** — the 9001 card shows the real DNV scan. The 14001 and
      45001 cards previously showed that *same* scan under a different label,
      which presented evidence the artwork did not support; they are now
      typographic plates that state the certification without a document image.
      Send the real 14001 / 45001 scans and they become normal cards again —
      the markup to copy is the 9001 card directly above them in `index.html`.
- [x] **News photography** — the stock images are gone; each article now
      carries a real photograph matched to what the article actually claims.
- [ ] **News articles** — six articles. The first three follow ALprojects Group's
      own LinkedIn carousels closely (client-supplied screenshots): the NDT /
      "we do not certify our own welds" post, the engine-room piping post, and the
      Strongest in Lithuania award. The last three came from post summaries and
      are less exact. ⚠️ **Dates**: LinkedIn reports posts relatively ("2d", "1w"),
      so those are derived from 15 Aug 2026 — verify. The award date (23 June 2026)
      is the certificate's own and is solid. ⚠️ **Photos** are reused stock from
      the original design and do not depict the work described — swap in the real
      carousel images when you have the files.
- [ ] **Award artwork** — the Strongest in Lithuania badge is rendered
      typographically because the image file wasn't supplied. Drop in the badge
      and I'll use it.
- [x] **Privacy Policy** — `privacy.html` is live and linked from the footer.
      ⚠️ Written from what the site technically does; **not reviewed by a
      lawyer** — have it checked against your internal processes.
- [x] **Careers** — `careers.html` has an open-positions list and an application
      form. Positions are edited in `POSITIONS` (see Configuration above).
- [ ] **Application form backend** — set `CAREERS_ENDPOINT` in `js/main.js`.
      Until then the form validates in the browser and hands off to the
      applicant's mail client with every field pre-filled, so the CV can be
      attached there. **A static site cannot accept file uploads** — if you want
      CVs submitted through the page rather than by email, that needs a form
      service (Formspree, Netlify Forms) or a small backend.
- [x] **Company documents** — both presentations are downloadable from the
      homepage (`#downloads`) with rendered covers, page count, format and size.
- [x] **Certificate PDFs** — the real DNV certificates for ISO 9001 (C760290),
      14001 (C550875) and 45001 (C550877) arrived 22 Aug 2026 and are live in
      `assets/certificates/`. Each card shows the scan, its number and expiry,
      and opens the PDF.
- [ ] **Rope access slide photograph** — ⚠️ the fifth slide on the home page is
      running a **stand-in**. The frame ALDY chose (technician on rope under an
      offshore deck, grey sea) was pasted into chat and never reached the disk.
      `assets/svc-rope-access.webp` is currently cut from the Company page's
      offshore frame, and it is only 928px wide against a slide that renders at
      1280 — soft, and the third use of that same photograph on the site. Drop
      the real file anywhere and it is a one-file swap.
- [ ] **VCA** — ⚠️ **no certificate supplied.** The mark is on the site as a
      fourth card, added at the client's request. What was provided is EBN
      Certification's own logo — no company name, no certificate number, no
      validity dates — so the card deliberately shows only `VCA / EBN
      Certification` and is **not** a link. Fill `VCA_URL` and `VCA_META` in
      `js/main.js` and it becomes a linked card with a number and a date like
      the three DNV ones. Two things to get from the client:
      the certificate PDF, and **which level** — VCA\*, VCA\*\* and VCA-P are
      separate certifications for different scopes, and the artwork listed all
      three because that is the certifying body's scheme list, not the holder's.
- [ ] **ISO 3834** — ⚠️ **no certificate supplied.** The company profile lists
      it and three pages state welding is carried out under ISO 3834, but it was
      not among the three DNV certificates. Its card has been removed rather
      than shown as a placeholder beside three real scans. Get the document, or
      the claim is unevidenced if a tender asks.
- [ ] **Registered address** — the street type is settled: **Šilutės pl.**
      (not `av.`), confirmed by both the DNV certificates and the client's own
      TZ part 6 mockup footer, and corrected across the site. ⚠️ The office
      number is still open — the certificates read **521 kab.**, the site and
      the client's mockup both read **2-536**. The certificate is the legal
      document, so confirm which one belongs in the footer and the JSON-LD.
- [ ] **Team section** — ⚠️ the client struck the five management headshots out.
      That block is now "Qualified specialists" (the profile's own personnel
      split and 100+ figure). If the intent was only "fix the photo quality",
      the previous block is in git at `abaec6e` and restores cleanly.
- [ ] **Analytics** — decide whether you want visitor stats. If yes, register at
      plausible.io, set `ANALYTICS_DOMAIN`, and update the privacy policy as
      described under Configuration.
- [ ] Contact email is `info@alprojects.eu` while the site is on alprojects.co —
      intentional, .eu redirects to .co.

### /company.html — the six confirmations TZ part 6 §6 asks for

TZ part 6 was specified as a separate `/this-is-alprojects` page. It is instead
the Company page: the old prose `/company.html` and the TZ's vision / values /
HSEQ material were the same subject told twice, and one page carries it better
than two competing for the same visitor. Six of its statements are commitments
rather than descriptions, and the TZ itself says they must be confirmed before
publication:

- [ ] **"Anyone on our crew can stop a job."** This is Stop Work Authority. It is
      only publishable if a written procedure exists that says so and protects
      the person who uses it. If there is no procedure, the sentence has to go —
      a client will test it on site.
- [ ] **"When the mistake is ours, we say so and we correct it at our cost."**
      A commercial commitment. Confirm it does not contradict the liability and
      rework clauses in the standard contract.
- [ ] **"We answer enquiries that arrive at short notice"** — the TZ's draft said
      one working day. Confirm the company can hold that, or the line changes.
- [ ] **"We publish our safety figures once a year: hours worked, incidents, and
      what we changed as a result."** Nothing has been published yet. Either the
      first set gets published, or this promise is dated the moment a client
      looks for it.
- [ ] **Three hundred specialists** — the headline figure on this page. Elsewhere
      the site says 300+. Confirm the number and keep the two in step.
- [ ] **"Meet the management" button** — the Company page has the slot wired but the
      button is removed while `MANAGEMENT_URL` is blank (see Configuration). It
      switches on the moment there is a page to point it at; names and photos
      are still needed.
- [ ] **ISO 3834 on the Company page** — the HSEQ block shows four ISO plates, matching
      the rest of the site. The sentence above them now names the three
      management-system standards separately from the welding one, so the page
      no longer claims four certified management systems. The underlying gap is
      unchanged: no ISO 3834 certificate has been supplied. See the ISO 3834
      item above.

## Local preview

No build step, but **use `tools/serve.py`, not `python3 -m http.server`**:

```
python3 tools/serve.py          # then open http://localhost:8899/
```

The site links to `/company`, not `/company.html`. GitHub Pages resolves that
itself — nested paths and the language trees included — but the plain
`http.server` does not, so every link on the site 404s and it looks as though
the build is broken. `tools/serve.py` adds the one rule the host applies
(extensionless → `.html`) and serves `404.html` with a real 404 status, so
what you see locally is what deploys.

### Why the links have no .html

Both spellings resolve on GitHub Pages, which is exactly why the canonical,
the `hreflang` set and `sitemap.xml` all name the extensionless one — otherwise
every page is reachable at two URLs and points search engines at the one
nothing links to. `404.html` keeps its extension: that filename is how GitHub
Pages finds the custom 404, and no browser ever requests `/404`.

`clean_urls()` in `tools/paths.py` does the rewriting, and both builds call it.
If you add a link by hand in `index.html`, write it either way — the build
normalises it on the next run.

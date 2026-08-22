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
var BOOKING_URL = "";               // header "Book a call" button
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

## TODO before go-live (client input needed)

- [ ] **Calendly** — set `BOOKING_URL`. Until then the button reads "Book a call"
      and scrolls to the contact section, which is a valid destination.
- [x] **Company social links** — LinkedIn, Instagram and Facebook are wired up,
      taken from the Wayback snapshot of the old alprojects.eu (which is now a
      "coming soon" placeholder). The design's X/Twitter slot became Facebook,
      as no X account exists.
- [ ] **Team member links** — `MEMBER_SOCIAL` is still blank, so the per-person
      Instagram/LinkedIn icons stay hidden. A likely match for Aleksandr is
      linkedin.com/in/aleksandr-vasiljev-067549aa (listed as ALprojects Norge
      AS) — unconfirmed, so not wired in.
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
- [ ] **Certificate PDFs** — still only one DNV scan (`assets/cert-dnv.webp`).
      The 14001 / 45001 / 3834 cards state the certification rather than showing
      artwork that does not evidence it. Send the real scans and they drop in.
- [ ] **Team section** — ⚠️ the client struck the five management headshots out.
      That block is now "Qualified specialists" (the profile's own personnel
      split and 100+ figure). If the intent was only "fix the photo quality",
      the previous block is in git at `abaec6e` and restores cleanly.
- [ ] **Analytics** — decide whether you want visitor stats. If yes, register at
      plausible.io, set `ANALYTICS_DOMAIN`, and update the privacy policy as
      described under Configuration.
- [ ] Contact email is `info@alprojects.eu` while the site is on alprojects.co —
      intentional, .eu redirects to .co.

## Local preview

No build step. Any static server works:

```
python3 -m http.server 8080     # then open http://localhost:8080/
```

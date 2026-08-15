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
- `BLUE` and `BEIGE` were unused before. Beige is now the accent (eyebrow
  labels, lit loading-bar segments, the featured hero card's corner marks);
  blue tints the certifications panel glow.

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
```

**Open positions** live in `POSITIONS` at the top of `tools/build-pages.py` —
one dict per role. Set `open=False` to take a role off the live page without
deleting it; when none are open the page shows an "open applications welcome"
notice instead. Edit the list, run `python3 tools/build-pages.py`, commit.

⚠️ Only list roles the company is actually recruiting for. The one role
currently listed (30 certified TIG welders) comes from ALprojects Group's own
LinkedIn post and should be removed once it is filled.

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
- [ ] **Partner logos** — the design only contained LVEA. The auto-scrolling
      marquee (which repeated that one logo ten times) is gone; partners are now
      a static centred grid that looks right with 1, 3 or 8 logos. Add one
      `.partner-card` per real partner as they come in.
- [ ] **Certificates** — ⚠️ all three cards show the *same* DNV scan, and that
      scan reads ISO 9001, while the cards are labelled 9001 / 14001 / 45001.
      As published this claims certifications the artwork does not evidence.
      Swap in the real 14001 / 45001 scans, or drop those two cards.
- [ ] **News articles** — ⚠️ five articles written from ALprojects Group's own
      LinkedIn posts (retrieved 15 Aug 2026). **Dates are approximate** — LinkedIn
      reports posts as "2 days ago" / "3 weeks ago", not calendar dates — and the
      wording is ours, derived from those posts rather than quoted. Verify both
      before promoting the pages. Article photos are reused stock from the
      original design and do not depict the projects described.
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
- [ ] Contact email is `info@alprojects.eu` while the site is on alprojects.co —
      intentional, .eu redirects to .co.

## Local preview

No build step. Any static server works:

```
python3 -m http.server 8080     # then open http://localhost:8080/
```

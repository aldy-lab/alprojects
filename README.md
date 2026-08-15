# ALPROJECTS Group — website

Static site (HTML/CSS/JS, no build step). Built from the Figma design. Made by ALDY.

## Structure

```
index.html      — the whole homepage (all sections)
css/style.css   — design tokens + all styles, responsive down to mobile
js/main.js      — nav, reveals, counters, loadbars, team headline, newsletter
assets/         — optimized images extracted from the design (1.6 MB total)
```

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
var SOCIAL       = { instagram, linkedin, x };        // header + footer
var MEMBER_SOCIAL = { "aleksandr-vasiljev": {...}, … } // team cards
var FORM_ENDPOINT = "";             // newsletter POST target
```

## TODO before go-live (client input needed)

- [ ] **Calendly** — set `BOOKING_URL`. Until then the button reads "Book a call"
      and scrolls to the contact section, which is a valid destination.
- [ ] **Social links** — set `SOCIAL` / `MEMBER_SOCIAL`. Currently all blank, so
      the social rows are removed at runtime rather than linking nowhere.
- [ ] **Newsletter backend** — set `FORM_ENDPOINT` (Formspree, Buttondown,
      Mailerlite…). Without it the form opens the visitor's mail app with a
      pre-filled request to info@alprojects.eu.
- [ ] **Partner logos** — the design only contained LVEA; it is repeated in the
      marquee. Add real partner logos as more come in (`.partner-card` blocks).
- [ ] **Certificates** — ⚠️ all three cards show the *same* DNV scan, and that
      scan reads ISO 9001, while the cards are labelled 9001 / 14001 / 45001.
      As published this claims certifications the artwork does not evidence.
      Swap in the real 14001 / 45001 scans, or drop those two cards.
- [ ] **News articles** — cards link to `#news`; point them at real article
      pages when they exist. Cards 01 and 03 are currently the same headline
      and date with different photos.
- [ ] **Privacy Policy** — footer link points at `#contacts`; needs a real page
      (required if the newsletter starts collecting addresses in the EU).
- [ ] Nav "Careers" anchors to the team section (no careers page yet).
- [ ] Contact email is `info@alprojects.eu` while the site is on alprojects.co —
      intentional, .eu redirects to .co.

## Local preview

No build step. Any static server works:

```
python3 -m http.server 8080     # then open http://localhost:8080/
```

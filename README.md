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

## TODO before go-live (client input needed)

- [ ] **Calendly** — header button links to `https://calendly.com/` (placeholder).
      Replace with the client's real booking link.
- [ ] **Social links** — all Instagram / LinkedIn / X links are `#` placeholders
      (header, team cards, footer).
- [ ] **Newsletter backend** — currently opens the visitor's mail app with a
      pre-filled request to info@alprojects.eu. For a real endpoint (Formspree,
      Buttondown, Mailerlite…), set `FORM_ENDPOINT` at the top of `js/main.js`.
- [ ] **Partner logos** — the design only contained LVEA; it is repeated in the
      marquee. Add real partner logos as more come in (`.partner-card` blocks).
- [ ] **Certificates** — the same DNV scan is used for all three ISO cards
      (that's what was in the design). Swap in the real 14001 / 45001 scans.
- [ ] **News articles** — cards link to `#news`; point them at real article
      pages when they exist.
- [ ] The design had a typo "SHIPBULDING" — fixed to "Shipbuilding" on the site.
- [ ] Nav "Careers" currently anchors to the team section (no careers page yet).

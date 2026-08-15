#!/usr/bin/env python3
"""Renders a branded 1200x630 share image per page, using the real site font.
Run after changing a page title:  python3 tools/make-og.py"""
import os, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = [
    ("home",      "ALPROJECTS Group", "Integrated engineering for industry & offshore", "Klaipeda · Belgium · Norway"),
    ("company",   "Company",  "A European provider of industrial services", "ISO 3834 · 9001 · 14001 · 45001"),
    ("services",  "Services", "Integrated inspection & access services", "NDT · Rope access · QAQC"),
    ("projects",  "Projects", "Shipbuilding, offshore, industrial, renewable", "Northern & Western Europe"),
    ("contacts",  "Contacts", "Send us the scope and we will come back with a price", "info@alprojects.eu"),
    ("careers",   "Careers",  "Work with ALPROJECTS", "30 certified TIG welders wanted"),
    ("news",      "News",     "Project updates & engineering insights", "From the site, not the brochure"),
    ("we-do-not-certify-our-own-welds",  "Quality control", "We do not certify our own welds", "Internal QC · Independent NDT"),
    ("piping-installation-engine-room",  "Shipbuilding",    "Piping installation in the engine room", "Seawater · Bilge · Ballast · Fuel"),
    ("strongest-in-lithuania-2025-2026", "Company",         "Among the strongest companies in Lithuania", "Creditinfo · 2025–2026"),
]
out = ROOT / "assets" / "og"; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    pg.goto((ROOT / "tools" / "og-template.html").as_uri(), wait_until="load")
    pg.wait_for_timeout(600)
    for slug, eyebrow, title, tag in CARDS:
        pg.evaluate("""([e,t,g])=>{
            document.getElementById('eyebrow').textContent=e;
            const h=document.getElementById('title'); h.textContent=t;
            h.className = t.length>38 ? 'long' : '';
            document.getElementById('tag').textContent=g;
        }""", [eyebrow, title, tag])
        pg.wait_for_timeout(200)
        pg.screenshot(path=str(out / f"{slug}.jpg"), type="jpeg", quality=88)
        print("og:", slug, f"{(out / f'{slug}.jpg').stat().st_size//1024} KB")
    b.close()

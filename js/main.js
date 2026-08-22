/* ============================================================
   ALPROJECTS GROUP — main.js
   Interactions: header, mobile menu, scroll reveals, counters,
   loading bars, team headline highlight, newsletter form
   ============================================================ */
(function () {
  "use strict";

  /* ============================================================
     CONFIG — the only block that needs editing to go live.
     Fill in a URL to switch a link on; leave it "" and the link
     is removed from the page entirely, so nothing dead ships.
     ============================================================ */

  /* Header "Book a call" button, and the calendar panel on the contacts page.
     Falls back to /contacts.html, and hides the panel, while empty. */
  var BOOKING_URL = "https://calendly.com/aleksandr-alprojects/30min";

  /* Company profiles — used in the header and the footer. */
  var SOCIAL = {
    instagram: "https://www.instagram.com/alprojectsgroup",
    linkedin:  "https://www.linkedin.com/company/alprojects-group",
    facebook:  "https://www.facebook.com/alprojectsgroup"
  };

  /* Careers application form. Set to a Formspree/Netlify/etc endpoint to receive
     applications directly; while empty the form opens the applicant's mail client
     with everything pre-filled, so it works either way. */
  var CAREERS_ENDPOINT = ""; // e.g. "https://formspree.io/f/XXXXXXXX"

  /* Per-person profiles on the team cards. Keys match data-member in the HTML. */
  var MEMBER_SOCIAL = {
    "aleksandr-vasiljev": { instagram: "", linkedin: "" },
    "alex-stepanenko":    { instagram: "", linkedin: "" },
    "viktor-margus":      { instagram: "", linkedin: "" },
    "goda-budaviciute":   { instagram: "", linkedin: "" },
    "sergej-andrejev":    { instagram: "", linkedin: "" }
  };

  /* Cookieless analytics. Leave "" and no third-party request is made at all —
     nothing to disclose, no consent banner needed. Set it to the domain you
     registered with Plausible (self-hosted or plausible.io) to switch it on;
     if you do, add the disclosure paragraph to privacy.html — see README. */
  var ANALYTICS_DOMAIN = ""; // e.g. "alprojects.co"

  /* ---------- apply config ---------- */
  if (ANALYTICS_DOMAIN) {
    var an = document.createElement("script");
    an.defer = true;
    an.setAttribute("data-domain", ANALYTICS_DOMAIN);
    an.src = "https://plausible.io/js/script.js";
    document.head.appendChild(an);
  }

  /* there is a booking button in the header and another in the mobile menu */
  if (BOOKING_URL) {
    document.querySelectorAll("[data-booking]").forEach(function (b) {
      b.setAttribute("href", BOOKING_URL);
      b.setAttribute("target", "_blank");
      b.setAttribute("rel", "noopener");
    });
  }

  /* ---------- the calendar panel on /contacts.html ----------
     Click-to-load on purpose. Calendly's embed script sets cookies and sees the
     visitor's IP, so loading it on every page view would put the site into
     consent-banner territory. Nothing is requested from calendly.com until the
     visitor presses the button, which keeps the privacy story the same as the
     rest of the site. */
  var bookingPanel = document.querySelector("[data-booking-embed]");
  if (bookingPanel && BOOKING_URL) {
    bookingPanel.removeAttribute("hidden");
    var loadBtn = bookingPanel.querySelector("[data-booking-load]");
    var calendly = /(^|\.)calendly\.com$/i.test(
      (function () { try { return new URL(BOOKING_URL).hostname; } catch (e) { return ""; } })()
    );

    if (!calendly) {
      /* Not a Calendly link — send them straight out rather than embedding
         something we cannot style or vouch for. */
      loadBtn.parentNode.replaceChild((function () {
        var a = document.createElement("a");
        a.className = "btn-bracket";
        a.href = BOOKING_URL;
        a.target = "_blank"; a.rel = "noopener";
        a.textContent = "Open the calendar";
        return a;
      })(), loadBtn);
    } else if (loadBtn) {
      loadBtn.addEventListener("click", function () {
        loadBtn.disabled = true;
        loadBtn.textContent = "Loading\u2026";

        /* Calendly reads the theme off the query string, so the embed comes up
           in the site's palette instead of its own white default. */
        var url = BOOKING_URL +
          (BOOKING_URL.indexOf("?") === -1 ? "?" : "&") +
          "hide_gdpr_banner=1&background_color=0b0f16&text_color=e8eaf0&primary_color=ffffff";

        var mount = document.createElement("div");
        mount.className = "calendly-inline-widget booking-widget";
        mount.setAttribute("data-url", url);
        mount.setAttribute("data-resize", "true");

        var css = document.createElement("link");
        css.rel = "stylesheet";
        css.href = "https://assets.calendly.com/assets/external/widget.css";
        document.head.appendChild(css);

        var js = document.createElement("script");
        js.src = "https://assets.calendly.com/assets/external/widget.js";
        js.async = true;
        js.onerror = function () {
          /* Blocked by an extension or offline — never leave a dead panel. */
          bookingPanel.classList.remove("is-loaded");
          loadBtn.disabled = false;
          loadBtn.textContent = "Open the calendar";
          var msg = bookingPanel.querySelector(".booking-note");
          if (msg) {
            msg.innerHTML = "The calendar could not load. " +
              '<a href="' + BOOKING_URL + '" target="_blank" rel="noopener">' +
              "Open it in a new tab</a> instead.";
          }
        };

        bookingPanel.classList.add("is-loaded");
        bookingPanel.appendChild(mount);
        document.body.appendChild(js);
      });
    }
  }

  document.querySelectorAll("[data-social]").forEach(function (a) {
    var member = a.getAttribute("data-member");
    var set = member ? MEMBER_SOCIAL[member] || {} : SOCIAL;
    var url = set[a.getAttribute("data-social")];
    if (url) {
      a.setAttribute("href", url);
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener");
    } else {
      a.remove();
    }
  });

  /* Drop any socials row left empty, so the gap collapses cleanly. */
  document.querySelectorAll(".socials, .member .links").forEach(function (row) {
    if (!row.querySelector("a")) row.remove();
  });

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;


  /* ============================================================
     TECHNICAL DRAWING MOTIF
     Applies the grid + crosshair language from the design to the
     sections that can carry it, and reveals each as it scrolls in.
     Injected here so the generated sub-pages need no markup changes.
     ============================================================ */
  var GRID_SECTIONS = [
    ".hero", ".advantages", ".partners", ".team", ".people", ".footprint",
    ".downloads", ".certifications", ".news", ".cta", ".page-head", ".apply-panel"
  ];
  var CROSSHAIR_TARGETS = [
    ".certs-panel", ".cta-panel", ".apply-panel", ".hero-tags", ".position",
    ".doc-card", ".people-figure", ".shot-grid"
  ];
  /* Dimension callouts: a drawing rule with end caps and the measured width,
     the way a general arrangement drawing dimensions a run. The number is read
     off the live element, so it is a real measurement, not decoration. */
  /* Target only elements whose parent lays out in normal flow -- inserting the
     rule as a sibling inside a grid container would make it a grid item and
     push the real content into the wrong column. */
  var DIMENSION_TARGETS = [".footprint .fp-wrap", ".downloads .docs-grid",
                           ".people .people-grid", ".shot-grid"];

  function addDimension(el) {
    if (el.previousElementSibling && el.previousElementSibling.classList.contains("dim")) return;
    var d = document.createElement("span");
    d.className = "dim";
    d.setAttribute("aria-hidden", "true");
    d.innerHTML = '<i></i><s></s><b></b><s></s><i></i>';
    el.parentNode.insertBefore(d, el);
    return d;
  }

  var dims = [];
  DIMENSION_TARGETS.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      var d = addDimension(el);
      if (d) dims.push([d, el]);
    });
  });
  /* NB: named measureDimensions, not measure -- blueprint mode already
     declares a measure(), and the later declaration would win the hoist and
     silently leave every dimension label empty. */
  function measureDimensions() {
    dims.forEach(function (pair) {
      var w = Math.round(pair[1].getBoundingClientRect().width);
      if (w) pair[0].querySelector("b").textContent = w + " mm";
    });
  }
  measureDimensions();
  var mt;
  window.addEventListener("resize", function () {
    clearTimeout(mt); mt = setTimeout(measureDimensions, 160);
  });

  function addCrosshairs(el) {
    if (el.querySelector(":scope > .xhair")) return;
    if (getComputedStyle(el).position === "static") el.style.position = "relative";
    ["tl", "tr", "bl", "br"].forEach(function (corner) {
      var m = document.createElement("span");
      m.className = "xhair " + corner;
      m.setAttribute("aria-hidden", "true");
      el.appendChild(m);
    });
  }

  var gridEls = [];
  GRID_SECTIONS.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      /* .hero already paints its own grid — don't double it up */
      if (!el.classList.contains("hero")) el.classList.add("tech-grid");
      gridEls.push(el);
    });
  });
  CROSSHAIR_TARGETS.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(addCrosshairs);
  });

  if ("IntersectionObserver" in window && !reduceMotion) {
    var gio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("grid-in");
          gio.unobserve(e.target);
        }
      });
    }, { threshold: 0, rootMargin: "0px 0px -5% 0px" });
    gridEls.forEach(function (el) { gio.observe(el); });
  } else {
    gridEls.forEach(function (el) { el.classList.add("grid-in"); });
  }


  /* ---------- blueprint: the drawing sheet ----------
     Pressing B used to brighten the grid and label the cards. It now lays a
     real sheet over the viewport: frame, zone letters and numbers down the
     margins, registration marks and a title block that reads off the page it
     is actually on. Built once, on first use. */
  var sheet = null;
  function buildSheet() {
    if (sheet) return sheet;
    sheet = document.createElement("div");
    sheet.className = "bp-sheet";
    sheet.setAttribute("aria-hidden", "true");

    var frame = document.createElement("span");
    frame.className = "bp-frame";
    sheet.appendChild(frame);

    /* zones: 1..8 across, A..E down, as on a general arrangement sheet */
    var cols = 8, rows = 5, i;
    for (i = 1; i <= cols; i++) {
      ["top", "bottom"].forEach(function (side) {
        var z = document.createElement("span");
        z.className = "bp-zone bp-zone-" + side;
        z.style.left = ((i - 0.5) / cols * 100) + "%";
        z.textContent = i;
        sheet.appendChild(z);
      });
    }
    for (i = 0; i < rows; i++) {
      ["left", "right"].forEach(function (side) {
        var z = document.createElement("span");
        z.className = "bp-zone bp-zone-" + side;
        z.style.top = ((i + 0.5) / rows * 100) + "%";
        z.textContent = String.fromCharCode(65 + i);
        sheet.appendChild(z);
      });
    }

    var title = document.createElement("div");
    title.className = "bp-title";
    /* name the drawing after the page, not the company: on the homepage the
       title is just the company name, so fall back to the H1 and then to Home */
    var page = (document.title || "").split("—")[0].trim();
    if (!page || /^ALPROJECTS/i.test(page)) {
      var h1 = document.querySelector("h1");
      page = h1 ? h1.textContent.trim() : "Home";
    }
    if (page.length > 30) page = page.slice(0, 29).trim() + "…";
    var d = new Date();
    var stamp = d.getFullYear() + "." +
                ("0" + (d.getMonth() + 1)).slice(-2) + "." +
                ("0" + d.getDate()).slice(-2);
    title.innerHTML =
      '<b>ALPROJECTS GROUP</b>' +
      '<i><s>DRAWING</s><em>' + page + '</em></i>' +
      '<i><s>SCALE</s><em>1:1</em></i>' +
      '<i><s>UNITS</s><em>px</em></i>' +
      '<i><s>DATE</s><em>' + stamp + '</em></i>';
    sheet.appendChild(title);

    document.body.appendChild(sheet);
    return sheet;
  }

  /* ---------- hidden: blueprint mode ----------
     Press B to overlay the drafting sheet — grid everywhere, corner
     registration marks, and the real pixel size of each card, in the
     spirit of the "200x200" annotation in the design. Off by default,
     remembered for the tab only. Ignored while typing in a field. */
  var BLUEPRINT_KEY = "alp-blueprint";
  var flag = document.createElement("div");
  flag.className = "blueprint-flag";
  flag.setAttribute("role", "status");
  flag.setAttribute("aria-live", "polite");
  document.body.appendChild(flag);
  var flagTimer;

  function measure() {
    /* Kept in step with the markup: .dir-card, .member, .partner-card and
       .position no longer exist, and half the site's cards are new. */
    document.querySelectorAll(
      ".sector-card, .adv-card, .news-card, .cert-card, .doc-card, .shot, .fp-card"
    ).forEach(function (el) {
      var r = el.getBoundingClientRect();
      el.setAttribute("data-dim", Math.round(r.width) + "×" + Math.round(r.height));
    });
  }

  /* The hero's legend button — the only route into this on a phone. */
  var bpHint = document.querySelector(".bp-hint");
  var bpHintLabel = bpHint && bpHint.querySelector(".bp-hint-label");

  function setBlueprint(on, announce) {
    document.documentElement.classList.toggle("blueprint", on);
    if (bpHint) {
      bpHint.setAttribute("aria-pressed", on ? "true" : "false");
      if (bpHintLabel) bpHintLabel.textContent = on ? "Exit drawing mode" : "Drawing mode";
    }
    if (on) buildSheet();
    if (on) measure();
    try { sessionStorage.setItem(BLUEPRINT_KEY, on ? "1" : "0"); } catch (e) {}
    if (announce) {
      flag.textContent = on
        ? "Blueprint mode — drag to measure · B to exit"
        : "Blueprint mode off";
      flag.classList.add("show");
      clearTimeout(flagTimer);
      flagTimer = setTimeout(function () { flag.classList.remove("show"); }, 2600);
    }
  }

  try {
    if (sessionStorage.getItem(BLUEPRINT_KEY) === "1") setBlueprint(true, false);
  } catch (e) {}

  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "b" && ev.key !== "B") return;
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    var t = ev.target;
    if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" ||
              t.tagName === "SELECT" || t.isContentEditable)) return;
    setBlueprint(!document.documentElement.classList.contains("blueprint"), true);
  });

  if (bpHint) {
    bpHint.addEventListener("click", function () {
      setBlueprint(!document.documentElement.classList.contains("blueprint"), true);
      /* Keeping focus here would swallow the next B press into the button. */
      bpHint.blur();
    });
  }

  window.addEventListener("resize", function () {
    if (document.documentElement.classList.contains("blueprint")) measure();
  }, { passive: true });


  /* ---------- hidden, part two: drag to measure ----------
     Inside blueprint mode, dragging draws a dimension line with a live
     readout — the drafting tool the rest of the motif implies. Pointer
     events only, so it never interferes with touch scrolling or links. */
  var mLayer = document.createElement("div");
  mLayer.className = "measure-layer";
  mLayer.setAttribute("aria-hidden", "true");
  mLayer.innerHTML =
    '<span class="m-line"></span><span class="m-cap m-a"></span>' +
    '<span class="m-cap m-b"></span><span class="m-read"></span>';
  document.body.appendChild(mLayer);
  var mLine = mLayer.querySelector(".m-line"),
      mCapA = mLayer.querySelector(".m-a"),
      mCapB = mLayer.querySelector(".m-b"),
      mRead = mLayer.querySelector(".m-read"),
      mFrom = null, mFade;

  function drawMeasure(x, y) {
    var dx = x - mFrom.x, dy = y - mFrom.y;
    var len = Math.sqrt(dx * dx + dy * dy);
    var ang = Math.atan2(dy, dx) * 180 / Math.PI;
    mLine.style.transform =
      "translate(" + mFrom.x + "px," + mFrom.y + "px) rotate(" + ang + "deg)";
    mLine.style.width = len + "px";
    mCapA.style.transform =
      "translate(" + mFrom.x + "px," + mFrom.y + "px) rotate(" + ang + "deg)";
    mCapB.style.transform =
      "translate(" + x + "px," + y + "px) rotate(" + ang + "deg)";
    mRead.textContent = Math.round(len) + " px";
    mRead.style.transform =
      "translate(" + (mFrom.x + dx / 2) + "px," + (mFrom.y + dy / 2) + "px)";
  }

  function measuring() {
    return document.documentElement.classList.contains("blueprint");
  }

  document.addEventListener("pointerdown", function (ev) {
    if (!measuring() || ev.pointerType !== "mouse" || ev.button !== 0) return;
    /* ev.target can be a non-element (document, SVG in older engines) — guard
       before calling closest(), or the whole handler throws. */
    var t = ev.target;
    if (t && typeof t.closest === "function" &&
        t.closest("a, button, input, textarea, select, label")) return;
    ev.preventDefault();
    clearTimeout(mFade);
    mFrom = { x: ev.clientX, y: ev.clientY };
    mLayer.classList.add("on");
    drawMeasure(ev.clientX, ev.clientY);
  });

  document.addEventListener("pointermove", function (ev) {
    if (mFrom) drawMeasure(ev.clientX, ev.clientY);
  });

  function endMeasure() {
    if (!mFrom) return;
    mFrom = null;
    mFade = setTimeout(function () { mLayer.classList.remove("on"); }, 1800);
  }
  document.addEventListener("pointerup", endMeasure);
  document.addEventListener("pointercancel", endMeasure);
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") { mFrom = null; mLayer.classList.remove("on"); }
  });

  /* a note for whoever opens the console */
  if (window.console && console.log) {
    console.log(
      "%cALPROJECTS GROUP%c\nIntegrated engineering for industry & offshore." +
      "\nPress B for blueprint mode, then drag to measure.\nBuilt by ALDY — https://aldystudio.com",
      "font:600 14px/1.4 system-ui;letter-spacing:.14em",
      "font:12px/1.6 system-ui;color:#8e97ab"
    );
  }

  /* ---------- header state ---------- */
  var header = document.querySelector(".site-header");
  function onScrollHeader() {
    header.classList.toggle("scrolled", window.scrollY > 30);
  }
  window.addEventListener("scroll", onScrollHeader, { passive: true });
  onScrollHeader();

  /* ---------- footprint: map markers linked to the country rows ----------
     Both the map and the list already carry every country, so this only
     connects them; nothing is revealed by the interaction. */
  var euromap = document.querySelector(".euromap");
  var fpRows = document.querySelectorAll(".fp-row[data-country]");
  if (euromap && fpRows.length) {
    var setCountry = function (key, on) {
      var pin = euromap.querySelector('[data-pin="' + key + '"]');
      var row = document.querySelector('.fp-row[data-country="' + key + '"]');
      /* Not every country has a shape: Poland and Lithuania are a single
         shape in the source map, so Lithuania is marker-only. */
      var shape = euromap.querySelector('[data-shape="' + key + '"]');
      if (pin) pin.classList.toggle("is-active", on);
      if (row) row.classList.toggle("is-active", on);
      if (shape) shape.classList.toggle("is-active", on);
      euromap.classList.toggle("has-active", on);
    };
    var bind = function (el, key) {
      el.addEventListener("mouseenter", function () { setCountry(key, true); });
      el.addEventListener("mouseleave", function () { setCountry(key, false); });
      el.addEventListener("focus", function () { setCountry(key, true); });
      el.addEventListener("blur", function () { setCountry(key, false); });
    };
    fpRows.forEach(function (row) { bind(row, row.getAttribute("data-country")); });
    euromap.querySelectorAll("[data-pin]").forEach(function (pin) {
      bind(pin, pin.getAttribute("data-pin"));
    });
  }

  /* ---------- suppress hover motion while dragging ----------
     Sweeping the pointer across a row of cards fired each hover in turn, so
     the cards lifted and dropped one after another. That is read as blinking,
     not as hover, so the motion stands down until the pointer is released. */
  var dragDoc = document.documentElement;
  document.addEventListener("pointerdown", function (ev) {
    if (ev.pointerType === "mouse" && ev.button === 0) dragDoc.classList.add("dragging");
  }, true);
  ["pointerup", "pointercancel", "blur"].forEach(function (evt) {
    window.addEventListener(evt, function () { dragDoc.classList.remove("dragging"); }, true);
  });
  /* Belt and braces for engines that ignore -webkit-user-drag: without this the
     native drag fires pointercancel mid-sweep and the suppression is dropped
     exactly when it is needed. */
  document.addEventListener("dragstart", function (ev) {
    var t = ev.target;
    if (t && typeof t.closest === "function" &&
        t.closest(".dir-card, .news-card, .shot, .doc-cover, .member")) ev.preventDefault();
  });

  /* ---------- services: switch without a reload ----------
     Every service has a real URL and a real page, so this works with JS off
     and the links are ordinary links. With JS on, the panel is re-rendered
     from the embedded JSON and the URL is updated, so switching is instant
     and the address bar still points at something you can send to someone. */
  var srvData = document.getElementById("srv-data");
  var srvPanel = document.querySelector(".srv-panel");
  if (srvData && srvPanel) {
    var services = [];
    try { services = JSON.parse(srvData.textContent); } catch (e) { services = []; }
    var indexOfSlug = function (slug) {
      for (var i = 0; i < services.length; i++) if (services[i].slug === slug) return i;
      return -1;
    };
    var currentSlug = function () {
      var a = document.querySelector(".srv-link.is-active");
      return a ? a.getAttribute("data-service") : (services[0] && services[0].slug);
    };

    var renderService = function (slug, push) {
      var i = indexOfSlug(slug);
      if (i < 0) return;
      var sv = services[i];
      var art = srvPanel.querySelector(".srv-item");
      if (!art) return;

      art.setAttribute("data-panel", sv.slug);
      /* restart the entrance animation on every switch */
      art.classList.remove("is-switching");
      void art.offsetWidth;
      art.classList.add("is-switching");
      art.querySelector(".srv-count").textContent = sv.num + " / 12";
      art.querySelector(".srv-title").textContent = sv.h1;
      art.querySelector(".srv-lead").innerHTML = sv.lead;
      var ul = art.querySelector(".srv-points");
      ul.innerHTML = "";
      sv.points.forEach(function (p) {
        var li = document.createElement("li");
        li.innerHTML = p;
        ul.appendChild(li);
      });
      var pos = srvPanel.querySelector(".srv-pos");
      if (pos) pos.textContent = sv.num + " / 12";

      document.querySelectorAll(".srv-link").forEach(function (a) {
        var on = a.getAttribute("data-service") === sv.slug;
        a.classList.toggle("is-active", on);
        if (on) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      });

      document.title = sv.h1 + " — ALPROJECTS Group";
      if (push && window.history && history.pushState) {
        history.pushState({ srv: sv.slug }, "", "/services/" + sv.slug + ".html");
      }
      /* the panel is what changed, so that is what should be announced */
      art.setAttribute("tabindex", "-1");
      if (push) {
        art.focus({ preventScroll: true });
        /* stacked on a phone the panel sits below twelve list items, so a tap
           would otherwise look like nothing happened */
        if (window.matchMedia("(max-width: 900px)").matches) {
          art.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
        }
      }
    };

    document.querySelectorAll(".srv-link").forEach(function (a) {
      a.addEventListener("click", function (ev) {
        if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button !== 0) return;
        ev.preventDefault();
        renderService(a.getAttribute("data-service"), true);
      });
    });

    var step = function (delta) {
      var i = indexOfSlug(currentSlug());
      if (i < 0) return;
      var next = (i + delta + services.length) % services.length;
      renderService(services[next].slug, true);
    };
    var prev = srvPanel.querySelector("[data-srv-prev]");
    var next = srvPanel.querySelector("[data-srv-next]");
    if (prev) prev.addEventListener("click", function () { step(-1); });
    if (next) next.addEventListener("click", function () { step(1); });

    document.addEventListener("keydown", function (ev) {
      if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
      var t = ev.target;
      if (t && /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
      if (ev.key === "ArrowLeft") step(-1);
      else if (ev.key === "ArrowRight") step(1);
    });

    window.addEventListener("popstate", function () {
      var m = location.pathname.match(/\/services\/([a-z0-9-]+)\.html$/);
      renderService(m ? m[1] : services[0].slug, false);
    });
  }

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector(".burger");
  var mobileMenu = document.getElementById("mobileMenu");
  if (burger && mobileMenu) {
    var setMenu = function (open) {
      mobileMenu.classList.toggle("open", open);
      burger.classList.toggle("open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
      if (open) {
        /* Move focus into the panel, otherwise a keyboard user opens the menu
           and their focus is still behind it on the page. */
        var first = mobileMenu.querySelector("a, button");
        if (first) first.focus();
      } else {
        burger.focus();
      }
    };
    var isOpen = function () { return mobileMenu.classList.contains("open"); };

    burger.addEventListener("click", function () { setMenu(!isOpen()); });
    mobileMenu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        /* Navigating away: close without stealing focus back to the burger. */
        mobileMenu.classList.remove("open");
        burger.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });

    document.addEventListener("keydown", function (ev) {
      if (!isOpen()) return;
      if (ev.key === "Escape") { ev.preventDefault(); setMenu(false); return; }
      if (ev.key !== "Tab") return;
      /* Keep Tab inside the open panel — without this the focus ring walks off
         behind the overlay and the visitor cannot see where they are. */
      var items = Array.prototype.slice
        .call(mobileMenu.querySelectorAll('a[href], button:not([disabled])'))
        .filter(function (el) { return el.offsetParent !== null; });
      items.unshift(burger);
      if (!items.length) return;
      var firstEl = items[0], lastEl = items[items.length - 1];
      if (ev.shiftKey && document.activeElement === firstEl) {
        ev.preventDefault(); lastEl.focus();
      } else if (!ev.shiftKey && document.activeElement === lastEl) {
        ev.preventDefault(); firstEl.focus();
      }
    });
  }

  /* ---------- active nav link by section ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".main-nav a"));
  var sectionsForNav = ["top", "company", "services", "projects", "team", "contacts", "news"]
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);

  function setActiveNav() {
    var y = window.scrollY + window.innerHeight * 0.35;
    var currentId = "top";
    var bestTop = -Infinity;
    sectionsForNav.forEach(function (sec) {
      var top = sec.getBoundingClientRect().top + window.scrollY;
      if (top <= y && top > bestTop) {
        bestTop = top;
        currentId = sec.id;
      }
    });
    navLinks.forEach(function (a) {
      a.classList.toggle("active", a.getAttribute("href") === "#" + currentId);
    });
  }
  window.addEventListener("scroll", setActiveNav, { passive: true });
  setActiveNav();

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0, rootMargin: "0px 0px -10% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- stat counters ---------- */
  var counters = document.querySelectorAll("[data-count]");
  function animateCounter(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduceMotion) { el.textContent = target + suffix; return; }
    var dur = 1400;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          animateCounter(e.target);
          cio.unobserve(e.target);
        }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(animateCounter);
  }

  /* ---------- segmented loading bars ---------- */
  /* Fills, holds, empties, holds, repeats -- a continuous cycle rather than
     filling and snapping back to the start, which was the part that read as
     flashing. Pauses while the tab is hidden so it is not burning frames in
     the background. */
  function runLoadbar(id, interval) {
    var bar = document.getElementById(id);
    if (!bar) return;
    var segs = bar.querySelectorAll("i");
    if (!segs.length) return;
    if (reduceMotion) {
      segs.forEach(function (s) { s.classList.add("on"); });
      return;
    }
    var pos = 0, dir = 1, timer = null;
    var paint = function () { segs.forEach(function (s, i) { s.classList.toggle("on", i < pos); }); };
    var step = function () {
      pos += dir;
      if (pos >= segs.length) { pos = segs.length; dir = -1; hold(900); }
      else if (pos <= 0)      { pos = 0;           dir = 1;  hold(500); }
      paint();
    };
    var hold = function (ms) {
      clearInterval(timer);
      setTimeout(function () { timer = setInterval(step, interval); }, ms);
    };
    var start = function () { clearInterval(timer); timer = setInterval(step, interval); };
    var stop  = function () { clearInterval(timer); };
    paint();
    start();
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) stop(); else start();
    });
  }

  runLoadbar("heroLoadbar", 420);
  runLoadbar("ctaLoadbar", 240);

  /* ---------- team headline: words light up on scroll ---------- */
  var headline = document.getElementById("teamHeadline");
  if (headline) {
    var words = headline.textContent.trim().split(/\s+/);
    headline.innerHTML = words
      .map(function (w) { return '<span class="w">' + w + "</span>"; })
      .join(" ");
    var wordEls = headline.querySelectorAll(".w");

    if (reduceMotion) {
      wordEls.forEach(function (w) { w.classList.add("lit"); });
    } else {
      function updateHeadline() {
        var rect = headline.getBoundingClientRect();
        var vh = window.innerHeight;
        /* progress: 0 when headline enters lower third, 1 when its bottom passes mid-screen */
        var startAt = vh * 0.85;
        var endAt = vh * 0.35;
        var progress = (startAt - rect.top) / (startAt - endAt);
        progress = Math.max(0, Math.min(1, progress));
        var litCount = Math.round(progress * wordEls.length);
        wordEls.forEach(function (w, i) {
          w.classList.toggle("lit", i < litCount);
        });
      }
      window.addEventListener("scroll", updateHeadline, { passive: true });
      window.addEventListener("resize", updateHeadline);
      updateHeadline();
    }
  }

  /* ---------- careers application form ---------- */
  var applyForm = document.getElementById("applyForm");
  if (applyForm) {
    var applyNote = document.getElementById("applyNote");
    var roleSelect = document.getElementById("apRole");

    /* "Apply for this role" preselects that position and moves focus into the form */
    document.querySelectorAll("[data-apply]").forEach(function (a) {
      a.addEventListener("click", function () {
        var role = a.getAttribute("data-apply");
        if (roleSelect) {
          Array.prototype.forEach.call(roleSelect.options, function (o) {
            if (o.value === role) roleSelect.value = role;
          });
        }
        var first = document.getElementById("apName");
        if (first) setTimeout(function () { first.focus(); }, 400);
      });
    });

    applyForm.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var f = applyForm;
      var data = {
        name: f.name.value.trim(),
        email: f.email.value.trim(),
        phone: f.phone.value.trim(),
        role: f.role.value,
        certifications: f.certifications.value.trim(),
        message: f.message.value.trim()
      };

      function fail(msg, field) {
        applyNote.textContent = msg;
        applyNote.classList.add("show", "is-error");
        if (field) field.focus();
      }
      applyNote.classList.remove("is-error");

      if (!data.name) return fail("Please enter your name.", f.name);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email))
        return fail("Please enter a valid email address.", f.email);
      if (!data.message) return fail("Please describe your experience and availability.", f.message);
      if (!f.consent.checked) return fail("Please confirm the privacy notice to continue.", f.consent);

      if (CAREERS_ENDPOINT) {
        applyNote.textContent = "Sending…";
        applyNote.classList.add("show");
        fetch(CAREERS_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(data)
        })
          .then(function (r) {
            if (r.ok) {
              applyNote.textContent = "Application sent. We will be in touch.";
              f.reset();
            } else {
              fail("Could not send. Please email info@alprojects.eu instead.");
            }
          })
          .catch(function () {
            fail("Could not send. Please email info@alprojects.eu instead.");
          });
        return;
      }

      /* No endpoint configured: hand off to the applicant's mail client with a
         pre-filled message, so the CV can be attached there. */
      var body = [
        "Position: " + data.role,
        "Name: " + data.name,
        "Email: " + data.email,
        "Phone: " + (data.phone || "—"),
        "Certifications: " + (data.certifications || "—"),
        "",
        "Experience and availability:",
        data.message,
        "",
        "(Please attach your CV and certificates to this email.)"
      ].join("\n");
      window.location.href =
        "mailto:info@alprojects.eu?subject=" +
        encodeURIComponent("Application — " + data.role) +
        "&body=" + encodeURIComponent(body);
      applyNote.textContent =
        "Your mail app opened with the details filled in — attach your CV and send.";
      applyNote.classList.add("show");
    });
  }

  /* ---------- newsletter (no backend: opens mail client) ----------
     To wire a real endpoint later (e.g. Formspree/Buttondown), set
     FORM_ENDPOINT to the URL and the form will POST instead.       */
  var FORM_ENDPOINT = ""; // e.g. "https://formspree.io/f/XXXXXXXX"
  var form = document.getElementById("newsletterForm");
  var note = document.getElementById("formNote");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var email = form.email.value.trim();
      var valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
      if (!valid) {
        note.textContent = "Enter a valid email address to subscribe.";
        note.classList.add("show");
        return;
      }
      if (FORM_ENDPOINT) {
        fetch(FORM_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify({ email: email })
        })
          .then(function (r) {
            note.textContent = r.ok
              ? "Subscribed. You will receive our next update."
              : "Subscription failed. Email us at info@alprojects.eu.";
            note.classList.add("show");
            if (r.ok) form.reset();
          })
          .catch(function () {
            note.textContent = "Subscription failed. Email us at info@alprojects.eu.";
            note.classList.add("show");
          });
      } else {
        window.location.href =
          "mailto:info@alprojects.eu?subject=" +
          encodeURIComponent("Newsletter subscription") +
          "&body=" +
          encodeURIComponent("Please subscribe this address to company updates: " + email);
        note.textContent = "Your mail app opened with a pre-filled subscription request.";
        note.classList.add("show");
      }
    });
  }
})();

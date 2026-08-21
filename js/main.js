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

  /* Header "Book a call" button. Falls back to /contacts.html while empty. */
  var BOOKING_URL = ""; // e.g. "https://calendly.com/alprojects/30min"

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
    }, { threshold: 0.05 });
    gridEls.forEach(function (el) { gio.observe(el); });
  } else {
    gridEls.forEach(function (el) { el.classList.add("grid-in"); });
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
    document.querySelectorAll(
      ".dir-card, .adv-card, .member, .news-card, .partner-card, .cert-card"
    ).forEach(function (el) {
      var r = el.getBoundingClientRect();
      el.setAttribute("data-dim", Math.round(r.width) + "×" + Math.round(r.height));
    });
  }

  function setBlueprint(on, announce) {
    document.documentElement.classList.toggle("blueprint", on);
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

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector(".burger");
  var mobileMenu = document.getElementById("mobileMenu");
  if (burger && mobileMenu) {
    burger.addEventListener("click", function () {
      var open = mobileMenu.classList.toggle("open");
      burger.classList.toggle("open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    mobileMenu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        mobileMenu.classList.remove("open");
        burger.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
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
    }, { threshold: 0.12 });
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
  function runLoadbar(id, interval) {
    var bar = document.getElementById(id);
    if (!bar || reduceMotion) return;
    var segs = bar.querySelectorAll("i");
    var lit = 0;
    segs.forEach(function (s, i) { if (s.classList.contains("on")) lit = Math.max(lit, i + 1); });
    var base = lit || 1;
    var pos = base;
    setInterval(function () {
      pos += 1;
      if (pos > segs.length) pos = base;
      segs.forEach(function (s, i) { s.classList.toggle("on", i < pos); });
    }, interval);
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

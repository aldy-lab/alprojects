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

  /* Header "Book a call" button. Falls back to #contacts while empty. */
  var BOOKING_URL = ""; // e.g. "https://calendly.com/alprojects/30min"

  /* Company profiles — used in the header and the footer. */
  var SOCIAL = {
    instagram: "",
    linkedin: "",
    x: ""
  };

  /* Per-person profiles on the team cards. Keys match data-member in the HTML. */
  var MEMBER_SOCIAL = {
    "aleksandr-vasiljev": { instagram: "", linkedin: "" },
    "alex-stepanenko":    { instagram: "", linkedin: "" },
    "viktor-margus":      { instagram: "", linkedin: "" },
    "goda-budaviciute":   { instagram: "", linkedin: "" },
    "sergej-andrejev":    { instagram: "", linkedin: "" }
  };

  /* ---------- apply config ---------- */
  var booking = document.querySelector("[data-booking]");
  if (booking && BOOKING_URL) {
    booking.setAttribute("href", BOOKING_URL);
    booking.setAttribute("target", "_blank");
    booking.setAttribute("rel", "noopener");
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

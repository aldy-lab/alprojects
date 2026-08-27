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
  /* Contact form on /contacts.html. Empty -> the form opens the visitor's
     mail client with every answer filled in, so an enquiry is never lost
     to a POST that goes nowhere. */
  var CONTACT_ENDPOINT = ""; // e.g. "https://formspree.io/f/XXXXXXXX"
  /* "Meet the management" on /company.html. There is no such page
     yet and no names or photographs for one, so the button stays out of the
     DOM until this points somewhere real. */
  var MANAGEMENT_URL = "";
  /* VCA. The mark is on the site; the certificate is not. Fill these two in and
     the card becomes a link with a number and a validity date like the three DNV
     ones. Leave them empty and it stays a plain tile that claims nothing beyond
     the mark itself. */
  var VCA_URL = "";   // e.g. "/assets/certificates/alprojects-vca.pdf"
  var VCA_META = "";  // e.g. "Cert. 12345|Valid to 01.03.2028"

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

  /* ============================================================
     LANGUAGE
     <html lang> is set per tree by tools/i18n_build.py. PREFIX comes from it
     too, because pushState below writes a path: without the prefix a French
     visitor clicking a service would be silently moved to the English URL.
     Strings here are the ones JavaScript writes; everything in the HTML is
     translated at build time.
     ============================================================ */
  var LANG = (document.documentElement.lang || "en").slice(0, 2).toLowerCase();
  var PREFIX = ["fr", "de", "it"].indexOf(LANG) >= 0 ? "/" + LANG : "";

  var TXT = (function () {
    var T = {};
    T.en = {
      cal_open: "Open the calendar", cal_loading: "Loading\u2026",
      cal_failed: 'The calendar could not load. <a href="%s" target="_blank" rel="noopener">Open it in a new tab</a> instead.',
      home: "Home", title_suffix: " \u2014 ALPROJECTS Group",
      bp_on: "Exit drawing mode", bp_off: "Drawing mode",
      bp_flag_on: "Blueprint mode \u2014 drag to measure \u00b7 B to exit",
      bp_flag_off: "Blueprint mode off",
      apply_sending: "Sending\u2026",
      apply_sent: "Application sent. We will be in touch.",
      apply_fail: "Could not send. Please email info@alprojects.eu instead.",
      sub_invalid: "Enter a valid email address to subscribe.",
      sub_consent: "Please tick the consent box before subscribing.",
      sub_fail: "Subscription failed. Email us at info@alprojects.eu.",
      sub_mail: "Your mail app opened with a pre-filled subscription request.",
      need_name: "Please enter your name.",
      need_email: "Please enter a valid email address.",
      need_phone: "Please enter a phone or WhatsApp number.",
      need_role: "Please choose your discipline.",
      need_available: "Please say when you are available from.",
      need_consent: "Please confirm the privacy notice to continue.",
      need_group: "Please choose a service group.",
      need_topic: "Please choose a type of enquiry.",
      need_first: "Please enter your first name.",
      need_last: "Please enter your last name.",
      need_message: "Please tell us how we can help.",
      contact_sent: "Message sent. We will be in touch.",
      contact_mail: "Your mail app opened with the enquiry filled in — press send.",
      apply_mail: "Your mail app opened with the details filled in — attach your CV and send.",
      file_remove: "Remove",
      file_too_big: "Too large (10 MB maximum):",
      apply_mail_files: "Your mail app opened — now attach:",
      bp_flag_on_touch: "Blueprint mode \u2014 tap two points to measure \u00b7 tap the badge to exit"
    };
    T.fr = {
      cal_open: "Ouvrir le calendrier", cal_loading: "Chargement\u2026",
      cal_failed: 'Le calendrier n\u2019a pas pu se charger. <a href="%s" target="_blank" rel="noopener">Ouvrez-le dans un nouvel onglet</a>.',
      home: "Accueil", title_suffix: " \u2014 ALPROJECTS Group",
      bp_on: "Quitter le mode dessin", bp_off: "Mode dessin",
      bp_flag_on: "Mode plan \u2014 glissez pour mesurer \u00b7 B pour quitter",
      bp_flag_off: "Mode plan d\u00e9sactiv\u00e9",
      apply_sending: "Envoi\u2026",
      apply_sent: "Candidature envoy\u00e9e. Nous vous recontacterons.",
      apply_fail: "Envoi impossible. \u00c9crivez-nous \u00e0 info@alprojects.eu.",
      sub_invalid: "Saisissez une adresse e-mail valide pour vous abonner.",
      sub_consent: "Veuillez cocher la case de consentement avant de vous abonner.",
      sub_fail: "\u00c9chec de l\u2019abonnement. \u00c9crivez-nous \u00e0 info@alprojects.eu.",
      sub_mail: "Votre messagerie s\u2019est ouverte avec une demande d\u2019abonnement pr\u00e9-remplie.",
      need_name: "Veuillez saisir votre nom.",
      need_email: "Veuillez saisir une adresse e-mail valide.",
      need_phone: "Veuillez indiquer un numéro de téléphone ou WhatsApp.",
      need_role: "Veuillez choisir votre métier.",
      need_available: "Veuillez indiquer votre date de disponibilité.",
      need_consent: "Veuillez accepter la notice de confidentialité pour continuer.",
      need_group: "Veuillez choisir un domaine de services.",
      need_topic: "Veuillez choisir un type de demande.",
      need_first: "Veuillez saisir votre prénom.",
      need_last: "Veuillez saisir votre nom.",
      need_message: "Veuillez nous indiquer comment nous pouvons vous aider.",
      contact_sent: "Message envoyé. Nous vous recontacterons.",
      contact_mail: "Votre messagerie s’est ouverte avec la demande préremplie — cliquez sur envoyer.",
      apply_mail: "Votre messagerie s’est ouverte avec les informations pré-remplies — joignez votre CV et envoyez.",
      file_remove: "Retirer",
      file_too_big: "Trop volumineux (10 Mo maximum) :",
      apply_mail_files: "Votre messagerie s’est ouverte — joignez maintenant :",
      bp_flag_on_touch: "Mode plan \u2014 touchez deux points pour mesurer \u00b7 touchez le badge pour quitter"
    };
    T.de = {
      cal_open: "Kalender \u00f6ffnen", cal_loading: "Wird geladen\u2026",
      cal_failed: 'Der Kalender konnte nicht geladen werden. <a href="%s" target="_blank" rel="noopener">In neuem Tab \u00f6ffnen</a>.',
      home: "Startseite", title_suffix: " \u2014 ALPROJECTS Group",
      bp_on: "Zeichnungsmodus beenden", bp_off: "Zeichnungsmodus",
      bp_flag_on: "Zeichnungsmodus \u2014 zum Messen ziehen \u00b7 B zum Beenden",
      bp_flag_off: "Zeichnungsmodus aus",
      apply_sending: "Wird gesendet\u2026",
      apply_sent: "Bewerbung gesendet. Wir melden uns.",
      apply_fail: "Senden nicht m\u00f6glich. Bitte schreiben Sie an info@alprojects.eu.",
      sub_invalid: "Bitte geben Sie eine g\u00fcltige E-Mail-Adresse ein.",
      sub_consent: "Bitte kreuzen Sie das Einwilligungsfeld an, bevor Sie sich anmelden.",
      sub_fail: "Anmeldung fehlgeschlagen. Schreiben Sie an info@alprojects.eu.",
      sub_mail: "Ihr E-Mail-Programm wurde mit einer vorausgef\u00fcllten Anmeldung ge\u00f6ffnet.",
      need_name: "Bitte geben Sie Ihren Namen ein.",
      need_email: "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
      need_phone: "Bitte geben Sie eine Telefon- oder WhatsApp-Nummer an.",
      need_role: "Bitte wählen Sie Ihr Gewerk.",
      need_available: "Bitte geben Sie an, ab wann Sie verfügbar sind.",
      need_consent: "Bitte bestätigen Sie den Datenschutzhinweis, um fortzufahren.",
      need_group: "Bitte wählen Sie einen Leistungsbereich.",
      need_topic: "Bitte wählen Sie eine Art der Anfrage.",
      need_first: "Bitte geben Sie Ihren Vornamen ein.",
      need_last: "Bitte geben Sie Ihren Nachnamen ein.",
      need_message: "Bitte teilen Sie uns mit, wie wir helfen können.",
      contact_sent: "Nachricht gesendet. Wir melden uns.",
      contact_mail: "Ihr E-Mail-Programm wurde mit der ausgefüllten Anfrage geöffnet — bitte absenden.",
      apply_mail: "Ihr E-Mail-Programm wurde mit den Angaben geöffnet — hängen Sie Ihren Lebenslauf an und senden Sie.",
      file_remove: "Entfernen",
      file_too_big: "Zu groß (maximal 10 MB):",
      apply_mail_files: "Ihr E-Mail-Programm wurde geöffnet — hängen Sie jetzt an:",
      bp_flag_on_touch: "Zeichnungsmodus \u2014 zwei Punkte antippen zum Messen \u00b7 Badge antippen zum Beenden"
    };
    T.it = {
      cal_open: "Apri il calendario", cal_loading: "Caricamento\u2026",
      cal_failed: 'Impossibile caricare il calendario. <a href="%s" target="_blank" rel="noopener">Aprilo in una nuova scheda</a>.',
      home: "Home", title_suffix: " \u2014 ALPROJECTS Group",
      bp_on: "Esci dalla modalit\u00e0 disegno", bp_off: "Modalit\u00e0 disegno",
      bp_flag_on: "Modalit\u00e0 disegno \u2014 trascina per misurare \u00b7 B per uscire",
      bp_flag_off: "Modalit\u00e0 disegno disattivata",
      apply_sending: "Invio\u2026",
      apply_sent: "Candidatura inviata. Vi ricontatteremo.",
      apply_fail: "Invio non riuscito. Scriveteci a info@alprojects.eu.",
      sub_invalid: "Inserisci un indirizzo e-mail valido per iscriverti.",
      sub_consent: "Spunta la casella di consenso prima di iscriverti.",
      sub_fail: "Iscrizione non riuscita. Scriveteci a info@alprojects.eu.",
      sub_mail: "Il programma di posta si \u00e8 aperto con una richiesta di iscrizione precompilata.",
      need_name: "Inserisci il tuo nome.",
      need_email: "Inserisci un indirizzo e-mail valido.",
      need_phone: "Inserisci un numero di telefono o WhatsApp.",
      need_role: "Seleziona il tuo mestiere.",
      need_available: "Indica da quando sei disponibile.",
      need_consent: "Conferma l’informativa sulla privacy per continuare.",
      need_group: "Scegli un’area di servizio.",
      need_topic: "Scegli un tipo di richiesta.",
      need_first: "Inserisci il tuo nome.",
      need_last: "Inserisci il tuo cognome.",
      need_message: "Indicaci come possiamo aiutarti.",
      contact_sent: "Messaggio inviato. Vi ricontatteremo.",
      contact_mail: "Il programma di posta si è aperto con la richiesta compilata — premi invia.",
      apply_mail: "Il programma di posta si è aperto con i dati precompilati — allega il CV e invia.",
      file_remove: "Rimuovi",
      file_too_big: "Troppo grande (massimo 10 MB):",
      apply_mail_files: "Il programma di posta si è aperto — ora allega:",
      bp_flag_on_touch: "Modalit\u00e0 disegno \u2014 tocca due punti per misurare \u00b7 tocca il badge per uscire"
    };
    return T[LANG] || T.en;
  })();

  /* ---------- apply config ---------- */
  if (ANALYTICS_DOMAIN) {
    var an = document.createElement("script");
    an.defer = true;
    an.setAttribute("data-domain", ANALYTICS_DOMAIN);
    an.src = "https://plausible.io/js/script.js";
    document.head.appendChild(an);
  }

  /* ---------- booking ----------
     Calendly, loaded once and shared by the header button and the panel on
     the contacts page.

     The buttons stay plain links to Calendly, so they work with JavaScript
     off, with the script blocked, and on cmd-click. On a normal click we
     upgrade to Calendly's own popup -- the visitor picks a slot without ever
     leaving the tab -- but the widget is fetched ONLY AT THAT MOMENT.

     That ordering is the point. Embedding on page load would hand every
     visitor's IP to Calendly whether or not they ever book, and the rest of
     this site makes no third-party request at all. Loading on the click keeps
     that true for everyone who does not book. If the fetch fails, nothing is
     trapped: the original link is followed instead. */
  var CALENDLY_CSS = "https://assets.calendly.com/assets/external/widget.css";
  var CALENDLY_JS  = "https://assets.calendly.com/assets/external/widget.js";
  var calendlyLoading = null;

  /* Calendly reads the theme off the query string, so it opens in the site's
     palette instead of its own white default. */
  function calendlyUrl(url) {
    return url + (url.indexOf("?") === -1 ? "?" : "&") +
      "hide_gdpr_banner=1&background_color=0b0f16&text_color=e8eaf0&primary_color=ffffff";
  }

  function loadCalendly() {
    if (window.Calendly) return Promise.resolve();
    if (calendlyLoading) return calendlyLoading;
    calendlyLoading = new Promise(function (resolve, reject) {
      var css = document.createElement("link");
      css.rel = "stylesheet";
      css.href = CALENDLY_CSS;
      document.head.appendChild(css);

      var js = document.createElement("script");
      js.src = CALENDLY_JS;
      js.async = true;
      js.onload = function () { window.Calendly ? resolve() : reject(); };
      js.onerror = reject;
      document.head.appendChild(js);

      /* a blocker can leave onerror unfired -- do not hang on the click */
      setTimeout(function () { window.Calendly ? resolve() : reject(); }, 6000);
    });
    return calendlyLoading;
  }

  /* there is a booking button in the header and another in the mobile menu */
  if (BOOKING_URL) {
    document.querySelectorAll("[data-booking]").forEach(function (b) {
      b.setAttribute("href", BOOKING_URL);
      b.setAttribute("rel", "noopener");
      b.addEventListener("click", function (ev) {
        /* let a modifier open it in a tab, as any link would */
        if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button) return;
        ev.preventDefault();
        b.classList.add("is-loading");
        loadCalendly().then(function () {
          window.Calendly.initPopupWidget({ url: calendlyUrl(BOOKING_URL) });
        })["catch"](function () {
          window.open(BOOKING_URL, "_blank", "noopener");
        }).then(function () { b.classList.remove("is-loading"); });
      });
    });
  }

  /* ---------- the calendar panel on /contacts.html ----------
     A dedicated booking section gets the widget inline rather than in an
     overlay -- there is nothing to return to behind it. Same click-to-load
     rule, same shared loader. */
  var bookingPanel = document.querySelector("[data-booking-embed]");
  if (bookingPanel && BOOKING_URL) {
    bookingPanel.removeAttribute("hidden");
    var loadBtn = bookingPanel.querySelector("[data-booking-load]");
    var isCalendly = /(^|\.)calendly\.com$/i.test(
      (function () { try { return new URL(BOOKING_URL).hostname; } catch (e) { return ""; } })()
    );

    if (!isCalendly && loadBtn) {
      /* Not a Calendly link -- send them out rather than embedding something
         we cannot style or vouch for. */
      var out = document.createElement("a");
      out.className = "btn-bracket";
      out.href = BOOKING_URL;
      out.target = "_blank"; out.rel = "noopener";
      out.textContent = TXT.cal_open;
      loadBtn.parentNode.replaceChild(out, loadBtn);
    } else if (loadBtn) {
      loadBtn.addEventListener("click", function () {
        loadBtn.disabled = true;
        loadBtn.textContent = TXT.cal_loading;
        loadCalendly().then(function () {
          var mount = document.createElement("div");
          mount.className = "booking-widget";
          bookingPanel.classList.add("is-loaded");
          bookingPanel.appendChild(mount);
          window.Calendly.initInlineWidget({
            url: calendlyUrl(BOOKING_URL),
            parentElement: mount
          });
        })["catch"](function () {
          /* Blocked by an extension or offline -- never leave a dead panel. */
          bookingPanel.classList.remove("is-loaded");
          loadBtn.disabled = false;
          loadBtn.textContent = TXT.cal_open;
          var msg = bookingPanel.querySelector(".booking-note");
          if (msg) {
            msg.innerHTML = TXT.cal_failed.replace("%s", BOOKING_URL);
          }
        });
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
      page = h1 ? h1.textContent.trim() : TXT.home;
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
      ".sector-card, .adv-card, .news-card, .cert-card, .doc-card, .shot, .fp-card, " +
      ".plate, .case-card, .case-next-link"
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
      if (bpHintLabel) bpHintLabel.textContent = on ? TXT.bp_on : TXT.bp_off;
    }
    if (on) buildSheet();
    if (on) measure();
    try { sessionStorage.setItem(BLUEPRINT_KEY, on ? "1" : "0"); } catch (e) {}
    if (announce) {
      /* "B to exit" is wrong advice on a device with no B key. */
      var touch = window.matchMedia("(hover: none)").matches;
      flag.textContent = on
        ? (touch ? TXT.bp_flag_on_touch : TXT.bp_flag_on)
        : TXT.bp_flag_off;
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

  /* ---------- measuring by touch ----------
     Dragging is how you scroll a phone, so the mouse gesture cannot simply be
     reused -- the handler above ignores anything that is not a mouse for that
     reason, which left blueprint mode on a phone as a picture you could not
     use. Tapping two points does the same job and cannot be confused with a
     scroll: first tap plants the origin, second draws the dimension, third
     starts again.

     A tap is distinguished from a scroll by how far the finger travelled, not
     by how long it was down -- a slow scroll is still a scroll. */
  var tapStart = null, tapMoved = false, tapOrigin = null;

  document.addEventListener("pointerdown", function (ev) {
    if (!measuring() || ev.pointerType === "mouse") return;
    tapStart = { x: ev.clientX, y: ev.clientY };
    tapMoved = false;
  }, { passive: true });

  document.addEventListener("pointermove", function (ev) {
    if (!tapStart || ev.pointerType === "mouse") return;
    if (Math.abs(ev.clientX - tapStart.x) > 10 || Math.abs(ev.clientY - tapStart.y) > 10) {
      tapMoved = true;
    }
  }, { passive: true });

  document.addEventListener("pointerup", function (ev) {
    if (!measuring() || ev.pointerType === "mouse") return;
    var wasTap = tapStart && !tapMoved;
    tapStart = null;
    if (!wasTap) return;
    var t = ev.target;
    if (t && typeof t.closest === "function" &&
        t.closest("a, button, input, textarea, select, label")) return;

    clearTimeout(mFade);
    if (!tapOrigin) {
      tapOrigin = { x: ev.clientX, y: ev.clientY };
      mFrom = tapOrigin;
      mLayer.classList.add("on");
      drawMeasure(ev.clientX, ev.clientY);
    } else {
      mFrom = tapOrigin;
      drawMeasure(ev.clientX, ev.clientY);
      mFrom = null;
      tapOrigin = null;
      /* left on screen long enough to read the number */
      mFade = setTimeout(function () { mLayer.classList.remove("on"); }, 3200);
    }
  });
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

  /* The header used to gain a solid background once you scrolled past 30px.
     It is transparent at every scroll position now -- what keeps the nav
     readable is a scrim fixed to the top of the viewport that fades out to
     nothing, so there is no state to track and no scroll listener for it. */

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
      /* Reset to the out state only if the panel is at rest. Clicking a second
         service while the first is still fading in should let that fade carry
         on to the new content, not snap back to invisible -- which is exactly
         what the old @keyframes did: measured opacity 0.97, then 0 one click
         later. */
      var settled = parseFloat(getComputedStyle(art).opacity) > 0.99;
      if (settled) art.classList.add("is-entering");
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

      /* The longer block below the shell belongs to one service, and switching
         never reloads the page, so it has to be swapped with the panel. */
      var deep = document.getElementById("srvDeep");
      if (deep) {
        deep.innerHTML = sv.deep || "";
        deep.classList.toggle("is-on", !!sv.deep);
      }

      document.querySelectorAll(".srv-link").forEach(function (a) {
        var on = a.getAttribute("data-service") === sv.slug;
        a.classList.toggle("is-active", on);
        if (on) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      });

      document.title = sv.h1 + TXT.title_suffix;
      if (push && window.history && history.pushState) {
        history.pushState({ srv: sv.slug }, "", PREFIX + "/services/" + sv.slug);
      }
      /* Release on the next frame: the browser has to paint the out state once
         before the transition back to rest will run. */
      if (settled) {
        requestAnimationFrame(function () {
          requestAnimationFrame(function () { art.classList.remove("is-entering"); });
        });
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
      /* The header is transparent at the top of the page; while the panel is
         open it has to be opaque or the page shows through above it. */
      document.documentElement.classList.toggle("menu-open", open);
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
        document.documentElement.classList.remove("menu-open");
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
  /* The real figure is written into the HTML, so a crawler, a link preview or
     a visitor whose JS never ran sees 11,000 rather than 0. That means the
     animation has to reset it here instead of counting up from a zero that was
     sitting in the markup. Reset only when the animation is going to run: with
     reduced motion the number simply stays as authored. */
  if (!reduceMotion) {
    counters.forEach(function (el) {
      var t = parseInt(el.getAttribute("data-count"), 10);
      if (!isNaN(t)) el.textContent = "0" + (el.getAttribute("data-suffix") || "");
    });
  }
  function animateCounter(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    /* 11000 has to read as 11,000 -- and as 11.000 in German, 11 000 in
       French. The page's own lang attribute picks the separator, so the
       figure is grouped correctly in all four languages without a table. */
    function fmt(n) {
      try { return n.toLocaleString(document.documentElement.lang || "en"); }
      catch (e) { return String(n); }
    }
    if (reduceMotion) { el.textContent = fmt(target) + suffix; return; }
    var dur = 1400;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(target * eased)) + suffix;
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
  /* ---------- gallery viewer ----------
     The thumbnails are buttons in the markup, so with JavaScript off they are
     simply figures and nothing is broken. Here they open the full photograph:
     an industrial portfolio is evidence, and evidence you cannot see at size
     is decoration. */
  var lb = document.getElementById("lightbox");
  var shotBtns = [].slice.call(document.querySelectorAll(".shot-open"));
  if (lb && shotBtns.length) {
    var lbImg = document.getElementById("lbImage");
    var lbCap = document.getElementById("lbCaption");
    var lbCount = document.getElementById("lbCount");
    var lbPrev = document.getElementById("lbPrev");
    var lbNext = document.getElementById("lbNext");
    var lbClose = document.getElementById("lbClose");
    var lbIndex = 0;
    var lastFocus = null;

    var shots = shotBtns.map(function (btn) {
      var img = btn.querySelector("img");
      var cap = btn.parentNode.querySelector("figcaption");
      return {
        src: img.getAttribute("src"),
        alt: img.getAttribute("alt") || "",
        caption: cap ? cap.textContent.trim() : "",
        btn: btn
      };
    });

    function show(i, instant) {
      lbIndex = (i + shots.length) % shots.length;
      var sh = shots[lbIndex];
      /* Fade the old frame out, swap, fade in. Without it the photograph is
         replaced in a single frame, which reads as a glitch rather than as
         moving to the next one. Neighbours are preloaded below, so the new
         image is decoded and the fade is the only cost. */
      if (!instant) lbImg.classList.add("is-swapping");
      lbImg.src = sh.src;
      lbImg.alt = sh.alt;
      if (!instant) {
        var clear = function () {
          /* the browser has to paint the invisible frame once before the
             transition back to full opacity will run */
          requestAnimationFrame(function () {
            requestAnimationFrame(function () { lbImg.classList.remove("is-swapping"); });
          });
        };
        if (lbImg.decode) lbImg.decode().then(clear, clear);
        else lbImg.addEventListener("load", clear, { once: true });
      }
      lbCap.textContent = sh.caption;
      lbCount.textContent = (lbIndex + 1) + " / " + shots.length;
      /* Preload the neighbours so arrowing through does not flash. */
      [lbIndex - 1, lbIndex + 1].forEach(function (n) {
        var t = shots[(n + shots.length) % shots.length];
        var pre = new Image();
        pre.src = t.src;
      });
    }

    function openLb(i) {
      lastFocus = document.activeElement;
      show(i, true);      /* the panel itself is appearing; no crossfade */
      lb.hidden = false;
      document.documentElement.classList.add("lb-open");
      lbClose.focus();
    }

    function closeLb() {
      lb.hidden = true;
      document.documentElement.classList.remove("lb-open");
      lbImg.removeAttribute("src");   /* not src="" -- see the markup note */
      /* Back to the thumbnail that was opened, not the top of the page. */
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    shotBtns.forEach(function (btn, i) {
      btn.addEventListener("click", function () { openLb(i); });
    });
    lbPrev.addEventListener("click", function () { show(lbIndex - 1); });
    lbNext.addEventListener("click", function () { show(lbIndex + 1); });
    [].slice.call(lb.querySelectorAll("[data-lb-close]")).forEach(function (el) {
      el.addEventListener("click", closeLb);
    });

    document.addEventListener("keydown", function (ev) {
      if (lb.hidden) return;
      if (ev.key === "Escape") { ev.preventDefault(); closeLb(); }
      else if (ev.key === "ArrowLeft") { ev.preventDefault(); show(lbIndex - 1); }
      else if (ev.key === "ArrowRight") { ev.preventDefault(); show(lbIndex + 1); }
      else if (ev.key === "Tab") {
        /* Keep Tab inside the dialog, or the focus ring walks off into the page
           behind the scrim where nothing is visible.

           This takes over every Tab rather than only the ones that fall off the
           end. Deferring to the browser in the middle of the cycle assumed my
           array was in DOM order, and it is not -- the buttons are prev, next,
           close in the markup -- so Tab from the close button went straight out
           to a link behind the scrim. */
        var f = [lbPrev, lbNext, lbClose];
        var at = f.indexOf(document.activeElement);
        var next = at === -1 ? 0 : (at + (ev.shiftKey ? -1 : 1) + f.length) % f.length;
        ev.preventDefault();
        f[next].focus();
      }
    });

    /* Swipe, because on a phone this is the obvious gesture. Horizontal only,
       so it never fights the vertical scroll. */
    var sx = 0, sy = 0, tracking = false;
    lb.addEventListener("touchstart", function (ev) {
      if (ev.touches.length !== 1) return;
      sx = ev.touches[0].clientX; sy = ev.touches[0].clientY; tracking = true;
    }, { passive: true });
    lb.addEventListener("touchend", function (ev) {
      if (!tracking) return;
      tracking = false;
      var t = ev.changedTouches[0];
      var dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        show(lbIndex + (dx < 0 ? 1 : -1));
      }
    }, { passive: true });
  }

  /* ---------- careers: chips ----------
     Toggle buttons instead of free text. The applicant taps rather than types,
     and what arrives is structured enough to filter on. aria-pressed carries
     the state: a <button> that only changes class has, to a screen reader,
     done nothing. */
  function chipGroup(id, attr, single) {
    var box = document.getElementById(id);
    if (!box) return function () { return []; };
    var btns = [].slice.call(box.querySelectorAll(".chip"));
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var on = b.getAttribute("aria-pressed") === "true";
        if (single) btns.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", on ? "false" : "true");
      });
    });
    return function () {
      return btns.filter(function (b) { return b.getAttribute("aria-pressed") === "true"; })
                 .map(function (b) { return b.getAttribute(attr); });
    };
  }

  var getCerts = chipGroup("certChips", "data-cert");
  var getRotation = chipGroup("rotChips", "data-rotation", true);
  var getCountries = chipGroup("ctryChips", "data-country");

  var applyForm = document.getElementById("applyForm");
  if (applyForm) {
    var applyNote = document.getElementById("applyNote");
    var roleSelect = document.getElementById("apRole");

    function pickRole(role) {
      if (!roleSelect) return;
      Array.prototype.forEach.call(roleSelect.options, function (o) {
        if (o.value === role || o.text === role) roleSelect.value = o.value || o.text;
      });
    }

    /* The discipline chips above the form are a shortcut into it. */
    var discBox = document.getElementById("discChips");
    if (discBox) {
      [].slice.call(discBox.querySelectorAll(".chip")).forEach(function (b) {
        b.addEventListener("click", function () {
          [].slice.call(discBox.querySelectorAll(".chip")).forEach(function (x) {
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          });
          pickRole(b.getAttribute("data-discipline"));
          var form = document.getElementById("apply");
          if (form) form.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
          var first = document.getElementById("apName");
          if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 500);
        });
      });
    }

    /* "Apply for this role" preselects that position and moves focus into the form */
    document.querySelectorAll("[data-apply]").forEach(function (a) {
      a.addEventListener("click", function () {
        pickRole(a.getAttribute("data-apply"));
        var first = document.getElementById("apName");
        if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 400);
      });
    });

    /* ---------- documents ----------
       The drop zone is in the markup, so it is there with or without a backend
       and it is translated with everything else. What differs is where the
       files go:
         CAREERS_ENDPOINT set   -> uploaded with the form as multipart
         CAREERS_ENDPOINT empty -> named in the email that opens, so the
                                   applicant knows exactly what to attach
       What it never does is accept a file and quietly lose it. */
    var picked = [];
    var dz = document.getElementById("dropZone");
    var fileInput = document.getElementById("apFiles");
    var fileList = document.getElementById("fileList");
    var MAX = 10 * 1024 * 1024;

    function renderFiles() {
      if (!fileList) return;
      fileList.innerHTML = "";
      picked.forEach(function (f, i) {
        var li = document.createElement("li");
        var nm = document.createElement("span");
        nm.textContent = f.name;
        var sz = document.createElement("span");
        sz.textContent = Math.max(1, Math.round(f.size / 1024)) + " KB";
        var rm = document.createElement("button");
        rm.type = "button";
        rm.className = "file-x";
        rm.setAttribute("aria-label", TXT.file_remove + " " + f.name);
        rm.textContent = "\u00d7";
        rm.addEventListener("click", function () {
          picked.splice(i, 1);
          renderFiles();
          if (fileInput) fileInput.focus();
        });
        li.appendChild(nm); li.appendChild(sz); li.appendChild(rm);
        fileList.appendChild(li);
      });
    }

    if (dz && fileInput) {
      var takeFiles = function (list) {
        var over = [];
        [].slice.call(list).forEach(function (f) {
          if (f.size > MAX) { over.push(f.name); return; }
          /* the same file twice is a mis-click, not an intention */
          var dup = picked.some(function (x) { return x.name === f.name && x.size === f.size; });
          if (!dup) picked.push(f);
        });
        if (over.length && applyNote) {
          applyNote.textContent = TXT.file_too_big + " " + over.join(", ");
          applyNote.classList.add("show", "is-error");
        }
        renderFiles();
      };
      /* No click handler on the drop zone: it is a <label for>, so the browser
         opens the picker itself. JavaScript only adds drag-and-drop. */
      fileInput.addEventListener("change", function () {
        takeFiles(fileInput.files);
        fileInput.value = "";     /* so re-picking the same file still fires change */
      });
      ["dragenter", "dragover"].forEach(function (e) {
        dz.addEventListener(e, function (ev) { ev.preventDefault(); dz.classList.add("is-over"); });
      });
      ["dragleave", "drop"].forEach(function (e) {
        dz.addEventListener(e, function (ev) { ev.preventDefault(); dz.classList.remove("is-over"); });
      });
      dz.addEventListener("drop", function (ev) {
        ev.preventDefault();
        takeFiles(ev.dataTransfer.files);
      });
    }

    applyForm.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var f = applyForm;
      var data = {
        name: f.name.value.trim(),
        email: f.email.value.trim(),
        phone: f.phone.value.trim(),
        country: f.country.value.trim(),
        role: f.role.value,
        years: f.years.value,
        certifications: getCerts().join(", "),
        available: f.available.value,
        rotation: getRotation().join(", "),
        countries: getCountries().join(", "),
        message: f.message.value.trim()
      };

      function fail(msg, field) {
        applyNote.textContent = msg;
        applyNote.classList.add("show", "is-error");
        if (field) field.focus();
      }
      applyNote.classList.remove("is-error");

      /* the honeypot is invisible to a person; anything in it is a bot */
      if (f.company && f.company.value) return;

      if (!data.name) return fail(TXT.need_name, f.name);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) return fail(TXT.need_email, f.email);
      if (!data.phone) return fail(TXT.need_phone, f.phone);
      if (!data.role) return fail(TXT.need_role, f.role);
      if (!data.available) return fail(TXT.need_available, f.available);
      if (!f.consent.checked) return fail(TXT.need_consent, f.consent);

      if (CAREERS_ENDPOINT) {
        applyNote.textContent = TXT.apply_sending;
        applyNote.classList.add("show");
        var fd = new FormData();
        Object.keys(data).forEach(function (k) { fd.append(k, data[k]); });
        picked.forEach(function (file) { fd.append("attachment", file, file.name); });
        fetch(CAREERS_ENDPOINT, { method: "POST", headers: { Accept: "application/json" }, body: fd })
          .then(function (r) {
            if (r.ok) {
              applyNote.textContent = TXT.apply_sent;
              applyNote.classList.remove("is-error");
              f.reset();
              picked.length = 0;
              document.querySelectorAll(".apply-form .chip[aria-pressed=true]")
                .forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
              var fl = document.getElementById("fileList");
              if (fl) fl.innerHTML = "";
            } else { fail(TXT.apply_fail); }
          })
          .catch(function () { fail(TXT.apply_fail); });
        return;
      }

      /* No endpoint configured: hand off to the applicant's mail client with a
         pre-filled message, so the CV can be attached there. */
      function line(label, v) { return label + ": " + (v || "—"); }
      var body = [
        line("Position", data.role),
        line("Name", data.name),
        line("Email", data.email),
        line("Phone", data.phone),
        line("Country", data.country),
        line("Experience", data.years),
        line("Certificates", data.certifications),
        line("Available from", data.available),
        line("Rotation", data.rotation),
        line("Can work in", data.countries),
        "",
        data.message || "",
        "",
        picked.length
          ? "(Please attach to this email: " +
            picked.map(function (f) { return f.name; }).join(", ") + ")"
          : "(Please attach your CV and certificates to this email.)"
      ].join("\n");
      window.location.href =
        "mailto:info@alprojects.eu?subject=" +
        encodeURIComponent("Application — " + data.role) +
        "&body=" + encodeURIComponent(body);
      /* mailto cannot carry an attachment, so say which files to attach rather
         than letting the applicant assume the ones they chose went with it. */
      applyNote.textContent = picked.length
        ? TXT.apply_mail_files + " " + picked.map(function (f) { return f.name; }).join(", ")
        : TXT.apply_mail;
      applyNote.classList.add("show");
    });
  }


  /* ---------- "Meet the management" link ---------- */
  /* ---------- VCA certificate card ---------- */
  var vca = document.querySelector("[data-vca]");
  if (vca) {
    if (VCA_META) {
      var meta = vca.querySelector(".cert-meta");
      if (meta) {
        meta.innerHTML = "";
        VCA_META.split("|").forEach(function (part) {
          var sp = document.createElement("span");
          sp.textContent = part;
          meta.appendChild(sp);
        });
      }
    }
    if (VCA_URL) {
      /* becomes a link, the same as the three DNV cards */
      var a = document.createElement("a");
      a.className = "cert-card";
      a.href = VCA_URL;
      a.target = "_blank";
      a.rel = "noopener";
      a.setAttribute("aria-label", "Open the VCA certificate as a PDF");
      a.innerHTML = vca.innerHTML;
      vca.parentNode.replaceChild(a, vca);
    }
  }

  var mgmt = document.querySelector("[data-management]");
  if (mgmt) {
    if (MANAGEMENT_URL) {
      mgmt.href = MANAGEMENT_URL;
      mgmt.hidden = false;
    } else {
      mgmt.parentNode.removeChild(mgmt);
    }
  }

  /* ---------- contact form (/contacts.html) ----------
     Mirrors the careers form: validate, drop bots on the honeypot, POST to
     CONTACT_ENDPOINT when one is configured and otherwise hand the whole
     enquiry to the visitor's mail client. */
  var contactForm = document.getElementById("contactForm");
  var contactNote = document.getElementById("contactNote");
  if (contactForm && contactNote) {
    contactForm.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var f = contactForm;
      var data = {
        group: f.group.value,
        topic: f.topic.value,
        first: f.first.value.trim(),
        last: f.last.value.trim(),
        email: f.email.value.trim(),
        phone: f.phone.value.trim(),
        company: f.company.value.trim(),
        message: f.message.value.trim()
      };

      function fail(msg, field) {
        contactNote.textContent = msg;
        contactNote.classList.add("show", "is-error");
        if (field) field.focus();
      }
      contactNote.classList.remove("is-error");

      /* invisible to a person; anything in it is a bot */
      if (f.website && f.website.value) return;

      if (!data.group) return fail(TXT.need_group, f.group);
      if (!data.topic) return fail(TXT.need_topic, f.topic);
      if (!data.first) return fail(TXT.need_first, f.first);
      if (!data.last) return fail(TXT.need_last, f.last);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) return fail(TXT.need_email, f.email);
      if (!data.message) return fail(TXT.need_message, f.message);
      if (!f.consent.checked) return fail(TXT.need_consent, f.consent);

      if (CONTACT_ENDPOINT) {
        contactNote.textContent = TXT.apply_sending;
        contactNote.classList.add("show");
        var fd = new FormData();
        Object.keys(data).forEach(function (k) { fd.append(k, data[k]); });
        fetch(CONTACT_ENDPOINT, { method: "POST", headers: { Accept: "application/json" }, body: fd })
          .then(function (r) {
            if (r.ok) {
              contactNote.textContent = TXT.contact_sent;
              contactNote.classList.remove("is-error");
              f.reset();
            } else { fail(TXT.apply_fail); }
          })
          .catch(function () { fail(TXT.apply_fail); });
        return;
      }

      function line(label, v) { return label + ": " + (v || "\u2014"); }
      var body = [
        line("Service group", data.group),
        line("Type of enquiry", data.topic),
        line("Name", data.first + " " + data.last),
        line("Company", data.company),
        line("Email", data.email),
        line("Phone", data.phone),
        "",
        data.message
      ].join("\n");
      window.location.href =
        "mailto:info@alprojects.eu?subject=" +
        encodeURIComponent(data.topic + " \u2014 " + (data.company || data.last)) +
        "&body=" + encodeURIComponent(body);
      contactNote.textContent = TXT.contact_mail;
      contactNote.classList.remove("is-error");
      contactNote.classList.add("show");
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
        note.textContent = TXT.sub_invalid;
        note.classList.add("show");
        return;
      }
      /* Consent is a condition of sending, not decoration. The box lives
         outside <form> so a submit cannot be satisfied by the browser's own
         required-check alone; gate it here as well. */
      var consent = document.getElementById("nlConsent");
      if (consent && !consent.checked) {
        note.textContent = TXT.sub_consent;
        note.classList.add("show");
        consent.focus();
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
            note.textContent = TXT.sub_fail;
            note.classList.add("show");
          });
      } else {
        window.location.href =
          "mailto:info@alprojects.eu?subject=" +
          encodeURIComponent("Newsletter subscription") +
          "&body=" +
          encodeURIComponent("Please subscribe this address to company updates: " + email);
        note.textContent = TXT.sub_mail;
        note.classList.add("show");
      }
    });
  }
})();

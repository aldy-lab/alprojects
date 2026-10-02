/* ============================================================
   ALPROJECTS — the form endpoint, as a function on the site's own domain
   ============================================================
   This replaces endpoint/form.php, which needed a PHP host the client never
   supplied. It runs on Vercel, at /api/form, on alprojects.co itself: no
   second host to arrange, no cross-origin request, no third party holding the
   applications.

   WHAT IT DOES NOT DO
   Nothing is written to disk or to a database. The enquiries and applications
   already go to info@ and are worked from there; a second copy would be a
   second thing to secure, to find on a subject-access request, and to delete
   after twenty-four months, for no benefit.

   ZERO DEPENDENCIES, AND THAT IS DELIBERATE
   No package.json anywhere in this repository, and this file does not add one.
   Multipart is parsed by the platform -- a Web-standard handler gets
   request.formData() for free, which is why this is written as (request) =>
   Response rather than in the (req, res) style. The mail provider is a JSON
   POST over fetch. A dependency here would mean npm install on every deploy,
   a lockfile to keep current, and a build step on a host that currently needs
   none.

   THE SECRET LIVES IN THE ENVIRONMENT, NOT IN THE FILE
   form.php could never hold a key: it sat in a public repository and GitHub
   Pages served it as text. That is fixed twice over now -- the repository is
   closing and .vercelignore keeps the source out of the deployment -- but the
   rule stands anyway, because a key in a file is a key in every clone and
   every backup of it. MAIL_API_KEY is a Vercel environment variable.

   CONFIGURATION (Vercel project -> Settings -> Environment Variables)
     MAIL_PROVIDER   resend | postmark | dry-run   (unset = not configured,
                     and the endpoint then refuses rather than pretending)
     MAIL_API_KEY    the provider's key
     MAIL_TO         where submissions go          e.g. info@alprojects.eu
     MAIL_FROM       a sender the PROVIDER has verified, which need not be
                     the site's own domain         e.g. forms@alprojects.co
     SITE_ORIGIN     the origins allowed to post here, comma separated
   With MAIL_PROVIDER=dry-run the endpoint validates everything and reports
   what it would have sent without sending it -- the whole path, attachments
   included, before an address is involved. With it UNSET the endpoint refuses,
   which is what the forms need while the key is still missing.
   ============================================================ */

const MAX_FILES = 6;
/* The same ceiling the page promises and the picker enforces. The platform's
   own cap on a request body is lower than this, so on a big application the
   refusal comes from the edge and not from here -- and that is survivable
   rather than a dead end: the browser's failure branch hands the whole form
   to the applicant's mail client with every field filled in and the files
   named, so nothing they typed is lost and the CV gets attached there.

   Which is why this is 10MB and not 4: matching the promise on the page costs
   nothing, capping it lower would mean changing that promise in four
   languages, and the outcome for an applicant with a 6MB scan is the same
   either way. */
const MAX_BYTES = 10 * 1024 * 1024;
const ALLOWED_EXT = [
  "pdf", "doc", "docx", "jpg", "jpeg", "png", "webp", "heic",
  "dwg", "dxf", "step", "stp", "igs", "iges", "zip", "txt",
];
/* Which origins may use this endpoint. From the environment, so moving the
   site to another domain is a variable and not a code change:

     SITE_ORIGIN = https://alprojects.eu,https://www.alprojects.eu

   MAIL_FROM is a separate question and does not have to follow the site. The
   sending domain is whatever the mail provider has verified -- forms@ on one
   domain can post to info@ on another, and it keeps working after the website
   moves. That is why the sender is worth verifying on the domain whose DNS is
   in reach rather than on the one the site will end up on. */
const ALLOWED_ORIGIN = (process.env.SITE_ORIGIN ||
  "https://alprojects.eu,https://www.alprojects.eu," +
  "https://alprojects.co,https://www.alprojects.co")
  .split(",").map((s) => s.trim()).filter(Boolean);

/* The three forms, and which fields each one is allowed to send. A field not
   on its form's list is dropped rather than emailed: the endpoint is public,
   and without this anyone could post arbitrary text into the office's inbox
   through it. `honey` is the field that must stay empty. */
const FORMS = {
  careers: {
    subject: "Careers application",
    honey: "company",
    fields: ["name", "email", "phone", "country", "role", "years",
             "available", "message"],
    files: true,
  },
  contact: {
    subject: "Website enquiry",
    honey: "website",
    fields: ["group", "topic", "first", "last", "email", "phone",
             "company", "message"],
    files: true,
  },
  subscribe: {
    subject: "Newsletter subscription",
    honey: null,
    fields: ["email"],
    files: false,
  },
};

const CONSENT_FIELDS = ["consent", "consent_page", "consent_lang", "consent_text"];

/* A header value carries whatever the sender put in it, and a newline in a
   subject or a reply-to is a way to add headers of your own. The provider
   APIs take these as JSON rather than as header lines, so this is belt and
   braces -- and it costs one regex. */
function headerSafe(s) {
  return String(s == null ? "" : s).replace(/[\r\n]+/g, " ").slice(0, 300);
}

function json(status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

/* One minute between submissions from an address. Per instance, and that is
   the honest description of it: Vercel may run several, and one that has just
   started knows nothing. It blunts a script hammering one form; the honeypot
   and the consent requirement do the rest. A shared store for this would mean
   a dependency and another service for a rule that is not security. */
const seen = new Map();
function throttled(key) {
  const now = Date.now();
  for (const [k, t] of seen) if (now - t > 120000) seen.delete(k);
  const last = seen.get(key);
  if (last && now - last < 60000) return true;
  seen.set(key, now);
  return false;
}

async function send(mail) {
  /* An UNSET provider is "not configured", not "dry run", and the difference
     is the whole safety of switching the three endpoints on before the mail
     key exists.

     It defaulted to dry-run, which answers 200. That would have put the form
     in the worst state it can be in: the visitor is told the enquiry was sent,
     the office never receives it, and nothing anywhere records that it
     happened. Unset now means 503, the browser's failure branch opens the
     applicant's mail client with every field filled in, and the submission
     survives. Dry-run is still there, but only when it is asked for by name.

     Which is what makes the endpoints safe to enable ahead of the key: with
     no MAIL_PROVIDER the forms behave exactly as they do today, and the moment
     the four variables are set in the host they start delivering, with no
     deploy in between. */
  const provider = (process.env.MAIL_PROVIDER || "").toLowerCase();
  if (!provider) {
    return { ok: false, error: "MAIL_PROVIDER is not set", unconfigured: true };
  }
  if (provider === "dry-run") {
    console.log("[form] dry-run, would send:", JSON.stringify({
      to: mail.to, from: mail.from, subject: mail.subject,
      replyTo: mail.replyTo, bytes: mail.text.length,
      attachments: mail.attachments.map((a) => [a.filename, a.bytes]),
    }));
    return { ok: true, dryRun: true };
  }
  const key = process.env.MAIL_API_KEY;
  if (!key) return { ok: false, error: "MAIL_API_KEY is not set" };

  if (provider === "resend") {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { authorization: "Bearer " + key, "content-type": "application/json" },
      body: JSON.stringify({
        from: mail.from,
        to: [mail.to],
        reply_to: mail.replyTo || undefined,
        subject: mail.subject,
        text: mail.text,
        attachments: mail.attachments.map((a) => ({
          filename: a.filename, content: a.base64,
        })),
      }),
    });
    if (!r.ok) return { ok: false, error: "resend " + r.status + " " + (await r.text()).slice(0, 300) };
    /* The provider's own id for the message, to the server log and nowhere
       near the browser. It is the only thing that answers the one question
       this endpoint cannot answer by itself -- "the form said sent and nothing
       arrived" -- because it finds the exact message in the provider's
       dashboard, with its delivery or its bounce. Without it that question
       starts from scratch every time. */
    let id = null;
    try { id = (await r.json()).id || null; } catch { /* accepted, id unread */ }
    console.log("[form] resend accepted" + (id ? " id=" + id : "") +
                " to=" + mail.to + " attachments=" + mail.attachments.length);
    return { ok: true };
  }

  if (provider === "postmark") {
    const r = await fetch("https://api.postmarkapp.com/email", {
      method: "POST",
      headers: {
        "X-Postmark-Server-Token": key,
        "content-type": "application/json",
        accept: "application/json",
      },
      body: JSON.stringify({
        From: mail.from,
        To: mail.to,
        ReplyTo: mail.replyTo || undefined,
        Subject: mail.subject,
        TextBody: mail.text,
        MessageStream: "outbound",
        Attachments: mail.attachments.map((a) => ({
          Name: a.filename, Content: a.base64, ContentType: a.type || "application/octet-stream",
        })),
      }),
    });
    if (!r.ok) return { ok: false, error: "postmark " + r.status + " " + (await r.text()).slice(0, 300) };
    return { ok: true };
  }

  return { ok: false, error: "unknown MAIL_PROVIDER: " + provider };
}

const PROVIDER_NAMES = { resend: "Resend", postmark: "Postmark" };

async function handle(request) {
  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: { allow: "POST" } });
  }

  /* A GET says whether a third party is in the path, and nothing else.
     The privacy policy carries a line naming the processor that "receives
     what you send through the forms, including any documents you attach".
     It used to be revealed by the page whenever an endpoint was configured
     and named after that endpoint's hostname -- which, now that the endpoint
     is this site's own domain, would have printed "alprojects.co receives
     what you send and passes it to us". Nonsense, and in the other direction
     it would have claimed a processor before one existed: with no key set,
     nothing leaves the visitor's own browser except to their own mail client.

     So the page asks. No key, no line. Resend configured, the line names
     Resend. The policy cannot drift from what the host is actually doing,
     which is the way that particular disclosure goes wrong.

     Answered BEFORE the origin check, and that is not an oversight: a browser
     sends no Origin header on a same-origin GET, so the check would refuse
     the page's own question. What it gives away is a boolean and a provider
     name, which is precisely what the policy publishes on purpose. */
  if (request.method === "GET") {
    const p = (process.env.MAIL_PROVIDER || "").toLowerCase();
    return json(200, {
      ok: true,
      configured: !!p && p !== "dry-run",
      processor: PROVIDER_NAMES[p] || null,
    });
  }

  if (request.method !== "POST") return json(405, { ok: false, error: "post only" });

  /* Same-origin only. A form on another site cannot use this to mail the
     office, and a curl with no Origin at all is refused too -- every real
     submission comes from a page on the domain. The preview deployments are
     allowed as well, or the endpoint could never be tested before it is live. */
  const origin = request.headers.get("origin") || "";
  const okOrigin = ALLOWED_ORIGIN.includes(origin) ||
                   /^https:\/\/[a-z0-9-]+\.vercel\.app$/.test(origin);
  if (!okOrigin) return json(403, { ok: false, error: "origin" });

  const which = new URL(request.url).searchParams.get("f") || "";
  const form = FORMS[which];
  if (!form) return json(400, { ok: false, error: "unknown form" });

  let data;
  try {
    data = await request.formData();
  } catch (e) {
    /* PLATFORM LIMIT. A body over the platform's cap never reaches this
       function as a readable form -- it fails here, or the request is rejected
       at the edge before the function runs at all. MAX_BYTES below is the
       site's own limit and is set under the platform's so the refusal comes
       from this file, with a message the form can show, rather than from the
       edge with one it cannot. */
    return json(413, { ok: false, error: "body too large or not a form" });
  }

  if (form.honey && String(data.get(form.honey) || "").trim() !== "") {
    /* Answer 200. A bot that is told it failed tries again differently. */
    return json(200, { ok: true });
  }

  /* The consent record the site sends with every submission. Refusing a
     submission without it is the point: it is the only evidence that the box
     was ticked, and the wording it was ticked against. */
  if (String(data.get("consent") || "") !== "yes") {
    return json(422, { ok: false, error: "consent" });
  }

  const email = String(data.get("email") || "").trim();
  if (!/^[^@\s]+@[^@\s.]+\.[^@\s]+$/.test(email)) {
    return json(422, { ok: false, error: "email" });
  }

  const ip = (request.headers.get("x-forwarded-for") || "").split(",")[0].trim();
  if (throttled(ip + "|" + which)) return json(429, { ok: false, error: "too soon" });

  const lines = [];
  for (const name of form.fields) {
    const v = String(data.get(name) || "").trim();
    if (v) lines.push(name.padEnd(16) + v.replace(/\r?\n/g, "\n                "));
  }
  lines.push("");
  lines.push("--- consent -------------------------------------------------");
  for (const name of CONSENT_FIELDS) {
    lines.push(name.replace("consent_", "").padEnd(16) + String(data.get(name) || ""));
  }
  lines.push("");
  lines.push("--- request -------------------------------------------------");
  lines.push("form            " + which);
  lines.push("origin          " + origin);
  lines.push("ip              " + (ip || "unknown"));
  lines.push("received        " + new Date().toISOString());

  const attachments = [];
  if (form.files) {
    const files = data.getAll("attachment[]").concat(data.getAll("attachment"))
                      .filter((f) => f && typeof f === "object" && f.name);
    if (files.length > MAX_FILES) {
      return json(422, { ok: false, error: "too many files" });
    }
    let total = 0;
    for (const f of files) {
      const ext = (f.name.split(".").pop() || "").toLowerCase();
      if (!ALLOWED_EXT.includes(ext)) {
        return json(422, { ok: false, error: "file type: ." + ext });
      }
      const buf = Buffer.from(await f.arrayBuffer());
      total += buf.length;
      if (total > MAX_BYTES) {
        return json(413, { ok: false, error: "attachments too large" });
      }
      attachments.push({
        filename: f.name.replace(/[^\w.\- ]+/g, "_").slice(0, 120),
        base64: buf.toString("base64"),
        bytes: buf.length,
        type: f.type,
      });
    }
    if (attachments.length) {
      lines.splice(lines.length - 4, 0,
        "--- attachments ---------------------------------------------",
        ...attachments.map((a) => a.filename.padEnd(40) + a.bytes + " bytes"), "");
    }
  }

  const name = [data.get("name"), data.get("first"), data.get("last")]
    .map((x) => String(x || "").trim()).filter(Boolean).join(" ");

  const result = await send({
    to: process.env.MAIL_TO || "info@alprojects.eu",
    from: process.env.MAIL_FROM || "forms@alprojects.co",
    replyTo: email,
    /* The host the submission actually came from, not a hard-coded one: the
       office can tell which site sent it, and it stays true after a move. */
    subject: headerSafe(form.subject + (name ? " — " + name : "") +
                        " — " + (origin.replace(/^https?:\/\//, "") || "the website")),
    text: lines.join("\n"),
    attachments,
  });

  if (!result.ok) {
    console.error("[form] send failed:", result.error);
    /* 503 rather than 502 when the mail is simply not configured yet: the
       browser treats both the same -- any non-2xx hands the form to the mail
       client -- but the log says which of the two it was. */
    return json(result.unconfigured ? 503 : 502, { ok: false, error: "mail" });
  }
  return json(200, { ok: true, dryRun: result.dryRun || undefined });
}


/* ------------------------------------------------------------------
   THE SIGNATURE, WHICH THE PLATFORM PICKS AND NOT THIS FILE
   ------------------------------------------------------------------
   Everything above is written against the Web standard: a Request in, a
   Response out. That is the shape that gives multipart parsing for free
   through request.formData(), and it is what the 19 tests exercise.

   Vercel's Node runtime called it with (req, res) instead -- Node's own
   IncomingMessage and ServerResponse. Which broke it in two different ways at
   once, and the merge was the first time either could be seen:

     POST -> 500, because request.headers.get() does not exist on an
             IncomingMessage; its headers are a plain object.
     GET  -> no answer at all, timing out after 25 seconds, because the
             handler returned a Response and nothing ever wrote it to `res`.

   So the boundary adapts and the logic does not. If a second argument turns
   up that can end a response, the request is rebuilt as a Request, the
   Response that comes back is written out, and the size guard runs before any
   of it is buffered. Called with a single Request -- by a test, or by a
   runtime that uses the Web signature -- it passes straight through.

   Written this way rather than rewritten for (req, res) on purpose: hand-rolled
   multipart parsing is the part of this file most likely to be subtly wrong,
   and formData() is the platform's. */
const BODY_LIMIT = MAX_BYTES + 512 * 1024;   // the fields, on top of the files

function readBody(req) {
  return new Promise((resolve, reject) => {
    const parts = [];
    let size = 0;
    let over = false;
    req.on("data", (c) => {
      size += c.length;
      if (size > BODY_LIMIT) {
        /* Stop keeping it, keep reading it. The first version destroyed the
           request here, which killed the connection before the 413 could be
           written -- the client got ECONNRESET instead of an answer, and a
           reset is the one response the browser cannot turn into "your
           application did not send, here is your mail client".

           Draining costs the rest of an oversized upload on the wire and
           buys a real HTTP status. In practice the platform's own limit
           stops most of these before this code runs at all. */
        over = true;
        parts.length = 0;
        return;
      }
      if (!over) parts.push(c);
    });
    req.on("end", () => {
      if (over) reject(Object.assign(new Error("too large"), { tooLarge: true }));
      else resolve(Buffer.concat(parts));
    });
    req.on("error", reject);
  });
}

export default async function handler(a, b) {
  if (!b || typeof b.end !== "function") return handle(a);

  const req = a, res = b;
  const proto = req.headers["x-forwarded-proto"] || "https";
  const host = req.headers["x-forwarded-host"] || req.headers.host || "localhost";
  const url = proto + "://" + host + (req.url || "/");

  let body = null;
  if (req.method !== "GET" && req.method !== "HEAD" && req.method !== "OPTIONS") {
    try {
      body = await readBody(req);
    } catch (e) {
      res.statusCode = e && e.tooLarge ? 413 : 400;
      res.setHeader("content-type", "application/json; charset=utf-8");
      res.end(JSON.stringify({ ok: false, error: e && e.tooLarge ? "body too large" : "body" }));
      return;
    }
  }

  let out;
  try {
    out = await handle(new Request(url, {
      method: req.method,
      headers: req.headers,
      body: body && body.length ? body : undefined,
    }));
  } catch (e) {
    console.error("[form] handler threw:", e && e.stack || e);
    res.statusCode = 500;
    res.setHeader("content-type", "application/json; charset=utf-8");
    res.end(JSON.stringify({ ok: false, error: "server" }));
    return;
  }

  res.statusCode = out.status;
  out.headers.forEach((v, k) => res.setHeader(k, v));
  res.end(Buffer.from(await out.arrayBuffer()));
}

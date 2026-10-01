/* The client's door into the content, and it does not go through GitHub.
 *
 * WHY NOT GITHUB
 * The obvious editor -- Sveltia or Decap on a GitHub backend -- signs the
 * client in with a GitHub account and commits as him. That means giving him an
 * account on a private repository that holds the whole site: the build, the
 * form endpoint, this file. He asked to edit vacancies and news. Handing over
 * the source to achieve that is the wrong trade, and it cannot be walked back
 * once he has the clone.
 *
 * So the door is ours. He signs in with a password we issue. The GitHub token
 * lives in this function's environment and never leaves the server -- the
 * browser never sees it, and there is no request a browser can make that
 * returns it. He cannot read the repository because he is never talking to it.
 *
 * WHAT HE CAN REACH
 * Six files, by name, from a list compiled here. The collection name from the
 * query string is only ever used to look up an entry in that list; the path
 * sent to GitHub is built from the entry, never from his string. There is no
 * input that produces a path outside content/, including the obvious ones --
 * "../tools/build-pages", an absolute path, a URL. Nothing else in the
 * repository is reachable through this function at all.
 *
 * WHAT HAPPENS AFTER A SAVE
 * The commit lands on main and touches content/, which is what
 * .github/workflows/rebuild-on-content.yml waits for. It builds the pages,
 * translates, and commits the HTML back. Vercel deploys that. The client sees
 * his change on the site a couple of minutes later without anything else being
 * pressed.
 *
 * CONFIGURATION, none of which is in this file or in the repository
 *   CMS_PASSWORD_HASH    scrypt$<N>$<salt hex>$<hash hex>, from tools/cms-pass.py
 *   CMS_SESSION_SECRET   random, 32 bytes or more; signs the session cookie
 *   GITHUB_TOKEN         fine-grained PAT, Contents: read and write, THIS repo
 *   GITHUB_REPO          owner/name            (default aldy-lab/alprojects)
 *   GITHUB_BRANCH        the production branch (default main)
 *
 * With any of the first three missing every action answers 503 and says so,
 * rather than pretending to save. The same rule as the form endpoint: an
 * unconfigured endpoint must not look like a working one.
 */

import crypto from "node:crypto";

const BODY_LIMIT = 2 * 1024 * 1024;      /* a collection file, with room */
const SESSION_HOURS = 12;
const COOKIE = "cms_session";

/* The whole of what this function can touch. The value is the path; the key is
   the only thing a request may name. */
const COLLECTIONS = {
  positions: "content/positions.json",
  articles:  "content/articles.json",
  cases:     "content/cases.json",
  services:  "content/services.json",
  sectors:   "content/sectors.json",
  site:      "content/site.json",
  /* The per-id translations for the collections he owns. A vacancy's Russian
     used to live in tools/lang_ru.py, and a Python file is the one thing this
     endpoint exists to keep him out of. These carry a fingerprint of the
     English each line was made from, so the build can tell an edit from an
     omission -- see client_store() in tools/i18n_build.py. */
  "t-ru": "content/translations/ru.json",
  "t-fr": "content/translations/fr.json",
  "t-de": "content/translations/de.json",
  "t-it": "content/translations/it.json",
};

/* What may be uploaded, and how it is recognised. The extension is what the
   file is called; the magic bytes are what it is. Both have to agree, because
   a name is the client's and the bytes are the file's -- and the one that
   decides what a browser does with it is the bytes. */
const IMAGES = [
  { ext: "jpg",  type: "image/jpeg", magic: [0xFF, 0xD8, 0xFF] },
  { ext: "png",  type: "image/png",  magic: [0x89, 0x50, 0x4E, 0x47] },
  { ext: "webp", type: "image/webp", magic: [0x52, 0x49, 0x46, 0x46] },
];
const IMAGE_LIMIT = 12 * 1024 * 1024;   /* a phone photograph, with room */

function sniff(buf) {
  for (const k of IMAGES)
    if (k.magic.every(function (b, i) { return buf[i] === b; })) return k;
  return null;
}

/* A name the client typed becomes a file name in the repository, so it is
   rebuilt here from scratch rather than cleaned: lowercase, a-z 0-9 and the
   hyphen, nothing else, and the extension comes from the bytes. There is no
   input that produces a path -- no slash, no dot, no "..", no leading dash --
   because none of those characters survive. */
function safeStem(name) {
  return String(name || "")
    .replace(/\.[^.]*$/, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 60) || "photo";
}

const json = (status, body, headers) =>
  new Response(JSON.stringify(body), {
    status,
    headers: Object.assign(
      { "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store" },
      headers || {}),
  });

/* ---------------------------------------------------------------- password */

/* scrypt, not a bare comparison and not sha256: the password is short and
   human-chosen, and the only thing standing between it and the content is how
   long a guess takes. The parameters travel inside the hash so they can be
   raised later without invalidating what is already set. */
function checkPassword(given, stored) {
  const parts = String(stored || "").split("$");
  if (parts.length !== 4 || parts[0] !== "scrypt") return false;
  const N = parseInt(parts[1], 10);
  if (!Number.isFinite(N) || N < 1024) return false;
  let salt, want;
  try {
    salt = Buffer.from(parts[2], "hex");
    want = Buffer.from(parts[3], "hex");
  } catch { return false; }
  if (!salt.length || !want.length) return false;
  let got;
  try {
    got = crypto.scryptSync(String(given), salt, want.length, { N, r: 8, p: 1,
                                                                maxmem: 128 * N * 8 * 2 });
  } catch { return false; }
  return got.length === want.length && crypto.timingSafeEqual(got, want);
}

/* ----------------------------------------------------------------- session */

/* A signed expiry, nothing else. There is one user and no state to keep, so a
   cookie that proves "somebody knew the password before <time>" is the whole
   requirement -- and it needs no store, which on this platform would mean
   another service to run and another thing to leak. */
function mint(secret) {
  const exp = Date.now() + SESSION_HOURS * 3600 * 1000;
  const sig = crypto.createHmac("sha256", secret).update(String(exp)).digest("hex");
  return exp + "." + sig;
}

function valid(token, secret) {
  const [exp, sig] = String(token || "").split(".");
  if (!exp || !sig) return false;
  const want = crypto.createHmac("sha256", secret).update(exp).digest("hex");
  const a = Buffer.from(sig, "utf8"), b = Buffer.from(want, "utf8");
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return false;
  return Number(exp) > Date.now();
}

function cookieFrom(header, name) {
  for (const part of String(header || "").split(";")) {
    const i = part.indexOf("=");
    if (i > 0 && part.slice(0, i).trim() === name) return part.slice(i + 1).trim();
  }
  return null;
}

const setCookie = (value, maxAge) =>
  COOKIE + "=" + value + "; Path=/; Max-Age=" + maxAge +
  "; HttpOnly; Secure; SameSite=Lax";

/* ------------------------------------------------------------------ GitHub */

async function gh(path, env, init) {
  const repo = env.GITHUB_REPO || "aldy-lab/alprojects";
  const res = await fetch("https://api.github.com/repos/" + repo + "/contents/" + path +
                          (init ? "" : "?ref=" + encodeURIComponent(env.GITHUB_BRANCH || "main")),
    Object.assign({
      headers: {
        authorization: "Bearer " + env.GITHUB_TOKEN,
        accept: "application/vnd.github+json",
        "user-agent": "alprojects-cms",
      },
    }, init || {}));
  return res;
}

/* The same leaves tools/content.py flatten() produces, so an id built here
   means the same field it means everywhere else. Underscore keys are structure
   and are skipped; a list is numbered from 1 because the ids end up in front
   of a person. */
function flatten(node, prefix, out) {
  out = out || {};
  if (Array.isArray(node)) {
    node.forEach((v, i) => flatten(v, prefix + "." + (i + 1), out));
  } else if (node && typeof node === "object") {
    for (const k of Object.keys(node)) {
      if (k.startsWith("_")) continue;
      flatten(node[k], prefix ? prefix + "." + k : k, out);
    }
  } else if (typeof node === "string" && node.trim()) {
    out[prefix] = node;
  }
  return out;
}

/* --------------------------------------------------------------- the shape */

/* A save that breaks _order builds a site with a record nobody can reach, or
   an order naming a record that is not there. The editor should never send
   either, which is exactly why it is checked here: the rule belongs where it
   cannot be skipped by a bug in the page, and the page is the part a future
   version replaces. */
function shapeError(before, after) {
  if (!after || typeof after !== "object" || Array.isArray(after))
    return "the file must be a JSON object";
  if (!Array.isArray(before._order)) return null;       /* not a collection */
  if (!Array.isArray(after._order)) return "_order is missing";
  const keys = new Set(Object.keys(after).filter((k) => !k.startsWith("_")));
  for (const slug of after._order)
    if (!keys.has(slug)) return "_order names a record that is not in the file: " + slug;
  for (const k of keys)
    if (!after._order.includes(k)) return "a record is not in _order: " + k;
  return null;
}

/* -------------------------------------------------------------------- main */

export async function handle(request, env) {
  env = env || process.env;
  const url = new URL(request.url);
  const action = url.searchParams.get("a") || "";
  const configured = !!(env.CMS_PASSWORD_HASH && env.CMS_SESSION_SECRET && env.GITHUB_TOKEN);
  const signedIn = configured &&
    valid(cookieFrom(request.headers.get("cookie"), COOKIE), env.CMS_SESSION_SECRET);

  /* Answered before anything else so the sign-in page can tell "not set up
     yet" from "wrong password" without guessing from a failure. */
  if (action === "session" && request.method === "GET")
    return json(200, { ok: true, configured, signedIn });

  if (!configured)
    return json(503, { ok: false, configured: false,
                       error: "the editor is not configured on this deployment" });

  if (action === "login") {
    if (request.method !== "POST") return json(405, { ok: false, error: "POST" });
    let body;
    try { body = await request.json(); } catch { return json(400, { ok: false, error: "body" }); }
    /* Constant cost on the way out whatever the answer: scrypt already makes a
       guess expensive, and this keeps the two outcomes from being told apart
       by how long they took. */
    const ok = checkPassword(body && body.password, env.CMS_PASSWORD_HASH);
    await new Promise((r) => setTimeout(r, 250));
    if (!ok) return json(401, { ok: false, error: "wrong password" });
    return json(200, { ok: true },
                { "set-cookie": setCookie(mint(env.CMS_SESSION_SECRET), SESSION_HOURS * 3600) });
  }

  if (action === "logout")
    return json(200, { ok: true }, { "set-cookie": setCookie("", 0) });

  if (!signedIn) return json(401, { ok: false, error: "sign in first" });

  /* The only place a request's string meets a path, and it meets it as a key
     in a table rather than as a path. */
  const name = url.searchParams.get("f") || "";
  const path = Object.prototype.hasOwnProperty.call(COLLECTIONS, name)
    ? COLLECTIONS[name] : null;

  /* The photograph goes in as the client sent it -- original bytes, whatever
     the phone produced. This function has no image library and no business
     having one: tools/thumbs.py derives the 1200 and 900 webp on the next
     build, reads the real pixel size off the result, and the record keeps
     pointing at "uploads/<name>". See adopt_uploads(). */
  if (action === "upload") {
    if (request.method !== "POST") return json(405, { ok: false, error: "POST" });
    const buf = Buffer.from(await request.arrayBuffer());
    if (!buf.length) return json(400, { ok: false, error: "empty" });
    if (buf.length > IMAGE_LIMIT)
      return json(413, { ok: false, error: "больше 12 МБ" });
    const kind = sniff(buf);
    if (!kind)
      return json(415, { ok: false, error: "только JPEG, PNG или WebP" });
    const stem = safeStem(url.searchParams.get("name"));
    const rel = "assets/uploads/" + stem + "." + kind.ext;

    /* Overwriting somebody else's photograph by picking the same file name is
       a quiet way to change a page nobody was editing, so an existing name
       gets a suffix instead. */
    let target = rel, n = 1;
    while (n < 50) {
      const probe = await gh(target, env);
      if (probe.status === 404) break;
      target = "assets/uploads/" + stem + "-" + (++n) + "." + kind.ext;
    }

    const put = await gh(target, env, {
      method: "PUT",
      headers: {
        authorization: "Bearer " + env.GITHUB_TOKEN,
        accept: "application/vnd.github+json",
        "user-agent": "alprojects-cms",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        message: "Upload " + target.split("/").pop() + "\n\nSent from the editor at /admin.",
        content: buf.toString("base64"),
        branch: env.GITHUB_BRANCH || "main",
      }),
    });
    if (!put.ok) return json(502, { ok: false, error: "github " + put.status });
    /* The value the record wants, so the page can set the field without
       knowing how any of this is laid out. */
    return json(200, { ok: true, img: target.replace(/^assets\//, "") });
  }

  /* ---------------------------------------------------------- translate
     Machine translation, asked for explicitly and marked as machine when it
     lands. The client wanted an edit in English to reach the other languages
     without waiting for anybody, and the alternative -- an English line in the
     middle of a Russian page -- is the thing he was complaining about.
     Two things keep it from being worse than that:
       - content/glossary.json forces the trade terms. Left to itself a
         translator model renders "TIG welding" as "сварка TIG"; a welder reads
         "аргонодуговая сварка", and the certificate he holds says so. The
         Russian half of that file is the terminology block from lang_ru.py,
         where every choice is argued.
       - the examples are real pairs out of the human translations already in
         the repository, so the register comes from a translator rather than
         from the model's idea of a register.
     The editor stores what comes back with by:"machine", and the panel says so,
     so a reviewed line and a generated one never look alike. */
  if (action === "translate") {
    if (request.method !== "POST") return json(405, { ok: false, error: "POST" });
    if (!env.ANTHROPIC_API_KEY)
      return json(503, { ok: false, error: "machine translation is not configured" });
    const to = url.searchParams.get("to") || "";
    const LANGS = { ru: "Russian", fr: "French", de: "German", it: "Italian" };
    if (!LANGS[to]) return json(400, { ok: false, error: "unknown language" });

    let body;
    try { body = await request.json(); } catch { return json(400, { ok: false, error: "body" }); }
    const items = (body && body.items || []).filter(
      (i) => i && typeof i.id === "string" && typeof i.text === "string" && i.text.trim());
    if (!items.length) return json(400, { ok: false, error: "nothing to translate" });
    if (items.length > 60) return json(400, { ok: false, error: "too many at once" });

    /* The glossary, and examples mined from what is already translated. Both
       are best-effort: a missing glossary makes the result worse, not broken. */
    let glossary = {}, never = [];
    try {
      const g = await gh("content/glossary.json", env);
      if (g.ok) {
        const doc = JSON.parse(Buffer.from((await g.json()).content, "base64").toString("utf8"));
        glossary = (doc.terms && doc.terms[to]) || {};
        never = doc._never_translate || [];
      }
    } catch { /* keep going without it */ }

    const examples = [];
    try {
      const collection = items[0].id.split(".")[0];
      if (Object.prototype.hasOwnProperty.call(COLLECTIONS, collection)) {
        const [cRes, sRes] = await Promise.all([
          gh(COLLECTIONS[collection], env),
          gh("content/translations/" + to + ".json", env),
        ]);
        if (cRes.ok && sRes.ok) {
          const flat = flatten(JSON.parse(
            Buffer.from((await cRes.json()).content, "base64").toString("utf8")), collection);
          const store = JSON.parse(
            Buffer.from((await sRes.json()).content, "base64").toString("utf8"));
          for (const id of Object.keys(store)) {
            if (examples.length >= 12) break;
            const rec = store[id];
            if (rec && rec.t && flat[id] && rec.by !== "machine")
              examples.push([flat[id], rec.t]);
          }
        }
      }
    } catch { /* examples are a help, not a requirement */ }

    const rules = [
      "You are translating the copy of an industrial-services website into " + LANGS[to] + ".",
      "The company does welding, pipe fitting, mechanical installation, inspection and rope access on shipyards and industrial plants.",
      "Register: the trade language actually used on site by welders, fitters and supervisors. Not marketing prose, not a literal word-for-word rendering.",
      "Keep any inline HTML exactly as it appears, including attributes and the text inside <a> tags.",
      "Keep numbers, dates, rotation ratios such as 8 / 2, email addresses and URLs unchanged.",
      "Never translate these names, reproduce them letter for letter: " + never.join(", ") + ".",
      "Where a term appears in the glossary, use the glossary wording and not your own.",
    ].join("\n");

    const glossaryText = Object.keys(glossary).length
      ? "GLOSSARY (English -> required " + LANGS[to] + "):\n" +
        Object.keys(glossary).map((k) => k + " -> " + glossary[k]).join("\n")
      : "";
    const exampleText = examples.length
      ? "\n\nEXISTING TRANSLATIONS FROM THIS SITE, as the register to match:\n" +
        examples.map((p) => p[0] + "\n-> " + p[1]).join("\n\n")
      : "";

    const ask =
      "Translate each string. Reply with JSON only: an object whose keys are the ids " +
      "given and whose values are the translations. No other text.\n\n" +
      JSON.stringify(items.map((i) => ({ id: i.id, text: i.text })), null, 1);

    let out;
    try {
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "x-api-key": env.ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01",
          "content-type": "application/json",
        },
        body: JSON.stringify({
          model: env.ANTHROPIC_MODEL || "claude-sonnet-5",
          max_tokens: 8000,
          thinking: { type: "adaptive" },
          system: rules + (glossaryText ? "\n\n" + glossaryText : "") + exampleText,
          messages: [{ role: "user", content: ask }],
        }),
      });
      if (!res.ok)
        return json(502, { ok: false, error: "translator " + res.status });
      const msg = await res.json();
      const text = (msg.content || [])
        .filter((b) => b.type === "text").map((b) => b.text).join("");
      const m = text.match(/\{[\s\S]*\}/);
      if (!m) return json(502, { ok: false, error: "the translator did not return JSON" });
      out = JSON.parse(m[0]);
    } catch (e) {
      return json(502, { ok: false, error: "translator unreachable" });
    }

    /* Only ids that were asked for, and never an empty string: a blank would
       be written into the store and blank that line on the site, which is a
       worse outcome than the English it was meant to replace. */
    const clean = {};
    for (const i of items) {
      const v = out[i.id];
      if (typeof v === "string" && v.trim()) clean[i.id] = v.trim();
    }
    if (!Object.keys(clean).length)
      return json(502, { ok: false, error: "the translator returned nothing usable" });
    return json(200, { ok: true, out: clean, missing: items.length - Object.keys(clean).length });
  }

  if (action === "list" && request.method === "GET")
    return json(200, { ok: true, collections: Object.keys(COLLECTIONS) });

  if (!path) return json(404, { ok: false, error: "no such collection" });

  if (action === "load" && request.method === "GET") {
    const res = await gh(path, env);
    if (!res.ok) return json(502, { ok: false, error: "github " + res.status });
    const meta = await res.json();
    let data;
    try {
      data = JSON.parse(Buffer.from(meta.content, "base64").toString("utf8"));
    } catch { return json(502, { ok: false, error: "the stored file is not valid JSON" }); }
    return json(200, { ok: true, data, sha: meta.sha });
  }

  if (action === "save") {
    if (request.method !== "POST") return json(405, { ok: false, error: "POST" });
    let body;
    try { body = await request.json(); } catch { return json(400, { ok: false, error: "body" }); }
    if (!body || !body.sha) return json(400, { ok: false, error: "sha is required" });

    /* The sha is what makes two editors safe: GitHub refuses the write if the
       file moved since it was loaded, and the client is told to reload rather
       than silently overwriting whatever the translator just put in. */
    const current = await gh(path, env);
    if (!current.ok) return json(502, { ok: false, error: "github " + current.status });
    const before = JSON.parse(Buffer.from((await current.json()).content, "base64").toString("utf8"));

    const bad = shapeError(before, body.data);
    if (bad) return json(400, { ok: false, error: bad });

    const text = JSON.stringify(body.data, null, 2) + "\n";
    if (Buffer.byteLength(text) > BODY_LIMIT)
      return json(413, { ok: false, error: "too large" });

    const subject = String(body.message || "").trim().slice(0, 72) ||
                    ("Edit " + name + " in the editor");
    const res = await gh(path, env, {
      method: "PUT",
      headers: {
        authorization: "Bearer " + env.GITHUB_TOKEN,
        accept: "application/vnd.github+json",
        "user-agent": "alprojects-cms",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        message: subject + "\n\nSaved from the editor at /admin.",
        content: Buffer.from(text, "utf8").toString("base64"),
        sha: body.sha,
        branch: env.GITHUB_BRANCH || "main",
      }),
    });
    if (res.status === 409)
      return json(409, { ok: false, error: "somebody else saved this since you opened it -- reload" });
    if (!res.ok) return json(502, { ok: false, error: "github " + res.status });
    const out = await res.json();
    return json(200, { ok: true, sha: out.content && out.content.sha });
  }

  return json(404, { ok: false, error: "no such action" });
}

/* ---------------------------------------------------------- the adapter
   Vercel's Node runtime calls a function with (req, res), not with a Request.
   The form endpoint learned this in production -- a POST threw on
   headers.get and a GET timed out returning a Response nothing ever wrote.
   Same adapter here, for the same reason. */
function readBody(req) {
  return new Promise((resolve, reject) => {
    const parts = [];
    let size = 0, over = false;
    req.on("data", (c) => {
      size += c.length;
      if (size > BODY_LIMIT) { over = true; parts.length = 0; return; }
      parts.push(c);
    });
    req.on("end", () => {
      if (over) { const e = new Error("too large"); e.tooLarge = true; return reject(e); }
      resolve(Buffer.concat(parts));
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
      res.end(JSON.stringify({ ok: false, error: e && e.tooLarge ? "too large" : "body" }));
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
    console.error("[cms] handler threw:", (e && e.stack) || e);
    res.statusCode = 500;
    res.setHeader("content-type", "application/json; charset=utf-8");
    res.end(JSON.stringify({ ok: false, error: "server" }));
    return;
  }

  res.statusCode = out.status;
  out.headers.forEach((v, k) => res.setHeader(k, v));
  res.end(Buffer.from(await out.arrayBuffer()));
}

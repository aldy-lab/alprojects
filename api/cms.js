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

/* The editor endpoint. The cases that matter are the ones where a mistake is
   not visible from the outside: a path that escapes content/, a save that goes
   through without a session, an unconfigured deployment that answers as though
   it had saved. */
import test from "node:test";
import assert from "node:assert/strict";
import crypto from "node:crypto";
import { handle } from "../api/cms.js";

const N = 1024;                                   /* tests, not production */
const PASSWORD = "a long enough password";
const salt = crypto.randomBytes(16);
const hash = crypto.scryptSync(PASSWORD, salt, 32, { N, r: 8, p: 1, maxmem: 128 * N * 8 * 2 });

const ENV = {
  CMS_PASSWORD_HASH: `scrypt$${N}$${salt.toString("hex")}$${hash.toString("hex")}`,
  CMS_SESSION_SECRET: "secret for the tests only",
  GITHUB_TOKEN: "ghp_not_a_real_token",
  GITHUB_REPO: "aldy-lab/alprojects",
  GITHUB_BRANCH: "main",
};

const FILE = { _order: ["one"], one: { title: "One" } };
const b64 = (o) => Buffer.from(JSON.stringify(o)).toString("base64");

/* Every GitHub request the function makes, so a test can assert on the PATH it
   asked for -- which is the whole point of the allowlist. */
let calls = [];
globalThis.fetch = async (url, init) => {
  calls.push({ url: String(url), method: (init && init.method) || "GET" });
  if (init && init.method === "PUT")
    return new Response(JSON.stringify({ content: { sha: "newsha" } }), { status: 200 });
  return new Response(JSON.stringify({ content: b64(FILE), sha: "oldsha" }), { status: 200 });
};

const req = (path, opts = {}) =>
  new Request("https://alprojects.eu/api/cms" + path, {
    method: opts.method || "GET",
    headers: Object.assign({ "content-type": "application/json" }, opts.headers || {}),
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  });

async function signIn() {
  const r = await handle(req("?a=login", { method: "POST", body: { password: PASSWORD } }), ENV);
  assert.equal(r.status, 200);
  return r.headers.get("set-cookie").split(";")[0];
}

test("an unconfigured deployment refuses rather than pretending", async () => {
  const r = await handle(req("?a=load&f=positions"), { });
  assert.equal(r.status, 503);
  assert.equal((await r.json()).configured, false);
});

test("the session probe answers before configuration and says which it is", async () => {
  let r = await handle(req("?a=session"), {});
  assert.deepEqual(await r.json(), { ok: true, configured: false, signedIn: false });
  r = await handle(req("?a=session"), ENV);
  assert.deepEqual(await r.json(), { ok: true, configured: true, signedIn: false });
});

test("the wrong password does not sign anybody in", async () => {
  const r = await handle(req("?a=login", { method: "POST", body: { password: "nope" } }), ENV);
  assert.equal(r.status, 401);
  assert.equal(r.headers.get("set-cookie"), null);
});

test("the right password sets an HttpOnly, Secure, SameSite cookie", async () => {
  const r = await handle(req("?a=login", { method: "POST", body: { password: PASSWORD } }), ENV);
  assert.equal(r.status, 200);
  const c = r.headers.get("set-cookie");
  assert.match(c, /HttpOnly/);
  assert.match(c, /Secure/);
  assert.match(c, /SameSite=Lax/);
});

test("without a session nothing can be read or written", async () => {
  for (const p of ["?a=load&f=positions", "?a=list"]) {
    assert.equal((await handle(req(p), ENV)).status, 401);
  }
  const r = await handle(req("?a=save&f=positions",
    { method: "POST", body: { data: FILE, sha: "oldsha" } }), ENV);
  assert.equal(r.status, 401);
});

test("a forged cookie is not a session", async () => {
  const token = (Date.now() + 3600e3) + ".0000000000000000000000000000000000000000000000000000000000000000";
  const r = await handle(req("?a=load&f=positions", { headers: { cookie: "cms_session=" + token } }), ENV);
  assert.equal(r.status, 401);
});

test("an expired session is not a session", async () => {
  const exp = Date.now() - 1000;
  const sig = crypto.createHmac("sha256", ENV.CMS_SESSION_SECRET).update(String(exp)).digest("hex");
  const r = await handle(req("?a=load&f=positions",
    { headers: { cookie: `cms_session=${exp}.${sig}` } }), ENV);
  assert.equal(r.status, 401);
});

test("nothing outside content/ can be named, however it is spelled", async () => {
  const cookie = await signIn();
  const tries = [
    "../tools/build-pages.py", "../../etc/passwd", "/etc/passwd",
    "content/positions.json", "positions.json", ".github/workflows/rebuild-on-content.yml",
    "api/form.js", "..%2Ftools%2Fpaths.py", "__proto__", "constructor", "toString",
  ];
  for (const t of tries) {
    calls = [];
    const r = await handle(req("?a=load&f=" + encodeURIComponent(t), { headers: { cookie } }), ENV);
    assert.equal(r.status, 404, "should refuse: " + t);
    assert.equal(calls.length, 0, "must not reach GitHub at all for: " + t);
  }
});

test("a collection on the list is read, and only from content/", async () => {
  const cookie = await signIn();
  calls = [];
  const r = await handle(req("?a=load&f=positions", { headers: { cookie } }), ENV);
  assert.equal(r.status, 200);
  const body = await r.json();
  assert.deepEqual(body.data, FILE);
  assert.equal(body.sha, "oldsha");
  assert.equal(calls.length, 1);
  assert.match(calls[0].url, /\/contents\/content\/positions\.json\?ref=main$/);
});

test("a save that breaks _order is refused before it reaches GitHub", async () => {
  const cookie = await signIn();
  for (const [why, data] of [
    ["_order names a record that is not there", { _order: ["ghost"], one: { title: "One" } }],
    ["a record missing from _order", { _order: [], one: { title: "One" } }],
    ["not an object", ["one"]],
  ]) {
    calls = [];
    const r = await handle(req("?a=save&f=positions",
      { method: "POST", headers: { cookie }, body: { data, sha: "oldsha" } }), ENV);
    assert.equal(r.status, 400, why);
    assert.equal(calls.filter((c) => c.method === "PUT").length, 0, why);
  }
});

test("a save without a sha is refused -- that is what stops a silent overwrite", async () => {
  const cookie = await signIn();
  const r = await handle(req("?a=save&f=positions",
    { method: "POST", headers: { cookie }, body: { data: FILE } }), ENV);
  assert.equal(r.status, 400);
});

test("a good save commits to content/ on the production branch", async () => {
  const cookie = await signIn();
  calls = [];
  const next = { _order: ["one", "two"], one: { title: "One" }, two: { title: "Two" } };
  const r = await handle(req("?a=save&f=positions",
    { method: "POST", headers: { cookie },
      body: { data: next, sha: "oldsha", message: "Add a vacancy" } }), ENV);
  assert.equal(r.status, 200);
  const put = calls.find((c) => c.method === "PUT");
  assert.match(put.url, /\/contents\/content\/positions\.json$/);
});

test("a translation file has no _order and saves anyway", async () => {
  const cookie = await signIn();
  /* The shape check only applies to files that had an _order to begin with.
     The translation stores are flat maps of id -> {en, t}; a rule written for
     collections must not refuse them. */
  globalThis.fetch = async (url, init) => {
    calls.push({ url: String(url), method: (init && init.method) || "GET" });
    if (init && init.method === "PUT")
      return new Response(JSON.stringify({ content: { sha: "newsha" } }), { status: 200 });
    return new Response(JSON.stringify({
      content: Buffer.from(JSON.stringify({ "positions.one.title": { en: "abc", t: "Un" } })).toString("base64"),
      sha: "oldsha",
    }), { status: 200 });
  };
  calls = [];
  const r = await handle(req("?a=save&f=t-ru", {
    method: "POST", headers: { cookie },
    body: { data: { "positions.one.title": { en: "abc", t: "Один" } }, sha: "oldsha" },
  }), ENV);
  assert.equal(r.status, 200);
  assert.match(calls.find((c) => c.method === "PUT").url,
               /\/contents\/content\/translations\/ru\.json$/);
});

test("an upload is judged by its bytes, and its name cannot become a path", async () => {
  const cookie = await signIn();
  const JPEG = Buffer.concat([Buffer.from([0xFF, 0xD8, 0xFF]), Buffer.alloc(40, 7)]);

  /* 404 on the probe means "this name is free", which is the path a first
     upload takes. */
  globalThis.fetch = async (url, init) => {
    calls.push({ url: String(url), method: (init && init.method) || "GET" });
    if (init && init.method === "PUT")
      return new Response(JSON.stringify({ content: { sha: "s" } }), { status: 200 });
    return new Response("{}", { status: 404 });
  };

  /* A name that tries to be a path. Every one of them has to come out as a
     file directly inside assets/uploads/ -- one slash after uploads, no dots
     in the stem, and the extension decided by the magic bytes. */
  for (const name of ["../../tools/build-pages.py", "/etc/passwd", "a/b/c.jpg",
                      "..%2F..%2Fx", "....//x.jpg", ".bashrc", "-rf", "шеллкод.jpg"]) {
    calls = [];
    const r = await handle(new Request(
      "https://alprojects.eu/api/cms?a=upload&name=" + encodeURIComponent(name),
      { method: "POST", headers: { cookie }, body: JPEG }), ENV);
    assert.equal(r.status, 200, name);
    const got = (await r.json()).img;
    assert.match(got, /^uploads\/[a-z0-9-]+\.jpg$/, name + " -> " + got);
    const put = calls.find((c) => c.method === "PUT");
    assert.match(put.url, /\/contents\/assets\/uploads\/[a-z0-9-]+\.jpg$/, name);
  }

  /* A .jpg name over PNG bytes is a PNG. */
  calls = [];
  const PNG = Buffer.concat([Buffer.from([0x89, 0x50, 0x4E, 0x47]), Buffer.alloc(40, 1)]);
  let r = await handle(new Request("https://alprojects.eu/api/cms?a=upload&name=shot.jpg",
    { method: "POST", headers: { cookie }, body: PNG }), ENV);
  assert.match((await r.json()).img, /\.png$/);

  /* Anything that is not one of the three is refused before it is stored. */
  calls = [];
  r = await handle(new Request("https://alprojects.eu/api/cms?a=upload&name=x.jpg",
    { method: "POST", headers: { cookie }, body: Buffer.from("<?php echo 1; ?>") }), ENV);
  assert.equal(r.status, 415);
  assert.equal(calls.filter((c) => c.method === "PUT").length, 0);

  /* And no session, no upload. */
  r = await handle(new Request("https://alprojects.eu/api/cms?a=upload&name=x.jpg",
    { method: "POST", body: JPEG }), ENV);
  assert.equal(r.status, 401);
});

test("an upload does not overwrite a photograph that is already there", async () => {
  const cookie = await signIn();
  const JPEG = Buffer.concat([Buffer.from([0xFF, 0xD8, 0xFF]), Buffer.alloc(40, 7)]);
  let seen = 0;
  globalThis.fetch = async (url, init) => {
    if (init && init.method === "PUT") {
      calls.push({ url: String(url), method: "PUT" });
      return new Response(JSON.stringify({ content: { sha: "s" } }), { status: 200 });
    }
    /* The first two names exist, the third does not. */
    return new Response("{}", { status: ++seen <= 2 ? 200 : 404 });
  };
  calls = [];
  const r = await handle(new Request("https://alprojects.eu/api/cms?a=upload&name=crane.jpg",
    { method: "POST", headers: { cookie }, body: JPEG }), ENV);
  assert.equal((await r.json()).img, "uploads/crane-3.jpg");
  assert.match(calls.find((c) => c.method === "PUT").url, /crane-3\.jpg$/);
});

test("GET cannot save, POST cannot be swapped for it", async () => {
  const cookie = await signIn();
  const r = await handle(req("?a=save&f=positions", { headers: { cookie } }), ENV);
  assert.equal(r.status, 405);
});

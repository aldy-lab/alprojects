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

test("GET cannot save, POST cannot be swapped for it", async () => {
  const cookie = await signIn();
  const r = await handle(req("?a=save&f=positions", { headers: { cookie } }), ENV);
  assert.equal(r.status, 405);
});

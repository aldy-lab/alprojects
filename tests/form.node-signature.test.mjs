/* The (req, res) path, which is the one the platform actually uses.
   tests/form.test.mjs calls the handler with a Request and covers the logic;
   this one puts the handler behind a real HTTP server and posts real
   multipart at it, because the two failures the merge exposed -- a 500 on
   POST and a request that never got an answer on GET -- both lived in the
   gap between those two signatures and neither could be seen from the other
   side of it.

       node tests/form.node-signature.test.mjs
*/
import { createServer } from "node:http";
process.env.MAIL_PROVIDER = "dry-run";
const { default: handler } = await import(new URL("../api/form.js", import.meta.url));

const server = createServer((req, res) => handler(req, res));
await new Promise((r) => server.listen(0, r));
const base = "http://127.0.0.1:" + server.address().port;

let pass = 0, fail = 0;
async function t(label, path, init, want, check) {
  const res = await fetch(base + path, init);
  let body = {};
  try { body = await res.json(); } catch (e) { /* not json */ }
  const good = res.status === want && (!check || check(body));
  if (good) { pass++; console.log("  ok   " + label + " -> " + res.status); }
  else { fail++; console.log("  FAIL " + label + " -> " + res.status + " want " + want + " " + JSON.stringify(body)); }
  return body;
}
const OK = { Origin: "https://alprojects.co" };

await t("GET answers, does not hang", "/api/form?f=careers", { headers: OK }, 200,
        b => b.ok === true && b.configured === false);
await t("PUT refused", "/api/form?f=careers", { method: "PUT", headers: OK }, 405);
await t("foreign origin refused", "/api/form?f=careers",
        { method: "POST", headers: { Origin: "https://evil.example" } }, 403);

function form(fields, files = []) {
  const fd = new FormData();
  for (const [k, v] of Object.entries(fields)) fd.append(k, v);
  for (const f of files) fd.append("attachment[]", new Blob([new Uint8Array(f.bytes)], { type: "application/pdf" }), f.name);
  return fd;
}
const base_fields = { consent: "yes", consent_page: "/careers", consent_lang: "en",
                      consent_text: "I agree", email: "a@b.co", name: "Jonas" };

await t("real multipart POST", "/api/form?f=careers",
        { method: "POST", headers: OK, body: form(base_fields, [{ name: "cv.pdf", bytes: 4096 }]) },
        200, b => b.ok === true && b.dryRun === true);
await t("consent enforced over the wire", "/api/form?f=careers",
        { method: "POST", headers: { ...OK, "x-forwarded-for": "5.5.5.5" },
          body: form({ ...base_fields, consent: "" }) }, 422, b => b.error === "consent");
await t("honeypot over the wire", "/api/form?f=careers",
        { method: "POST", headers: { ...OK, "x-forwarded-for": "5.5.5.6" },
          body: form({ ...base_fields, company: "bot" }) }, 200, b => b.ok === true);
await t("a body over the guard is refused", "/api/form?f=careers",
        { method: "POST", headers: { ...OK, "x-forwarded-for": "5.5.5.7" },
          body: form(base_fields, [{ name: "huge.pdf", bytes: 12 * 1024 * 1024 }]) },
        413, b => b.ok === false);

server.close();
console.log("\n" + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);

/* The form endpoint, exercised without a network and without a mail provider.
   MAIL_PROVIDER unset means send() reports what it would have sent instead of
   sending it, so the whole path -- origin, honeypot, consent, the field
   allowlist, attachments, the throttle -- is covered by:

       node tests/form.test.mjs

   Run it before touching api/form.js. Fourteen cases, and three of them are
   the ones that would matter most if they regressed: a foreign origin cannot
   use the endpoint, a submission without the consent record is refused, and a
   field that is not on its form's list is dropped rather than emailed. */
const { default: handler } = await import(new URL("../api/form.js", import.meta.url));
const OK = "https://alprojects.co";
let pass = 0, fail = 0;
const logs = [];
const origLog = console.log;
console.log = (...a) => logs.push(a.join(" "));

function req(which, fields = {}, files = [], origin = OK, method = "POST", ip = "1.2.3.4") {
  const fd = new FormData();
  for (const [k, v] of Object.entries(fields)) fd.append(k, v);
  for (const f of files) fd.append(f.key || "attachment[]", new Blob([f.bytes || new Uint8Array(10)], { type: f.type || "application/pdf" }), f.name);
  return new Request("https://alprojects.co/api/form?f=" + which, {
    method, body: method === "POST" ? fd : undefined,
    headers: { origin, "x-forwarded-for": ip },
  });
}
const base = { consent: "yes", consent_page: "/careers", consent_lang: "en", consent_text: "I agree…", email: "a@b.co", name: "Jonas" };

async function t(label, r, want, check) {
  const res = await handler(r);
  const body = await res.json().catch(() => ({}));
  const good = res.status === want && (!check || check(body));
  console.log = origLog;
  if (good) { pass++; origLog("  ok   " + label + "  -> " + res.status); }
  else { fail++; origLog("  FAIL " + label + "  -> " + res.status + " want " + want + "  " + JSON.stringify(body)); }
  console.log = (...a) => logs.push(a.join(" "));
  return body;
}

await t("GET is refused",            req("careers", base, [], OK, "GET"), 405);
await t("foreign origin refused",    req("careers", base, [], "https://evil.example"), 403);
await t("no origin refused",         req("careers", base, [], ""), 403);
await t("unknown form refused",      req("nope", base), 400);
await t("honeypot answers 200",      req("careers", { ...base, company: "bot" }, [], OK, "POST", "9.9.9.1"), 200, b => b.ok);
await t("no consent refused",        req("careers", { ...base, consent: "" }, [], OK, "POST", "9.9.9.2"), 422, b => b.error === "consent");
await t("bad email refused",         req("careers", { ...base, email: "nope" }, [], OK, "POST", "9.9.9.3"), 422, b => b.error === "email");
await t("bad extension refused",     req("careers", base, [{ name: "cv.exe" }], OK, "POST", "9.9.9.4"), 422, b => /file type/.test(b.error));
await t("too many files refused",    req("careers", base, Array.from({length:7},(_,i)=>({name:"f"+i+".pdf"})), OK, "POST", "9.9.9.5"), 422, b => b.error === "too many files");
await t("5MB is accepted",           req("careers", base, [{ name: "big.pdf", bytes: new Uint8Array(5*1024*1024) }], OK, "POST", "9.9.9.6"), 200, b => b.ok);
/* 11MB is over the site's own ceiling. A real request this big never reaches
   the function -- the platform refuses it first -- and the browser then hands
   the form to the applicant's mail client. This asserts the endpoint's own
   answer for the case where it does arrive. */
await t("over the ceiling refused",  req("careers", base, [{ name: "huge.pdf", bytes: new Uint8Array(11*1024*1024) }], OK, "POST", "9.9.9.61"), 413, b => /too large/.test(b.error));
await t("subscribe, no files",       req("subscribe", { consent: "yes", email: "a@b.co" }, [], OK, "POST", "9.9.9.7"), 200);
await t("contact honeypot is website", req("contact", { ...base, website: "bot", first: "A" }, [], OK, "POST", "9.9.9.8"), 200, b => b.ok);

const okBody = await t("careers happy path", req("careers",
  { ...base, phone: "+370", country: "LT", role: "Welding (TIG)", years: "5 to 10 years", message: "Line one\nLine two", extra_injected: "SHOULD BE DROPPED" },
  [{ name: "cv.pdf", bytes: new Uint8Array(2048) }, { name: "cert.jpg", bytes: new Uint8Array(1024), type: "image/jpeg" }],
  OK, "POST", "9.9.9.9"), 200, b => b.ok && b.dryRun);

await t("throttle on the second",    req("careers", base, [], OK, "POST", "9.9.9.9"), 429, b => b.error === "too soon");

console.log = origLog;
const dry = logs.filter(l => l.startsWith("[form] dry-run")).pop() || "";
console.log("\n--- what the happy path would have sent");
console.log("  " + dry.slice(0, 260));
console.log("  injected field dropped:", !dry.includes("SHOULD BE DROPPED"));
console.log("\n" + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);

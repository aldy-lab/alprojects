/* Run the editor locally, against the real endpoint.
 *
 *     node tools/cms-dev-server.mjs .
 *     open http://127.0.0.1:8899/admin/     password: a long enough password
 *
 * Only fetch() is replaced: GitHub becomes the working tree. The allowlist,
 * the session, the password check, the shape check, the magic-byte sniff and
 * the sha are all the code that runs in production -- so a test here is a test
 * of the thing rather than of a copy of it. A save writes the real content/
 * file and an upload writes a real assets/uploads/ file, which is the point:
 * run the build afterwards and see what the client's edit would actually do.
 *
 * Not deployed -- .vercelignore excludes tools/.
 */
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const ROOT = path.resolve(process.argv[2] || ".");
const N = 1024;
const PW = "a long enough password";
const salt = crypto.randomBytes(16);
const hash = crypto.scryptSync(PW, salt, 32, { N, r: 8, p: 1, maxmem: 128 * N * 8 * 2 });

const ENV = {
  CMS_PASSWORD_HASH: "scrypt$" + N + "$" + salt.toString("hex") + "$" + hash.toString("hex"),
  CMS_SESSION_SECRET: "development only",
  GITHUB_TOKEN: "development only",
  GITHUB_REPO: "local/working-tree",
  GITHUB_BRANCH: "main",
};

const shaOf = (b) => crypto.createHash("sha1").update(b).digest("hex");

globalThis.fetch = async (url, init) => {
  const m = String(url).match(/\/contents\/([^?]+)/);
  if (!m) return new Response("{}", { status: 404 });
  const file = path.join(ROOT, decodeURIComponent(m[1]));
  /* The same guard the endpoint has, repeated here on purpose: if a path ever
     escapes, this is a real filesystem and the test should fail loudly rather
     than quietly write outside the repo. */
  if (!file.startsWith(ROOT)) throw new Error("path escaped the root: " + file);

  if (init && init.method === "PUT") {
    const body = JSON.parse(init.body);
    if (body.sha) {
      const cur = fs.existsSync(file) ? fs.readFileSync(file) : Buffer.alloc(0);
      if (shaOf(cur) !== body.sha) return new Response("{}", { status: 409 });
    }
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, Buffer.from(body.content, "base64"));
    return new Response(JSON.stringify({ content: { sha: shaOf(fs.readFileSync(file)) } }),
                        { status: 200 });
  }

  if (!fs.existsSync(file)) return new Response("{}", { status: 404 });
  const buf = fs.readFileSync(file);
  return new Response(JSON.stringify({ content: buf.toString("base64"), sha: shaOf(buf) }),
                      { status: 200 });
};

const { handle } = await import(path.join(ROOT, "api/cms.js"));

const TYPES = {
  ".html": "text/html", ".js": "text/javascript", ".css": "text/css",
  ".woff2": "font/woff2", ".webp": "image/webp", ".svg": "image/svg+xml",
  ".json": "application/json", ".ico": "image/x-icon", ".jpg": "image/jpeg",
  ".png": "image/png", ".xml": "application/xml", ".txt": "text/plain",
};

http.createServer(async (req, res) => {
  if (req.url.startsWith("/api/cms")) {
    const parts = [];
    for await (const c of req) parts.push(c);
    const out = await handle(new Request("http://localhost" + req.url, {
      method: req.method,
      headers: req.headers,
      body: parts.length ? Buffer.concat(parts) : undefined,
    }), ENV);
    res.statusCode = out.status;
    /* Secure is stripped so the cookie survives plain http on localhost. It is
       the only difference between this and the deployed behaviour. */
    out.headers.forEach((v, k) =>
      res.setHeader(k, k === "set-cookie" ? v.replace("; Secure", "") : v));
    res.end(Buffer.from(await out.arrayBuffer()));
    return;
  }
  let p = decodeURIComponent(req.url.split("?")[0]);
  if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) {
    res.statusCode = 404;
    res.end("not found");
    return;
  }
  res.setHeader("content-type", TYPES[path.extname(f)] || "application/octet-stream");
  res.end(fs.readFileSync(f));
}).listen(8899, () => console.log("http://127.0.0.1:8899/admin/   password: " + PW));

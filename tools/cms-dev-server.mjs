/* Run the editor locally, against the real endpoint.
 *
 *     node tools/cms-dev-server.mjs .     then open http://127.0.0.1:8899/admin/
 *     password: a long enough password
 *
 * Only fetch() is replaced: GitHub becomes the working tree. The allowlist,
 * the session, the password check, the shape check and the sha are all the
 * code that runs in production -- so a test here is a test of the thing, not
 * of a copy of it. A save writes the real content/ file, which is the point:
 * run the build afterwards and see what the client's edit would do.
 *
 * Not deployed: .vercelignore excludes tools/.
 */
  CMS_PASSWORD_HASH: `scrypt$${N}$${salt.toString("hex")}$${hash.toString("hex")}`,
  CMS_SESSION_SECRET: "dev", GITHUB_TOKEN: "dev", GITHUB_REPO: "x/y", GITHUB_BRANCH: "main",
};

const shaOf = (b) => crypto.createHash("sha1").update(b).digest("hex");
globalThis.fetch = async (url, init) => {
  const m = String(url).match(/\/contents\/([^?]+)/);
  const file = path.join(ROOT, decodeURIComponent(m[1]));
  if (init && init.method === "PUT") {
    const body = JSON.parse(init.body);
    const cur = fs.readFileSync(file);
    if (shaOf(cur) !== body.sha)
      return new Response("{}", { status: 409 });
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
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css",
                ".woff2": "font/woff2", ".webp": "image/webp", ".svg": "image/svg+xml",
                ".json": "application/json", ".ico": "image/x-icon" };

http.createServer(async (req, res) => {
  if (req.url.startsWith("/api/cms")) {
    let body = [];
    for await (const c of req) body.push(c);
    const out = await handle(new Request("http://localhost" + req.url, {
      method: req.method, headers: req.headers,
      body: body.length ? Buffer.concat(body) : undefined,
    }), ENV);
    res.statusCode = out.status;
    out.headers.forEach((v, k) => res.setHeader(k, k === "set-cookie" ? v.replace("; Secure", "") : v));
    res.end(Buffer.from(await out.arrayBuffer()));
    return;
  }
  let p = decodeURIComponent(req.url.split("?")[0]);
  if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) {
    res.statusCode = 404; res.end("not found"); return;
  }
  res.setHeader("content-type", TYPES[path.extname(f)] || "application/octet-stream");
  res.end(fs.readFileSync(f));
}).listen(8899, () => console.log("ready"));

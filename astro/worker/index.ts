/**
 * Password gate for /private/*.
 *
 * Only this path runs the Worker (see `run_worker_first` in wrangler.jsonc);
 * every other request is served straight from static assets.
 *
 * Files live in an R2 bucket, not in the repository — this repo is public, so
 * anything committed here would be readable by anyone regardless of the gate.
 *
 * Secrets (set with `wrangler secret put <NAME>`, never committed):
 *   PRIVATE_PASSWORD  the shared password handed out to readers
 *   COOKIE_SECRET     random string used to sign the session cookie
 */

interface Env {
  ASSETS: { fetch: (request: Request) => Promise<Response> };
  PRIVATE_FILES: R2Bucket;
  PRIVATE_PASSWORD: string;
  COOKIE_SECRET: string;
}

interface R2Bucket {
  get(key: string): Promise<R2ObjectBody | null>;
  list(options?: { prefix?: string; cursor?: string }): Promise<R2Objects>;
}

interface R2ObjectBody {
  body: ReadableStream;
  size: number;
  httpEtag: string;
  httpMetadata?: { contentType?: string };
  key: string;
}

interface R2Objects {
  objects: { key: string; size: number; uploaded: Date }[];
  truncated: boolean;
  cursor?: string;
}

const COOKIE = "hio_private";
const SESSION_SECONDS = 60 * 60 * 12;

const encoder = new TextEncoder();

/** Compare without leaking length or position through timing. */
function safeEqual(a: string, b: string): boolean {
  const ab = encoder.encode(a);
  const bb = encoder.encode(b);
  if (ab.length !== bb.length) return false;
  let diff = 0;
  for (let i = 0; i < ab.length; i++) diff |= ab[i] ^ bb[i];
  return diff === 0;
}

async function sign(value: string, secret: string): Promise<string> {
  const key = await crypto.subtle.importKey("raw", encoder.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, [
    "sign",
  ]);
  const mac = await crypto.subtle.sign("HMAC", key, encoder.encode(value));
  return [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function issueToken(secret: string): Promise<string> {
  const expiry = String(Date.now() + SESSION_SECONDS * 1000);
  return `${expiry}.${await sign(expiry, secret)}`;
}

async function tokenIsValid(token: string | undefined, secret: string): Promise<boolean> {
  if (!token) return false;
  const [expiry, mac] = token.split(".");
  if (!expiry || !mac) return false;
  if (!Number(expiry) || Number(expiry) < Date.now()) return false;
  return safeEqual(mac, await sign(expiry, secret));
}

function readCookie(request: Request, name: string): string | undefined {
  const header = request.headers.get("Cookie");
  if (!header) return undefined;
  for (const part of header.split(";")) {
    const [k, ...rest] = part.trim().split("=");
    if (k === name) return rest.join("=");
  }
  return undefined;
}

function page(title: string, body: string, status = 200): Response {
  return new Response(
    `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>${title} · Frank Huettner</title>
<style>
  :root{--bg:#fdfdfd;--soft:#fff;--ink:#000;--muted:#828282;--rule:#ececec;--accent:#b71c1c;--radius:.5rem;color-scheme:light}
  @media(prefers-color-scheme:dark){:root{--bg:#1c1c1d;--soft:#212529;--ink:#e8e8e8;--muted:#a3a3a8;--rule:#313134;--accent:#f35e5e;color-scheme:dark}}
  *{box-sizing:border-box}
  body{margin:0;min-height:100vh;display:grid;place-items:center;padding:2rem;
    background:var(--bg);color:var(--ink);
    font:400 16px/1.6 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
  main{width:100%;max-width:26rem}
  h1{font-size:1.4rem;letter-spacing:-.022em;margin:0 0 .4rem}
  p{color:var(--muted);margin:0 0 1.4rem;font-size:.9rem}
  form{display:flex;gap:.5rem}
  input{flex:1;height:2.4rem;padding:0 .7rem;border:1px solid var(--rule);border-radius:.375rem;
    background:var(--soft);color:var(--ink);font:inherit;font-size:.9rem}
  input:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  button{height:2.4rem;padding:0 .9rem;border:1px solid var(--accent);border-radius:.375rem;
    background:var(--accent);color:#fff;font:inherit;font-size:.85rem;font-weight:500;cursor:pointer}
  .err{color:var(--accent);font-size:.85rem;margin:0 0 1rem}
  ul{list-style:none;margin:0;padding:0}
  li{border-bottom:1px solid var(--rule)}
  li a{display:flex;justify-content:space-between;gap:1rem;padding:.7rem .2rem;
    color:var(--ink);text-decoration:none;font-size:.9rem}
  li a:hover{color:var(--accent)}
  .size{color:var(--muted);font-size:.78rem;white-space:nowrap}
  .back{display:inline-block;margin-top:1.6rem;color:var(--muted);font-size:.82rem}
</style></head><body><main>${body}</main></body></html>`,
    { status, headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" } },
  );
}

function loginPage(error?: string): Response {
  return page(
    "Protected",
    `<h1>Protected area</h1>
     <p>These files are shared with a password.</p>
     ${error ? `<p class="err">${error}</p>` : ""}
     <form method="post" autocomplete="on">
       <input type="password" name="password" placeholder="Password" aria-label="Password" autofocus required>
       <button type="submit">Enter</button>
     </form>
     <a class="back" href="/">← huettner.io</a>`,
    // 401 either way: the body is a login form, never protected content, so no
    // cache or crawler should treat this response as the resource.
    401,
  );
}

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 ** 2) return `${(bytes / 1024).toFixed(0)} KB`;
  return `${(bytes / 1024 ** 2).toFixed(1)} MB`;
}

async function listing(env: Env): Promise<Response> {
  const items: { key: string; size: number }[] = [];
  let cursor: string | undefined;

  do {
    const batch = await env.PRIVATE_FILES.list({ cursor });
    items.push(...batch.objects.map((o) => ({ key: o.key, size: o.size })));
    cursor = batch.truncated ? batch.cursor : undefined;
  } while (cursor);

  items.sort((a, b) => a.key.localeCompare(b.key));

  const rows = items.length
    ? items
        .map(
          (o) =>
            `<li><a href="/private/${encodeURI(o.key)}"><span>${o.key}</span><span class="size">${formatSize(o.size)}</span></a></li>`,
        )
        .join("")
    : `<li><a><span>No files yet.</span></a></li>`;

  return page("Protected", `<h1>Files</h1><p>${items.length} item(s).</p><ul>${rows}</ul><a class="back" href="/">← huettner.io</a>`);
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (!url.pathname.startsWith("/private")) return env.ASSETS.fetch(request);

    if (!env.PRIVATE_PASSWORD || !env.COOKIE_SECRET) {
      return page("Not configured", "<h1>Not configured</h1><p>PRIVATE_PASSWORD and COOKIE_SECRET are not set.</p>", 503);
    }

    // Submitted the password.
    if (request.method === "POST") {
      const form = await request.formData();
      const supplied = String(form.get("password") ?? "");

      if (!safeEqual(supplied, env.PRIVATE_PASSWORD)) return loginPage("Wrong password.");

      const token = await issueToken(env.COOKIE_SECRET);
      return new Response(null, {
        status: 303,
        headers: {
          Location: url.pathname,
          "Set-Cookie": `${COOKIE}=${token}; Path=/private; HttpOnly; Secure; SameSite=Lax; Max-Age=${SESSION_SECONDS}`,
          "Cache-Control": "no-store",
        },
      });
    }

    if (!(await tokenIsValid(readCookie(request, COOKIE), env.COOKIE_SECRET))) return loginPage();

    const key = decodeURIComponent(url.pathname.replace(/^\/private\/?/, ""));
    if (!key) return listing(env);

    const object = await env.PRIVATE_FILES.get(key);
    if (!object) return page("Not found", '<h1>Not found</h1><p>No such file.</p><a class="back" href="/private/">← Files</a>', 404);

    return new Response(object.body, {
      headers: {
        "Content-Type": object.httpMetadata?.contentType ?? "application/octet-stream",
        "Content-Length": String(object.size),
        ETag: object.httpEtag,
        // Private, per-user content: never store it in a shared cache.
        "Cache-Control": "private, no-store",
        "X-Robots-Tag": "noindex, nofollow",
      },
    });
  },
};

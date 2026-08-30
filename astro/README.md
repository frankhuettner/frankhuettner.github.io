# huettner.io

Personal academic site — [Astro](https://astro.build) 7, static output.

The public site is served by **GitHub Pages** at huettner.io, exactly as before.
A separate **Cloudflare Worker** hosts a password-protected file area. The two
are independent: no DNS change is needed, and the live site is never at risk
from the private area.

Replaces the al-folio Jekyll starter (38 Ruby gems, a fork to keep merging) with
~6 direct dependencies and no upstream to track. A full build takes about a second.

## Develop

```bash
npm ci
npm run dev      # http://localhost:4321
npm run build    # → dist/
npm run preview  # serve dist/
```

## Where content lives

| What | Where |
| ---- | ----- |
| Bio on the homepage | `src/content/pages/about.md` |
| News items | `src/content/news/*.md` (front matter: `date`) |
| Projects | `src/content/projects/*.md` |
| Publications | `src/data/papers.bib` — plain BibTeX, parsed at build |
| Images, PDFs, files | `public/assets/…` (URLs preserved from the old site) |

The "BibTeX" disclosure shows the entry verbatim from the source file rather
than a re-serialisation, so what a visitor copies is what you wrote.

Adding a paper means adding a BibTeX entry. Recognised fields: `title`, `author`,
`year`, `journal`, `volume`, `number`, `pages`, `doi`, `html`, `pdf`, `arxiv`,
`abstract`, `keywords`, and `selected={true}` to feature it on the homepage.
Duplicate fields (`year = {forthcoming}` next to `year = {2026}`) are handled.

A project with a body gets its own page at `/projects/<id>/`; one without links
straight out to its `url` or `repo`.

Front matter is schema-validated in `src/content.config.ts` — a typo fails the
build instead of silently rendering an empty page.

## Design

Palette and type carry over from the al-folio site: near-white `#fdfdfd`, black
text, the red accent (`#b71c1c` light / `#f35e5e` dark) and the pink dividers
from `_sass/_variables.scss`. Inter replaces the old Roboto, self-hosted at build
time by Astro's font pipeline — no CDN, no third-party request at runtime.

Tokens live at the top of `src/styles/global.css`; light and dark palettes are
defined there and the theme is set before first paint. Dense list separators use
`--rule-soft` so the pink `--rule` stays for section bands, where the original
used it.

Pages ship **zero JavaScript** apart from two small inline scripts (theme toggle,
Abstract/BibTeX disclosures). Math renders to HTML at build time via KaTeX — no
runtime MathJax.

## Deploy

### The public site → GitHub Pages

```bash
npm run build   # → dist/, including CNAME and .nojekyll
```

`.github/workflows/deploy-pages.yml` does this and force-pushes `dist/` to
`gh-pages`. It is **manual-only (`workflow_dispatch`) on purpose**: that branch
is what serves huettner.io today, so running it replaces the live site. Once you
have cut over, give it a `push` trigger on `main` and delete the old
al-folio `deploy.yml`.

Two files in `public/` matter for Pages and must not be removed:

- `CNAME` — keeps the huettner.io custom domain
- `.nojekyll` — without it Pages runs Jekyll, which strips Astro's `_astro/`
  directory and the site loads unstyled

Because Pages cannot do `_redirects`, the old al-folio URLs (`/blog`, `/cv`,
`/teaching`, `/repositories`, `/dropdown`) are emitted as real redirect pages
via the `redirects` block in `astro.config.mjs`.

### Moving the whole site to Cloudflare later

Optional, and a separate decision. It requires moving the DNS zone to
Cloudflare, because Worker custom domains and routes both need the zone there —
a CNAME from another registrar to `workers.dev` does not work. In exchange you
get `/private` on your own domain, real `_headers`/`_redirects` (both files are
already in `public/`), and one deploy instead of two. Uncomment the `assets`
block in `wrangler.jsonc` and the same Worker serves both.

## Password-protected area

A standalone Cloudflare Worker, separate from the public site. It **fails
closed**: every request reaching it is gated, so nothing depends on route
configuration being correct. Deployed on its own `*.workers.dev` hostname —
that is the trade-off for leaving DNS alone.

**Files live in an R2 bucket, never in this repository — the repo is public,
so anything committed here is readable by anyone regardless of the gate.**

One-time setup:

```bash
npx wrangler r2 bucket create huettner-io-private
npx wrangler secret put PRIVATE_PASSWORD    # the password you hand out
npx wrangler secret put COOKIE_SECRET       # e.g. openssl rand -hex 32
```

Uploading a presentation — either drag-and-drop in the Cloudflare dashboard
(R2 → huettner-io-private), or:

```bash
npx wrangler r2 object put huettner-io-private/lecture-01.pdf \
  --file=./lecture-01.pdf --content-type application/pdf
```

It then appears in the file list at the Worker's URL, behind the password.

To link the area from the public site, set `PRIVATE_AREA_URL` in `src/site.ts`
to the Worker's URL. A discreet "private" link then appears in the footer;
leave it empty and nothing is rendered.

How the gate works: the password is compared in constant time, and on success
the Worker sets an HMAC-signed, `HttpOnly` `Secure` `SameSite=Lax` cookie that
carries its own expiry (12 h). Unauthenticated requests get a 401 with the
login form — never file bytes. Responses are `private, no-store` and
`X-Robots-Tag: noindex`.

Deploy it with `npx wrangler deploy`, or the
`deploy-private-worker.yml` workflow (needs `CLOUDFLARE_API_TOKEN` and
`CLOUDFLARE_ACCOUNT_ID` secrets).

Local development: put `PRIVATE_PASSWORD` and `COOKIE_SECRET` in `.dev.vars`
(gitignored) and run `npx wrangler dev`, which simulates R2 on disk.

If you would rather have per-person access than a shared password — say,
anyone with an `@skku.edu` address, with a one-time code by email —
Cloudflare Access does that in front of the same path with no code at all.

## Not carried over from al-folio

- **CV page** — `_data/cv.yml` was still Albert Einstein.
- **Teaching page** — was still placeholder text.
- **Blog** — the only post was the tikzjax starter demo.
- **Search** — Pagefind drops in cleanly if wanted; left out because the whole
  site is six pages and every paper is on one of them.

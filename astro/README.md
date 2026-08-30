# huettner.io

Personal academic site — [Astro](https://astro.build) 7, static output, deployed to
Cloudflare Workers.

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

Adding a paper means adding a BibTeX entry. Recognised fields: `title`, `author`,
`year`, `journal`, `volume`, `number`, `pages`, `doi`, `html`, `pdf`, `arxiv`,
`abstract`, `keywords`, and `selected={true}` to feature it on the homepage.
Duplicate fields (`year = {forthcoming}` next to `year = {2026}`) are handled.

A project with a body gets its own page at `/projects/<id>/`; one without links
straight out to its `url` or `repo`.

Front matter is schema-validated in `src/content.config.ts` — a typo fails the
build instead of silently rendering an empty page.

## Design

Two self-hosted families (Source Serif 4, IBM Plex Mono), downloaded at build
time by Astro's font pipeline — no CDN, no third-party request at runtime.
Tokens live at the top of `src/styles/global.css`; light and dark palettes are
defined there and the toggle is set before first paint.

Pages ship **zero JavaScript** apart from two small inline scripts (theme toggle,
abstract disclosure). Math renders to HTML at build time via KaTeX — no runtime
MathJax.

## Deploy

Cloudflare Workers static assets, configured in `wrangler.jsonc`.

```bash
npx wrangler deploy          # needs `npx wrangler login` once
```

CI deploys on push via `.github/workflows/deploy-cloudflare.yml`, which needs two
repository secrets: `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

`public/_redirects` keeps old al-folio URLs (`/blog/`, `/cv/`, `/teaching/`,
`/repositories/`) from 404ing. `public/_headers` sets cache and security headers.

## Not carried over from al-folio

- **CV page** — `_data/cv.yml` was still Albert Einstein.
- **Teaching page** — was still placeholder text.
- **Blog** — the only post was the tikzjax starter demo.
- **Search** — Pagefind drops in cleanly if wanted; left out because the whole
  site is six pages and every paper is on one of them.

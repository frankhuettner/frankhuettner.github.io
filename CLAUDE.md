# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this is

The personal academic site of Frank Huettner, at huettner.io. Two independent
pieces:

- **`astro/`** — the public site. Astro 7, static output, deployed to GitHub
  Pages. Also contains `worker/`, the Cloudflare Worker serving the
  password-gated download area from an R2 bucket.
- **`admin/`** — a thin wrapper around R2-Explorer, giving a file manager over
  that same bucket under separate credentials.

Read `astro/README.md` and `admin/README.md` before changing either.

## Things that will bite you

- **pnpm, not npm.** Both projects use pnpm; the CI workflows use
  `pnpm install --frozen-lockfile`.
- **`astro/public/CNAME` and `astro/public/.nojekyll` must survive.** Without
  the first the custom domain drops; without the second GitHub Pages runs
  Jekyll, which strips Astro's `_astro/` directory and the site loads
  unstyled.
- **Publications come from `astro/src/data/papers.bib`.** They are parsed at
  build time, including duplicate fields such as `year = {forthcoming}`
  alongside `year = {2026}`. Do not hand-maintain a second list.
- **Deploys are manual on purpose.** `deploy-pages.yml` force-pushes to
  `gh-pages`, which serves the live site.
- **The reader password and the admin credentials are deliberately separate.**
  The reader password is handed out for downloads and must never grant delete
  or rename.
- **Protected files belong in R2, never in this repo.** The repository is
  public.

## Design

Palette and type carry over from the previous al-folio site: near-white
`#fdfdfd`, black text, red accent (`#b71c1c` light, `#f35e5e` dark), pink
section dividers, Inter. Tokens sit at the top of
`astro/src/styles/global.css`. Structural elements follow shadcn conventions
(`--radius`, `--shadow-*`, `.btn`, `.badge`).

Pages ship zero JavaScript apart from two inline scripts: the theme toggle and
the Abstract/BibTeX disclosures. Math renders at build time via KaTeX.

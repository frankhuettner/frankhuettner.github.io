# huettner.io

Personal academic site of Frank Huettner.

| | |
| --- | --- |
| [`astro/`](astro) | The public site (Astro, static) and the password-gated download area (Cloudflare Worker) |
| [`admin/`](admin) | File manager for the protected files (R2-Explorer, Cloudflare Worker) |

Each directory has its own README with setup and deploy instructions.

## Quick reference

```bash
cd astro && pnpm install && pnpm dev     # http://localhost:4321
```

Deploys are manual:

- **Site** — `gh workflow run deploy-pages.yml` (builds `astro/`, force-pushes to `gh-pages`)
- **Download area** — `cd astro && pnpm wrangler deploy`
- **File manager** — `cd admin && pnpm wrangler deploy`

## History

This was a fork of [al-folio](https://github.com/alshedivat/al-folio) until
August 2026, when the site was rebuilt on Astro and the al-folio scaffolding
removed. The old Jekyll site remains in the git history.

## Licensing

`LICENSE` splits the repository in two: the **code** is MIT, the **content** —
the portrait, the paper PDFs, the bibliography and the written text — is not,
and stays all rights reserved. A single MIT file at the root would have implied
the photo and the papers were free to reuse, which they are not.

To roll the live site back to the last al-folio build:

```bash
git push --force origin d3cd5e2ee3a4a14f846d27a837bb776a723b4123:gh-pages
```

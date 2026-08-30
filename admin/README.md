# Admin file manager

[R2-Explorer](https://github.com/G4brym/R2-Explorer) over the same
`huettner-io-private` bucket the reader-facing Worker in `../astro` serves
from. Upload with drag-and-drop and progress, create folders, rename, delete.

## Why this is separate

The password in `../astro/worker` is handed to anyone who should *download* a
file. It must not also grant delete and rename. This Worker is the admin side
and has its own credentials. Both point at one bucket, so anything uploaded
here appears in the reader listing immediately.

## Setup

```bash
npm install
npx wrangler secret put ADMIN_USER
npx wrangler secret put ADMIN_PASSWORD
npx wrangler deploy
```

It fails closed: with the secrets unset it answers 503 rather than exposing an
unauthenticated file manager.

Local: put `ADMIN_USER` / `ADMIN_PASSWORD` in `.dev.vars` (gitignored) and run
`npx wrangler dev`.

## What is and is not protected

`run_worker_first` is scoped to `/api/*` and `/share/*`, so:

- **every operation that touches the bucket is behind basic auth** — verified:
  401 without credentials, 401 with wrong ones
- the empty dashboard shell is publicly loadable and carries no file names

That is R2-Explorer's design, not a misconfiguration. Setting
`run_worker_first: true` to cover the shell as well does not work: the Worker
then has to serve the dashboard assets itself and every page 500s.

Unlike the upstream template, the credentials are read from secrets rather
than hardcoded in `src/index.ts`, so nothing sensitive is in this repo.

## Updating

`npm update r2-explorer && npx wrangler deploy`. The dashboard is shipped
inside the package (`node_modules/r2-explorer/dashboard`), so `npm install`
must run before every deploy — the CI workflow does this.

/**
 * Admin file manager for the private-files bucket (R2-Explorer).
 *
 * Deliberately separate from the reader-facing password gate in ../astro:
 * that password is handed out to anyone who should download a file, and it
 * must not also grant delete or rename. This Worker is the admin side and
 * carries its own credentials.
 *
 * Both point at the same bucket, so a file uploaded here shows up in the
 * reader listing straight away.
 *
 * Secrets (`wrangler secret put <NAME>`, never committed):
 *   ADMIN_USER
 *   ADMIN_PASSWORD
 */
import { R2Explorer } from "r2-explorer";

interface Env {
  ADMIN_USER?: string;
  ADMIN_PASSWORD?: string;
}

export default {
  async fetch(request: Request, env: Env, context: ExecutionContext): Promise<Response> {
    // Fail closed: without credentials configured, serve nothing rather than
    // an unauthenticated file manager.
    if (!env.ADMIN_USER || !env.ADMIN_PASSWORD) {
      return new Response("Not configured: ADMIN_USER and ADMIN_PASSWORD are unset.", {
        status: 503,
        headers: { "Content-Type": "text/plain", "Cache-Control": "no-store" },
      });
    }

    // Built per request so the credentials come from secrets rather than
    // being baked into the source, as the upstream template does.
    return R2Explorer({
      readonly: false,
      basicAuth: { username: env.ADMIN_USER, password: env.ADMIN_PASSWORD },
    }).fetch(request, env, context);
  },
};

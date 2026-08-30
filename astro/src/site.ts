/**
 * Site-wide constants.
 *
 * Both point at Worker deployments on *.workers.dev; attaching huettner.io to
 * them would require moving DNS to Cloudflare — see README. Set either to ""
 * and its footer link disappears.
 */

/** Reader-facing download area. Shared password. */
export const PRIVATE_AREA_URL = "https://huettner-private.dawn-darkness-5c7f.workers.dev/";

/** Admin file manager. Separate credentials; only useful to the site owner. */
export const ADMIN_AREA_URL = "https://huettner-admin.dawn-darkness-5c7f.workers.dev/";

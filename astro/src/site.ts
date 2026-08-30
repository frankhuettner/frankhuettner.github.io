/**
 * Site-wide constants.
 *
 * PRIVATE_AREA_URL is the deployed private-files Worker. Leave it empty and no
 * link is rendered; set it and a discreet "private" link appears in the footer.
 * It lives on a *.workers.dev hostname because attaching huettner.io to a
 * Worker would require moving DNS to Cloudflare — see README.
 */
export const PRIVATE_AREA_URL = "https://huettner-private.dawn-darkness-5c7f.workers.dev/";

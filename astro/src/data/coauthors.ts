/**
 * Co-author homepages, keyed by last name.
 *
 * Matching ignores case and diacritics, so "beal" catches "Béal" and
 * "remila" catches "Rémila". `firstNames` disambiguates people sharing a
 * surname; a one- or two-letter entry matches an initial ("A" → "André").
 *
 * Carried over from the al-folio site's _data/coauthors.yml.
 */
export interface Coauthor {
  firstNames: string[];
  url: string;
}

export const coauthors: Record<string, Coauthor[]> = {
  casajus: [{ firstNames: ["André", "A"], url: "https://home.uni-leipzig.de/casajus/" }],
  akcay: [{ firstNames: ["Yalçın"], url: "https://mbs.edu/faculty-and-research/faculty/yalcin-akcay" }],
  boyaci: [{ firstNames: ["Tamer"], url: "https://faculty-research.esmt.berlin/person/tamer-boyaci/bio" }],
  remila: [{ firstNames: ["Eric"], url: "https://scholar.google.com/citations?user=znSHN2EAAAAJ&hl=en" }],
  wiese: [
    {
      firstNames: ["Harald"],
      url: "https://www.wifa.uni-leipzig.de/institut-fuer-theoretische-volkswirtschaftslehre/professuren/mikrooekonomik",
    },
  ],
  sunder: [
    {
      firstNames: ["Marco"],
      url: "https://www.frankfurt-university.de/en/about-us/faculty-3-business-and-law/contacts-at-faculty-3/professors-at-faculty-3/marco-sunder/",
    },
  ],
  solal: [{ firstNames: ["Philippe"], url: "https://www.gate.cnrs.fr/spip.php?article880&lang=fr" }],
  beal: [{ firstNames: ["Sylvain"], url: "https://sites.google.com/site/bealpage/" }],
  basteck: [{ firstNames: ["Christian"], url: "https://sites.google.com/site/christianbasteck/" }],
  funaki: [{ firstNames: ["Yukihiko"], url: "https://yfunaki.blogspot.com/" }],
};

/**
 * Letters Unicode decomposition cannot strip, because they are distinct
 * letters rather than a base plus an accent — Turkish dotless "ı" in Boyacı
 * being the one that actually occurs here.
 */
const INDIVISIBLE: Record<string, string> = {
  "\u0131": "i", // ı  dotless i
  "\u0130": "i", // İ  capital i with dot
  ø: "o",
  Ø: "o",
  ł: "l",
  Ł: "l",
  đ: "d",
  Đ: "d",
  ß: "ss",
  æ: "ae",
  Æ: "ae",
  œ: "oe",
  Œ: "oe",
};

const fold = (s: string) =>
  s
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .replace(/[^\u0000-\u007F]/g, (c) => INDIVISIBLE[c] ?? c)
    .toLowerCase()
    .trim();

export function coauthorUrl(firstName: string, lastName: string): string | undefined {
  const entries = coauthors[fold(lastName)];
  if (!entries) return undefined;

  const given = fold(firstName);
  for (const entry of entries) {
    for (const candidate of entry.firstNames) {
      const known = fold(candidate);
      // Exact match, or a stored initial matching the start of the given name.
      if (known === given || (known.length <= 2 && given.startsWith(known))) return entry.url;
    }
  }
  return undefined;
}

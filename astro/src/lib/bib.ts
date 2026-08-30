import { parse } from "@retorquere/bibtex-parser";
import raw from "../data/papers.bib?raw";
import { coauthorUrl } from "../data/coauthors";

export interface Paper {
  key: string;
  type: string;
  title: string;
  authors: { name: string; isSelf: boolean; url?: string }[];
  year: number;
  yearLabel: string;
  venue: string | null;
  volume?: string;
  number?: string;
  pages?: string;
  abstract?: string;
  preview?: string;
  keywords: string[];
  links: { label: string; href: string }[];
  selected: boolean;
  /** The verbatim BibTeX entry, for the "BibTeX" disclosure. */
  bibtex?: string;
}

const SELF = "huettner";

/**
 * BibTeX entries here sometimes repeat a field (`year = {forthcoming}` next to
 * `year = {2026}`); the parser exposes the repeats as `year+duplicate-1`.
 * Collect every variant so callers can pick the one they want.
 */
function allValues(fields: Record<string, unknown>, ...names: string[]): string[] {
  const out: string[] = [];
  for (const name of names) {
    for (const key of Object.keys(fields)) {
      if (key !== name && !key.startsWith(`${name}+`)) continue;
      const v = fields[key];
      const str = typeof v === "string" ? v : Array.isArray(v) && typeof v[0] === "string" ? v[0] : undefined;
      if (str?.trim()) out.push(str.trim());
    }
  }
  return out;
}

function field(fields: Record<string, unknown>, ...names: string[]): string | undefined {
  return allValues(fields, ...names)[0];
}

/**
 * `year` appears twice in some entries (e.g. `year = {forthcoming}` alongside
 * `year = {2026}`), which the parser exposes as `year+duplicate-1`. Prefer a
 * real number and keep the prose variant as the display label.
 */
function resolveYear(fields: Record<string, unknown>): { year: number; label: string } {
  const candidates = allValues(fields, "year");

  const numeric = candidates.map((c) => parseInt(c, 10)).find((n) => !Number.isNaN(n));
  const prose = candidates.find((c) => Number.isNaN(parseInt(c, 10)));
  return { year: numeric ?? 0, label: prose ?? String(numeric ?? "") };
}

function truthy(v: string | undefined): boolean {
  return v === "true" || v === "yes" || v === "1";
}

function buildLinks(fields: Record<string, unknown>): { label: string; href: string }[] {
  const links: { label: string; href: string }[] = [];
  const html = field(fields, "html", "url", "URL");
  const pdf = field(fields, "pdf");
  const arxiv = field(fields, "arxiv", "eprint");
  const doi = field(fields, "doi");

  // Preprints carry a 10.48550/arXiv.* DOI; that is the arXiv link, not a journal.
  const htmlIsArxiv = Boolean(html && /arxiv\.org/i.test(html));
  const doiIsArxiv = Boolean(doi && /arxiv/i.test(doi));

  // The DOI is the canonical publisher link, and nearly every entry here carries
  // both `doi` and an `html` that resolves to the same article (13 of them are
  // literally https://doi.org/<doi>). So prefer the DOI and only fall back to
  // `html` when there is no usable DOI — otherwise the row shows one destination
  // twice under two names.
  if (doi && !doiIsArxiv) links.push({ label: "DOI", href: `https://doi.org/${doi}` });
  else if (html && !htmlIsArxiv) links.push({ label: "Journal", href: html });

  if (arxiv) links.push({ label: "arXiv", href: `https://arxiv.org/abs/${arxiv}` });
  else if (htmlIsArxiv && html) links.push({ label: "arXiv", href: html });

  if (pdf) links.push({ label: "PDF", href: pdf.startsWith("http") ? pdf : `/assets/pdf/${pdf}` });

  return links;
}

/**
 * Pull each entry back out of the source verbatim, so the BibTeX shown on the
 * page is exactly what is in papers.bib rather than a re-serialisation.
 */
function extractRawEntries(src: string): Map<string, string> {
  const entries = new Map<string, string>();
  const header = /@(\w+)\s*\{\s*([^,\s]+)\s*,/g;

  for (let match = header.exec(src); match; match = header.exec(src)) {
    const start = match.index;
    let depth = 0;

    for (let i = src.indexOf("{", start); i < src.length; i++) {
      if (src[i] === "{") depth++;
      else if (src[i] === "}" && --depth === 0) {
        entries.set(match[2], src.slice(start, i + 1));
        break;
      }
    }
  }

  return entries;
}

function loadPapers(): Paper[] {
  // Strip the Jekyll front-matter fences if the file is ever re-copied verbatim.
  const source = raw.replace(/^\s*(---\s*\n)+/, "");
  const bib = parse(source);
  const rawEntries = extractRawEntries(source);

  const papers = bib.entries.map((entry): Paper => {
    const fields = entry.fields as Record<string, unknown>;
    const { year, label } = resolveYear(fields);

    const creators = (entry.fields.author ?? []) as Array<{
      lastName?: string;
      firstName?: string;
      name?: string;
    }>;

    const authors = creators.map((c) => {
      const name = c.name ?? [c.firstName, c.lastName].filter(Boolean).join(" ");
      const isSelf = (c.lastName ?? "").toLowerCase() === SELF;
      return {
        name,
        isSelf,
        url: isSelf ? undefined : coauthorUrl(c.firstName ?? "", c.lastName ?? ""),
      };
    });

    return {
      key: entry.key,
      type: entry.type,
      title: field(fields, "title") ?? entry.key,
      authors,
      year,
      yearLabel: label,
      venue:
        field(fields, "journal", "journaltitle", "booktitle", "publisher") ??
        (entry.type === "misc" || entry.type === "unpublished" ? "Working paper" : null),
      volume: field(fields, "volume"),
      number: field(fields, "number"),
      pages: allValues(fields, "pages").find((v) => /\d/.test(v)) ?? field(fields, "pages"),
      abstract: field(fields, "abstract"),
      preview: field(fields, "preview"),
      keywords: (field(fields, "keywords") ?? "")
        .split(",")
        .map((k) => k.trim())
        .filter(Boolean),
      links: buildLinks(fields),
      selected: truthy(field(fields, "selected")),
      bibtex: rawEntries.get(entry.key),
    };
  });

  return papers.sort((a, b) => b.year - a.year || a.title.localeCompare(b.title));
}

export const papers = loadPapers();
export const selectedPapers = papers.filter((p) => p.selected);

export function papersByYear(): { year: number; items: Paper[] }[] {
  const groups = new Map<number, Paper[]>();
  for (const p of papers) {
    if (!groups.has(p.year)) groups.set(p.year, []);
    groups.get(p.year)!.push(p);
  }
  return [...groups.entries()]
    .sort((a, b) => b[0] - a[0])
    .map(([year, items]) => ({ year, items }));
}

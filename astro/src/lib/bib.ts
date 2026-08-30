import { parse } from "@retorquere/bibtex-parser";
import raw from "../data/papers.bib?raw";

export interface Paper {
  key: string;
  type: string;
  title: string;
  authors: { name: string; isSelf: boolean }[];
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

function buildLinks(fields: Record<string, unknown>, key: string): { label: string; href: string }[] {
  const links: { label: string; href: string }[] = [];
  const html = field(fields, "html", "url", "URL");
  const pdf = field(fields, "pdf");
  const arxiv = field(fields, "arxiv", "eprint");
  const doi = field(fields, "doi");

  const htmlIsArxiv = Boolean(html && /arxiv\.org/i.test(html));

  if (html && !htmlIsArxiv) links.push({ label: "Journal", href: html });
  if (pdf) links.push({ label: "PDF", href: pdf.startsWith("http") ? pdf : `/assets/pdf/${pdf}` });
  if (arxiv) links.push({ label: "arXiv", href: `https://arxiv.org/abs/${arxiv}` });
  else if (htmlIsArxiv && html) links.push({ label: "arXiv", href: html });
  if (doi && !html?.includes(doi) && !/arxiv/i.test(doi)) links.push({ label: "DOI", href: `https://doi.org/${doi}` });
  return links;
}

function loadPapers(): Paper[] {
  // Strip the Jekyll front-matter fences if the file is ever re-copied verbatim.
  const bib = parse(raw.replace(/^\s*(---\s*\n)+/, ""));

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
      return { name, isSelf: (c.lastName ?? "").toLowerCase() === SELF };
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
      links: buildLinks(fields, entry.key),
      selected: truthy(field(fields, "selected")),
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

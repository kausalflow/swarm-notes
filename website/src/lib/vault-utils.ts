/**
 * Utility functions for vault entry metadata extraction and formatting.
 */

/** Format a date from the CSL issued.date-parts array [[YYYY, M, D]] */
export function formatIssuedDate(issued: any): string | null {
  const parts = issued?.['date-parts']?.[0];
  if (!parts || parts.length < 1) return null;
  const [y, m, d] = parts;
  const dt = new Date(y, (m ?? 1) - 1, d ?? 1);
  return dt.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

/** Pull first N author family/literal names */
export function formatAuthors(authors: any[], max = 3): string {
  if (!authors?.length) return '';
  const names = authors.slice(0, max).map((a: any) => {
    if (a.literal) {
      // If it's a full name in literal, just take the last part as family name for the list view
      const parts = a.literal.trim().split(' ');
      return parts[parts.length - 1];
    }
    return a.family || a.literal || '';
  });
  const suffix = authors.length > max ? ` +${authors.length - max}` : '';
  return names.join(', ') + suffix;
}

/** Get the most recent timestamp from an entry for sorting */
export function getMostRecentTimestamp(entry: any): number {
  const modified = entry?.data?.modified_at ? Date.parse(String(entry.data.modified_at)) : NaN;
  if (!Number.isNaN(modified)) return modified;
  const created = entry?.data?.created_at ? Date.parse(String(entry.data.created_at)) : NaN;
  if (!Number.isNaN(created)) return created;
  return 0;
}

/** 
 * Enriches a vault entry with common metadata fields for list views.
 */
export function enrichVaultEntry(entry: any) {
  const vaultIndex = entry.filePath?.indexOf('vault/');
  const realSlug = (entry.filePath && vaultIndex !== -1)
    ? entry.filePath.substring(vaultIndex + 6).replace(/\.md$/, '')
    : entry.id;
  
  const parts = realSlug.split('/');
  const section = parts.length > 1 ? parts[0] : 'root';
  const data = entry.data as any;

  return {
    title: data?.title || parts[parts.length - 1],
    href: `/${realSlug}/`,
    section,
    sortTimestamp: getMostRecentTimestamp(entry),
    // Paper fields
    authors: data?.author ? formatAuthors(data.author) : '',
    domain: data?.domain || '',
    tags: (data?.tags as string[] | undefined)?.slice(0, 3) ?? [],
    arxiv_id: data?.arxiv_id || '',
    date: formatIssuedDate(data?.issued) || (data?.created_at ? new Date(String(data.created_at)).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }) : ''),
    // Open-question fields
    source_paper_count: (data?.source_papers as string[] | undefined)?.length ?? 0,
    // Original entry data
    rawData: data,
    realSlug
  };
}

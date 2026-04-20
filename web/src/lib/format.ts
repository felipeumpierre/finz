const EUR = new Intl.NumberFormat('de-DE', {
  style: 'currency',
  currency: 'EUR',
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

const PCT = new Intl.NumberFormat('de-DE', {
  style: 'decimal',
  minimumFractionDigits: 1,
  maximumFractionDigits: 1,
});

const DATE = new Intl.DateTimeFormat('de-DE', {
  day: '2-digit',
  month: '2-digit',
  year: 'numeric',
});

export function formatEur(value: number | null | undefined): string {
  if (value == null) return '— (no data)';
  return EUR.format(value).replace(/\u00a0/g, ' ');
}

export function formatPct(value: number | null | undefined): string {
  if (value == null) return '—';
  return `${PCT.format(value)} %`;
}

export function formatDate(iso: string | null | undefined): string {
  if (!iso) return '—';
  return DATE.format(new Date(iso));
}

export function formatRelative(iso: string | null | undefined): string {
  if (!iso) return '—';
  const diffMs = Date.now() - new Date(iso).getTime();
  const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  if (days <= 0) return 'today';
  if (days === 1) return 'yesterday';
  if (days < 30) return `${days} days ago`;
  const months = Math.floor(days / 30);
  if (months < 12) return `${months} months ago`;
  const years = Math.floor(days / 365);
  return `${years} years ago`;
}

export function isStale(iso: string | null | undefined, thresholdDays = 90): boolean {
  if (!iso) return false;
  const diffMs = Date.now() - new Date(iso).getTime();
  const days = diffMs / (1000 * 60 * 60 * 24);
  return days > thresholdDays;
}

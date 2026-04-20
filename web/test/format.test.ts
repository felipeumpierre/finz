import { describe, expect, test } from 'bun:test';
import { formatEur, formatPct, formatDate, formatRelative } from '../src/lib/format';

describe('formatEur', () => {
  test('formats positive with thousands separator and euro suffix', () => {
    expect(formatEur(12345.67)).toBe('12.345,67 €');
  });

  test('formats zero', () => {
    expect(formatEur(0)).toBe('0,00 €');
  });

  test('formats negative with leading minus', () => {
    expect(formatEur(-1234.5)).toBe('-1.234,50 €');
  });

  test('rounds to 2 decimals', () => {
    expect(formatEur(1.005)).toBe('1,01 €');
  });

  test('handles null with em-dash', () => {
    expect(formatEur(null)).toBe('— (no data)');
  });
});

describe('formatPct', () => {
  test('formats with one decimal and percent', () => {
    expect(formatPct(24.35)).toBe('24,4 %');
  });

  test('formats zero', () => {
    expect(formatPct(0)).toBe('0,0 %');
  });

  test('handles null', () => {
    expect(formatPct(null)).toBe('—');
  });
});

describe('formatDate', () => {
  test('formats ISO date in DE locale', () => {
    expect(formatDate('2026-04-20T00:00:00Z')).toBe('20.04.2026');
  });

  test('handles null', () => {
    expect(formatDate(null)).toBe('—');
  });
});

describe('formatRelative', () => {
  test('returns "today" for today', () => {
    const today = new Date().toISOString();
    expect(formatRelative(today)).toBe('today');
  });

  test('returns "N days ago" for older dates', () => {
    const d = new Date();
    d.setDate(d.getDate() - 5);
    expect(formatRelative(d.toISOString())).toBe('5 days ago');
  });

  test('returns "N months ago" for dates >30 days', () => {
    const d = new Date();
    d.setDate(d.getDate() - 95);
    expect(formatRelative(d.toISOString())).toMatch(/months ago/);
  });
});

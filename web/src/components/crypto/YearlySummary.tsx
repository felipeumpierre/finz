import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { formatEur } from '@/lib/format';
import type { CryptoYearlyTax } from '@/lib/types';

function num(v: string | number | null | undefined): number | null {
  if (v == null) return null;
  const n = typeof v === 'string' ? parseFloat(v) : v;
  return Number.isFinite(n) ? n : null;
}

export function YearlySummary({ summary }: { summary: Record<string, CryptoYearlyTax> }) {
  const rows = Object.entries(summary).sort(([a], [b]) => b.localeCompare(a));
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Year</TableHead>
          <TableHead className="text-right">§23 net</TableHead>
          <TableHead className="text-right">§23 taxable</TableHead>
          <TableHead className="text-right">§22 Nr.3 income</TableHead>
          <TableHead className="text-right">§22 Nr.3 taxable</TableHead>
          <TableHead>Status</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.map(([year, y]) => (
          <TableRow key={year}>
            <TableCell className="tabular">{year}</TableCell>
            <TableCell className="tabular text-right">{formatEur(num(y.sect_23_net_eur))}</TableCell>
            <TableCell className="tabular text-right">{formatEur(num(y.sect_23_taxable_eur))}</TableCell>
            <TableCell className="tabular text-right">{formatEur(num(y.sect_22_3_income_eur))}</TableCell>
            <TableCell className="tabular text-right">{formatEur(num(y.sect_22_3_taxable_eur))}</TableCell>
            <TableCell>
              {y.needs_correction ? (
                <Badge variant="outline" className="border-destructive text-destructive">
                  Needs correction
                </Badge>
              ) : (
                <span className="text-xs text-muted-foreground">OK</span>
              )}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { formatEur } from '@/lib/format';
import type { CryptoHolding } from '@/lib/types';

export function HoldingsSummary({ holdings }: { holdings: CryptoHolding[] }) {
  const sorted = [...holdings].sort((a, b) => (b.value_eur ?? 0) - (a.value_eur ?? 0)).slice(0, 20);
  if (sorted.length === 0) return <p className="text-sm text-muted-foreground">No holdings.</p>;
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Symbol</TableHead>
          <TableHead className="text-right">Quantity</TableHead>
          <TableHead className="text-right">Value</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {sorted.map((h, i) => (
          <TableRow key={i}>
            <TableCell>
              {h.symbol} <span className="text-xs text-muted-foreground">{h.name}</span>
            </TableCell>
            <TableCell className="tabular text-right">{h.quantity.toFixed(6)}</TableCell>
            <TableCell className="tabular text-right">{formatEur(h.value_eur ?? null)}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

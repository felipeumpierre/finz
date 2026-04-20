import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { formatEur } from '@/lib/format';
import type { Broker, BrokerPosition } from '@/lib/types';

interface GroupedHolding {
  isin: string;
  name: string;
  owner: string;
  brokers: string[];
  quantity: number;
  valueEur: number;
}

function latestPositions(b: Broker): BrokerPosition[] {
  const snaps = b.portfolio_snapshots;
  if (snaps && snaps.length > 0) return snaps[snaps.length - 1].positions ?? [];
  return b.positions_year_end ?? [];
}

function posQuantity(p: BrokerPosition): number {
  return p.quantity ?? p.qty ?? 0;
}

function posValue(p: BrokerPosition): number {
  return p.value_eur ?? p.value ?? 0;
}

export function HoldingsTable({ brokers }: { brokers: Broker[] }) {
  const groups = new Map<string, GroupedHolding>();

  for (const b of brokers) {
    for (const p of latestPositions(b)) {
      if (!p.isin) continue;
      const key = `${p.isin}|${b.owner}`;
      const prev = groups.get(key);
      if (prev) {
        prev.quantity += posQuantity(p);
        prev.valueEur += posValue(p);
        if (!prev.brokers.includes(b.name)) prev.brokers.push(b.name);
      } else {
        groups.set(key, {
          isin: p.isin,
          name: p.name,
          owner: b.owner,
          brokers: [b.name],
          quantity: posQuantity(p),
          valueEur: posValue(p),
        });
      }
    }
  }

  const rows = Array.from(groups.values()).sort((a, b) => b.valueEur - a.valueEur);

  if (rows.length === 0) {
    return <p className="text-sm text-muted-foreground">No position-level data available.</p>;
  }

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Owner</TableHead>
          <TableHead>Brokers</TableHead>
          <TableHead className="text-right">Qty</TableHead>
          <TableHead className="text-right">Value</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.map((r, i) => (
          <TableRow key={i}>
            <TableCell className="max-w-xs truncate">{r.name}</TableCell>
            <TableCell>{r.owner}</TableCell>
            <TableCell className="text-muted-foreground">{r.brokers.join(', ')}</TableCell>
            <TableCell className="tabular text-right">{r.quantity.toFixed(2)}</TableCell>
            <TableCell className="tabular text-right">{formatEur(r.valueEur)}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

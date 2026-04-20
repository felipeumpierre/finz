import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { formatEur } from '@/lib/format';
import type { Broker } from '@/lib/types';

function latestValue(b: Broker): number {
  const snaps = b.portfolio_snapshots;
  if (snaps && snaps.length > 0) return snaps[snaps.length - 1].total_value ?? 0;
  const stmts = b.annual_statements ?? [];
  if (stmts.length === 0) return 0;
  const last = stmts[stmts.length - 1];
  const v = (last.portfolio_value_year_end ?? last.account_value_year_end ?? last.total_portfolio_value) as number | undefined;
  return typeof v === 'number' ? v : 0;
}

export function BrokerList({ brokers }: { brokers: Broker[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Broker</TableHead>
          <TableHead>Owner</TableHead>
          <TableHead>Type</TableHead>
          <TableHead className="text-right">Value</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {brokers.map((b, i) => (
          <TableRow key={i}>
            <TableCell>{b.name}</TableCell>
            <TableCell>{b.owner}</TableCell>
            <TableCell className="text-muted-foreground">{b.type}</TableCell>
            <TableCell className="tabular text-right">{formatEur(latestValue(b))}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

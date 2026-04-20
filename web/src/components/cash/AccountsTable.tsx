import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { formatEur, formatPct } from '@/lib/format';
import type { CashAccount } from '@/lib/types';

function latest<T>(arr: T[] | undefined): T | undefined {
  return arr && arr.length > 0 ? arr[arr.length - 1] : undefined;
}

export function AccountsTable({ accounts }: { accounts: CashAccount[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Bank</TableHead>
          <TableHead>Owner</TableHead>
          <TableHead>Type</TableHead>
          <TableHead className="text-right">Balance</TableHead>
          <TableHead className="text-right">Rate</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {accounts.map((a, i) => {
          const balance = latest(a.balances)?.balance ?? null;
          const rate = latest(a.interest)?.interest_rate_pct ?? null;
          return (
            <TableRow key={i}>
              <TableCell>{a.bank}</TableCell>
              <TableCell>{a.owner}</TableCell>
              <TableCell className="text-muted-foreground">{a.account_type}</TableCell>
              <TableCell className="tabular text-right">{formatEur(balance)}</TableCell>
              <TableCell className="tabular text-right">{rate == null ? '—' : formatPct(rate)}</TableCell>
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
}

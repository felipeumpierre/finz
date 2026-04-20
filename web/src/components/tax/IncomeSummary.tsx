import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { formatEur } from '@/lib/format';
import type { TaxState } from '@/lib/types';

export function IncomeSummary({ tax }: { tax: TaxState }) {
  const rows = (tax.persons ?? []).flatMap(p =>
    (p.employers ?? []).map(e => ({
      person: p.name,
      employer: e.employer_name,
      brutto: e.brutto,
      lohnsteuer: e.lohnsteuer,
    })),
  );

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Person</TableHead>
          <TableHead>Employer</TableHead>
          <TableHead className="text-right">Brutto</TableHead>
          <TableHead className="text-right">Lohnsteuer</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.length === 0 ? (
          <TableRow>
            <TableCell colSpan={4} className="text-muted-foreground">
              No employer income captured.
            </TableCell>
          </TableRow>
        ) : (
          rows.map((r, i) => (
            <TableRow key={i}>
              <TableCell>{r.person}</TableCell>
              <TableCell>{r.employer}</TableCell>
              <TableCell className="tabular text-right">{formatEur(r.brutto)}</TableCell>
              <TableCell className="tabular text-right">{formatEur(r.lohnsteuer)}</TableCell>
            </TableRow>
          ))
        )}
      </TableBody>
    </Table>
  );
}

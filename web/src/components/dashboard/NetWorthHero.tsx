import { Card } from '@/components/ui/card';
import { formatEur } from '@/lib/format';

interface Props {
  total: number;
  cash: number;
  investments: number;
  pension: number;
  asOf: string;
}

export function NetWorthHero({ total, cash, investments, pension, asOf }: Props) {
  return (
    <Card className="p-6">
      <div className="text-xs font-medium uppercase tracking-wider text-muted-foreground">
        Net worth · {asOf}
      </div>
      <div className="mt-1 tabular text-4xl font-semibold">{formatEur(total)}</div>
      <div className="mt-4 grid grid-cols-3 gap-6 text-sm">
        <div>
          <div className="text-xs text-muted-foreground">Cash</div>
          <div className="tabular">{formatEur(cash)}</div>
        </div>
        <div>
          <div className="text-xs text-muted-foreground">Investments</div>
          <div className="tabular">{formatEur(investments)}</div>
        </div>
        <div>
          <div className="text-xs text-muted-foreground">Pension</div>
          <div className="tabular">{formatEur(pension || null)}</div>
        </div>
      </div>
    </Card>
  );
}

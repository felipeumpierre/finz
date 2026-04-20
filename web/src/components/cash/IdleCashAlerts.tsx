import type { IdleCash } from '@/lib/insights';
import { formatEur } from '@/lib/format';

export function IdleCashAlerts({ idle }: { idle: IdleCash }) {
  if (idle.idleAccounts.length === 0) {
    return <p className="text-sm text-muted-foreground">No idle cash.</p>;
  }
  return (
    <div className="space-y-2">
      <p className="text-sm">
        Opportunity cost: <span className="tabular text-warning">{formatEur(idle.opportunityCostAnnual)}/year</span>
      </p>
      <ul className="space-y-1 text-sm">
        {idle.idleAccounts.map((a, i) => (
          <li key={i} className="flex justify-between">
            <span>{a.bank} ({a.owner})</span>
            <span className="tabular text-muted-foreground">
              {formatEur(a.balance)} · missing {formatEur(a.annualMissed)}/yr
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

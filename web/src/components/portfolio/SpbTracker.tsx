import type { SpbUsage } from '@/lib/insights';
import { formatEur } from '@/lib/format';

export function SpbTracker({ spb }: { spb: SpbUsage }) {
  const pct = Math.min(100, (spb.used / spb.allowance) * 100);
  return (
    <div className="space-y-2">
      <div className="flex justify-between text-sm">
        <span className="text-muted-foreground">Used</span>
        <span className="tabular">{formatEur(spb.used)} of {formatEur(spb.allowance)}</span>
      </div>
      <div className="h-2 overflow-hidden rounded bg-muted">
        <div className="h-full bg-primary" style={{ width: `${pct}%` }} />
      </div>
      <div className="text-xs text-muted-foreground">
        {formatEur(spb.remaining)} remaining · Bank {formatEur(spb.bankInterestYtd)} · Portfolio {formatEur(spb.portfolioSpbUsed)}
      </div>
    </div>
  );
}

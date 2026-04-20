import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { formatEur } from '@/lib/format';
import type { InsurancePolicy } from '@/lib/types';

export function PolicyCard({ policy }: { policy: InsurancePolicy }) {
  return (
    <Card>
      <CardContent className="py-4">
        <div className="flex items-start justify-between">
          <div>
            <div className="text-xs uppercase tracking-wider text-muted-foreground">{policy.type}</div>
            <div className="mt-0.5 font-semibold">{policy.product_name ?? policy.provider}</div>
            <div className="text-xs text-muted-foreground">{policy.provider}</div>
          </div>
          <Badge variant="outline">{policy.who_covered ?? '—'}</Badge>
        </div>
        <div className="mt-3 flex items-baseline gap-4 text-sm">
          <span className="tabular">{formatEur(policy.annual_premium ?? null)}</span>
          <span className="text-xs text-muted-foreground">{policy.payment_frequency ?? 'annual'}</span>
        </div>
      </CardContent>
    </Card>
  );
}

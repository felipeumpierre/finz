import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import type { TaxReadiness, Readiness } from '@/lib/insights';

const LABELS: Record<keyof TaxReadiness, string> = {
  income: 'Income data captured',
  investments: 'Investment data captured',
  bankInterest: 'Bank interest captured',
  insurancePremiums: 'Insurance premiums (Vorsorgeaufwand)',
  profileComplete: 'Profile complete',
};

const STATUS_COLOR: Record<Readiness, string> = {
  yes: 'text-positive',
  partial: 'text-warning',
  no: 'text-destructive',
};

export function TaxReadinessCard({ readiness }: { readiness: TaxReadiness }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Tax readiness ({new Date().getFullYear()})</CardTitle>
      </CardHeader>
      <CardContent>
        <ul className="space-y-1.5 text-sm">
          {(Object.keys(LABELS) as Array<keyof TaxReadiness>).map(k => (
            <li key={k} className="flex items-center justify-between">
              <span className="text-muted-foreground">{LABELS[k]}</span>
              <span className={`font-medium uppercase tracking-wider text-xs ${STATUS_COLOR[readiness[k]]}`}>
                {readiness[k]}
              </span>
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}

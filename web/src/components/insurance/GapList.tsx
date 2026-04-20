import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import type { InsuranceGap } from '@/lib/types';

const SEVERITY: Record<string, string> = {
  critical: 'text-destructive',
  important: 'text-warning',
  nice_to_have: 'text-muted-foreground',
};

export function GapList({ gaps }: { gaps: InsuranceGap[] }) {
  if (!gaps || gaps.length === 0) {
    return (
      <Card>
        <CardHeader><CardTitle className="text-sm">Coverage gaps</CardTitle></CardHeader>
        <CardContent className="text-sm text-muted-foreground">No gaps identified.</CardContent>
      </Card>
    );
  }
  return (
    <Card>
      <CardHeader><CardTitle className="text-sm">Coverage gaps</CardTitle></CardHeader>
      <CardContent>
        <ul className="space-y-2 text-sm">
          {gaps.map((g, i) => (
            <li key={i} className="flex items-start gap-2">
              <span className={`mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-current ${SEVERITY[g.severity] ?? 'text-muted-foreground'}`} />
              <div>
                <div className="font-medium uppercase tracking-wider text-xs">{g.type}</div>
                <div className="text-xs text-muted-foreground">{g.recommendation}</div>
              </div>
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}

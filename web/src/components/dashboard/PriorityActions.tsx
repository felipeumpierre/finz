import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import type { PriorityAction } from '@/lib/insights';

const SEVERITY_COLOR: Record<PriorityAction['severity'], string> = {
  high: 'text-destructive',
  medium: 'text-warning',
  low: 'text-muted-foreground',
};

export function PriorityActions({ actions }: { actions: PriorityAction[] }) {
  if (actions.length === 0) {
    return (
      <Card>
        <CardHeader>
          <CardTitle className="text-sm">Priority actions</CardTitle>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">Everything looks on track.</CardContent>
      </Card>
    );
  }
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm">Priority actions</CardTitle>
      </CardHeader>
      <CardContent>
        <ul className="space-y-2 text-sm">
          {actions.map((a, i) => (
            <li key={i} className="flex items-start gap-2">
              <span className={`mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-current ${SEVERITY_COLOR[a.severity]}`} />
              <div>
                <div className="font-medium">{a.title}</div>
                <div className="text-xs text-muted-foreground">{a.detail}</div>
              </div>
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}

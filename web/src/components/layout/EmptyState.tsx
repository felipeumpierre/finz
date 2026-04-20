import { Card, CardContent } from '@/components/ui/card';

interface Props {
  domain: string;
  command: string;
  hint?: string;
}

export function EmptyState({ domain, command, hint }: Props) {
  return (
    <Card className="border-dashed">
      <CardContent className="py-10 text-center">
        <p className="text-sm text-muted-foreground">No {domain} data yet.</p>
        <p className="mt-2 font-mono text-xs text-primary">{command}</p>
        {hint && <p className="mt-3 text-xs text-muted-foreground">{hint}</p>}
      </CardContent>
    </Card>
  );
}

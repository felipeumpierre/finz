import { Card, CardContent } from '@/components/ui/card';

interface Props {
  label: string;
  value: string;
  href: string;
  sub?: string;
}

export function DomainTile({ label, value, href, sub }: Props) {
  return (
    <a href={href} className="block">
      <Card className="transition-colors hover:border-primary">
        <CardContent className="py-4">
          <div className="text-xs font-medium uppercase tracking-wider text-muted-foreground">
            {label}
          </div>
          <div className="mt-1 tabular text-xl font-semibold">{value}</div>
          {sub && <div className="mt-1 text-xs text-muted-foreground">{sub}</div>}
        </CardContent>
      </Card>
    </a>
  );
}

import { Badge } from '@/components/ui/badge';
import { formatRelative, isStale } from '@/lib/format';

interface Props {
  lastUpdated: string | null | undefined;
}

export function StaleBadge({ lastUpdated }: Props) {
  if (!isStale(lastUpdated)) return null;
  return (
    <Badge variant="outline" className="ml-2 border-warning text-warning">
      Stale · {formatRelative(lastUpdated)}
    </Badge>
  );
}

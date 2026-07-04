# === Stage 24: Add grouped summaries by category or status ===
# Project: StockRoute
from collections import defaultdict
def group_by_category(records, key_field='category'):
    groups = defaultdict(list)
    for rec in records:
        k = rec.get(key_field, 'Unknown')
        groups[k].append(rec)
    return dict(sorted(groups.items()))

def group_by_status(records, status_key='status', summary_fields=None):
    if not summary_fields:
        summary_fields = ['total_qty', 'exceptions']
    grouped = defaultdict(lambda: {'items': [], 'stats': {}})
    for r in records:
        s = r.get(status_key, 'Unknown')
        grouped[s]['items'].append(r)
        if 'qty' in r:
            grouped[s]['stats']['total_qty'] = grouped[s]['stats'].get('total_qty', 0) + r['qty']
        exc_count = sum(1 for item in grouped[s]['items'] if item.get('exception'))
        grouped[s]['stats']['exceptions'] = exc_count
    return {k: {'items': v['items'], 'stats': v['stats']} for k, v in sorted(grouped.items())}

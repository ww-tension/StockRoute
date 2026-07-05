# === Stage 27: Add monthly summary calculations ===
# Project: StockRoute
def calculate_monthly_summary(records):
    from collections import defaultdict
    monthly = defaultdict(lambda: {'in': 0, 'out': 0, 'exceptions': []})
    for r in records:
        key = f"{r['date'][:7]}"
        if r.get('type') == 'IN':
            monthly[key]['in'] += int(r.get('qty', 0))
        elif r.get('type') == 'OUT':
            monthly[key]['out'] += int(r.get('qty', 0))
        if r.get('status') == 'EXCEPTION':
            monthly[key]['exceptions'].append(f"{r['note']} ({r['location']})")
    return {k: dict(v) for k, v in sorted(monthly.items())}

# === Stage 25: Add daily summary calculations ===
# Project: StockRoute
def calculate_daily_summary(records, date):
    daily_stats = {}
    for rec in records:
        if rec['date'] == date and 'batch_id' in rec:
            batch_key = f"Batch {rec['batch_id']} ({rec.get('status', 'unknown')})"
            if batch_key not in daily_stats:
                daily_stats[batch_key] = {'count': 0, 'exceptions': [], 'total_quantity': 0}
            daily_stats[batch_key]['count'] += 1
            daily_stats[batch_key]['total_quantity'] += rec.get('quantity', 0)
            if rec.get('exception_note'):
                daily_stats[batch_key]['exceptions'].append(rec['exception_note'])
    return {k: v for k, v in sorted(daily_stats.items(), key=lambda x: len(x[1]['exceptions']), reverse=True)}

# === Stage 26: Add weekly summary calculations ===
# Project: StockRoute
def calculate_weekly_summary(records, start_date):
    from datetime import timedelta, date
    week_start = start_date - timedelta(days=start_date.weekday())
    week_end = week_start + timedelta(weeks=1)
    weekly_data = {
        'start': week_start.strftime('%Y-%m-%d'),
        'end': (week_end - timedelta(days=1)).strftime('%Y-%m-%d'),
        'total_moves': 0,
        'total_exceptions': 0,
        'batches_processed': set(),
    }
    for r in records:
        if week_start <= date.fromisoformat(r['timestamp']) < week_end:
            weekly_data['total_moves'] += 1
            if r.get('status') == 'exception':
                weekly_data['total_exceptions'] += 1
            batch_id = r.get('batch_id', '')[:8]
            weekly_data['batches_processed'].add(batch_id)
    return {**weekly_data, 'unique_batches': len(weekly_data['batches_processed'])}

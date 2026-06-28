# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: StockRoute
def sort_records(records, key='date'):
    order_map = {'title': -1, 'priority': 1, 'last_update': -1, 'date': -1}
    if key in ['title', 'last_update']:
        reverse = False
    elif key == 'priority':
        reverse = True
    else:
        reverse = False
    return sorted(records, key=lambda r: (r.get(key) or ''), reverse=reverse)

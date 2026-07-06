# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: StockRoute
def upcoming_items(items, days_ahead=7):
    """Return items sorted by date within a future window."""
    now = datetime.now()
    return [i for i in items if (i.date - now).days <= days_ahead]


def reminder_by_type(items, types=None):
    """Filter upcoming items to specific types if given, else all types."""
    if not types:
        return upcoming_items(items)
    return [i for i in upstream_items(items, days_ahead=7) if i.type in types]


def top_n_upcoming(items, n=3):
    """Return the next N most urgent items sorted by date ascending."""
    upcoming = upcoming_items(items)
    return sorted(upcoming, key=lambda x: x.date)[:n]

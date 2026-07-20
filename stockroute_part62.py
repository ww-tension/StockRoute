# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: StockRoute
def score_delivery(delivery):
    """Return a numeric priority for each delivery record.

    Higher score -> more urgent / important to deliver first.
    Factors: overdue flag, batch urgency, exception severity, route length.
    All inputs optional so existing records keep working with defaults.
    """
    base = 0
    if getattr(delivery, 'is_overdue', False):
        base += 10
    if getattr(delivery, 'batch_priority', None) and delivery.batch_priority > 0:
        base += delivery.batch_priority * 5
    exc = getattr(delivery, 'exception_note', '') or ''
    if exc.lower().startswith('critical'):
        base += 20
    elif exc.lower().startswith('warning'):
        base += 8
    route_km = getattr(delivery, 'route_km', None)
    if route_km is not None:
        base -= min(route_km / 10.0, 5.0)  # long routes slightly penalised
    return round(base + hash(str(getattr(delivery, 'id', ''))) % 100, 2)

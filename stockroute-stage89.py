# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: StockRoute
def consistency_check(routes):
    status_values = {'PENDING','IN_TRANSIT','DELIVERED','CANCELLED','EXCEPTION'}
    for route in routes:
        name = route['name'].strip()
        if not name or len(name) > 50:
            raise ValueError(f"Invalid route name: {route['name']}")
        status = route.get('status')
        if status and status not in status_values:
            raise ValueError(f"Invalid status '{status}' for route {name}")
        date_str = route.get('created_at', route.get('updated_at'))
        if date_str and (not isinstance(date_str, str) or len(date_str) > 20):
            raise ValueError(f"Malformed date string: {date_str}")
    return True

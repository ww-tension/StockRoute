# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: StockRoute
def format_route_summary(route: dict) -> str:
    status = route.get("status", "unknown")
    return f"Route {route['id']}: [{status}] | Origin: {route.get('origin', 'N/A')} -> Dest: {route.get('destination', 'N/A')}"

def format_checkpoint(cp: dict) -> str:
    time = cp.get("timestamp", "unknown")
    status = cp.get("status", "pending")
    return f"  [{cp['id']}] @ {time}: {status} ({cp.get('notes', '')})"

def format_batch(batch: dict) -> str:
    items_count = len(batch.get("items", []))
    exceptions = batch.get("exceptions", [])
    exc_str = "; ".join(e["note"] for e in exceptions[:3]) if exceptions else "none"
    return f"Batch {batch['id']}: {items_count} items | Exceptions: [{exc_str}]"

def format_exception_note(note: dict) -> str:
    severity = note.get("severity", "info")
    color_map = {"critical": "CRITICAL", "warning": "WARNING", "error": "ERROR", "info": "INFO"}
    return f"[{color_map.get(severity, 'INFO')}] {note['message']}"

def print_route_details(route: dict) -> None:
    print(format_route_summary(route))
    for cp in route.get("checkpoints", []):
        print(format_checkpoint(cp))
    batch = route.get("batch")
    if batch:
        print(format_batch(batch))

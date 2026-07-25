# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: StockRoute
def snapshot_diff(before, after):
    """Compare two StockRoute snapshots and return a summary of changes."""
    if before is None and after is None:
        return {"status": "no_data"}
    changes = {}
    for field in ["batches", "checkpoints", "transfers", "exceptions"]:
        b, a = getattr(before, field) or [], getattr(after, field) or []
        if len(b) != len(a):
            changes[field] = {"added": len(a) - len(b), "removed": len(b) - len(a)}
    return changes

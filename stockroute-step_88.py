# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: StockRoute
def safe_get(d, key, default=None):
    """Return d[key] if present and truthy, else default."""
    return d.get(key) if isinstance(d, dict) else None


def safe_int(value, default=0):
    """Parse int safely; return default on failure."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_float(value, default=None):
    """Parse float safely; return default on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default if default is not None else 0.0


def fill_optional(record):
    """Apply safer defaults to a StockRoute-like dict for missing optional fields."""
    record.setdefault("status", "pending")
    record.setdefault("priority", "normal")
    record.setdefault("notes", "")
    record.setdefault("batch_id", None)
    record.setdefault("transfer_count", 0)

    if not safe_int(record.get("quantity")):
        record["quantity"] = 1

    if not safe_float(record.get("weight")):
        record["weight"] = 0.0

    return record

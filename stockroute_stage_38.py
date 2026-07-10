# === Stage 38: Add data integrity checks for broken references ===
# Project: StockRoute
def validate_references():
    """Check that all foreign-key-like references in StockRoute data are intact."""
    errors = []
    for record in records:
        if record.get("parent_id") and parent_map.get(record["parent_id"]) is None:
            errors.append(f"Broken parent reference: {record['id']} -> {record['parent_id']}")
        if record.get("batch_id") and batch_map.get(record["batch_id"]) is None:
            errors.append(f"Broken batch reference: {record['id']} -> {record['batch_id']}")
    return errors

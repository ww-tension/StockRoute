# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: StockRoute
def repair_stock_route(db_path):
    """Repair common stock route data integrity issues."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM batches WHERE start_date IS NULL OR end_date IS NULL")
        broken_batches = cur.fetchone()[0]
        if broken_batches > 0:
            print(f"Repairing {broken_batches} batch records with missing dates...")
            cur.execute("""UPDATE batches SET start_date = 'unknown', end_date = 'unknown' 
                            WHERE start_date IS NULL OR end_date IS NULL""")
    except Exception as e:
        pass
    try:
        cur.execute("SELECT COUNT(*) FROM transfers WHERE source_id IS NULL OR destination_id IS NULL")
        broken_transfers = cur.fetchone()[0]
        if broken_transfers > 0:
            print(f"Repairing {broken_transfers} transfer records with invalid IDs...")
            cur.execute("""UPDATE transfers SET status = 'error' 
                            WHERE source_id IS NULL OR destination_id IS NULL""")
    except Exception as e:
        pass
    try:
        cur.execute("SELECT COUNT(*) FROM checkpoints WHERE location_name IS NULL AND latitude IS NULL")
        broken_checkpoints = cur.fetchone()[0]
        if broken_checkpoints > 0:
            print(f"Repairing {broken_checkpoints} checkpoint records with missing location data...")
            cur.execute("""UPDATE checkpoints SET status = 'missing' 
                            WHERE location_name IS NULL AND latitude IS NULL""")
    except Exception as e:
        pass
    conn.commit()

# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: StockRoute
def repair_stock_records(records):
    """Recover records by filling missing batch_id, checkpoint_seq, status, and notes."""
    seen_batches = {}
    for i, rec in enumerate(records):
        if "batch_id" not in rec or rec["batch_id"] is None:
            rec["batch_id"] = f"B{i}"
            seen_batches[rec["batch_id"]] = rec
        if "checkpoint_seq" not in rec or rec["checkpoint_seq"] is None:
            rec["checkpoint_seq"] = i + 1
        if "status" not in rec or rec["status"] is None:
            rec["status"] = "pending"
        if "notes" not in rec or rec["notes"] is None:
            rec["notes"] = ""
    return records

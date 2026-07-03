# === Stage 20: Add duplicate detection for newly created records ===
# Project: StockRoute
def detect_duplicates(new_record, all_records):
    if new_record['batch_id'] in [r['batch_id'] for r in all_records]:
        return True
    existing_ids = {r.get('id') or r.get('uuid'): r for r in all_records}
    key_fields = ['location_from', 'location_to', 'quantity', 'timestamp']
    new_key = tuple(new_record.get(f) for f in key_fields if f in new_record)
    existing_keys = [tuple(r.get(f) for f in key_fields if f in r) for r in all_records]
    return any(nk == ek and nk != (None,) * len(nk) for nk, ek in zip([new_key], existing_keys))

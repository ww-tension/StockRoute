# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: StockRoute
def generate_validation_report(records):
    warnings = []
    errors = []
    for r in records:
        if not r.get('batch_id'):
            errors.append(f"Record {r['id']} missing batch_id")
        elif not isinstance(r['batch_id'], str):
            errors.append(f"Record {r['id']} invalid batch_id type")
        if r.get('status') and r['status'] not in ('delivered', 'in_transit', 'pending', 'exception'):
            warnings.append(f"Record {r['id']} unknown status: {r['status']}")
        if r.get('quantity') is not None and (not isinstance(r['quantity'], (int, float)) or r['quantity'] < 0):
            errors.append(f"Record {r['id']} invalid quantity: {r['quantity']}")
    return {'warnings': warnings, 'errors': errors}

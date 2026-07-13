# === Stage 42: Add CSV export without external dependencies ===
# Project: StockRoute
def export_to_csv(records, path):
    import csv
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(records[0].keys()))
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)

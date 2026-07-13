# === Stage 43: Add CSV import for the primary record type ===
# Project: StockRoute
def import_stock_routes_from_csv(csv_path, delimiter=','):
    """Import stock routes from a CSV file with columns: id, origin, destination, quantity."""
    records = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=delimiter)
            header = next(reader, None)
            if not header or len(header) < 4:
                raise ValueError("CSV must have at least id, origin, destination, quantity columns")
            for row in reader:
                if len(row) >= 4 and row[0].strip():
                    records.append({
                        'id': row[0].strip(),
                        'origin': row[1].strip(),
                        'destination': row[2].strip(),
                        'quantity': int(row[3].strip())
                    })
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except ValueError as e:
        print(f"Import error: {e}")
    return records

if __name__ == '__main__':
    example_csv = 'stock_routes.csv'
    if os.path.exists(example_csv):
        imported = import_stock_routes_from_csv(example_csv)
        for r in imported[:5]:
            print(f"{r['id']}: {r['origin']} -> {r['destination']} (qty: {r['quantity']})")

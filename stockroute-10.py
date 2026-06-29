# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: StockRoute
class SearchFilter:
    def __init__(self, records):
        self.records = records
    
    def search(self, query, fields=None):
        if fields is None:
            fields = ['id', 'batch_id', 'checkpoint_name', 'exception_note']
        lower_query = query.lower()
        return [r for r in self.records if any(lower_query in str(getattr(r, f, '')).lower() for f in fields)]

def main():
    data = [{'id': 101, 'batch_id': 'B-2024-X', 'checkpoint_name': 'Warehouse A', 'exception_note': 'Delayed shipment'}, {'id': 102, 'batch_id': 'b-2023-y', 'checkpoint_name': 'warehouse b', 'exception_note': None}]
    filter_obj = SearchFilter(data)
    results = filter_obj.search('WAREHOUSE')
    for r in results:
        print(f"ID: {r['id']}, Batch: {r['batch_id']}")

if __name__ == '__main__':
    main()

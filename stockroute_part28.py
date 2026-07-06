# === Stage 28: Add overdue item detection based on due dates ===
# Project: StockRoute
class StockOverdueDetector:
    """Detects items that have passed their delivery due date."""

    def __init__(self, stock_route):
        self.stock_route = stock_route

    def check_overdue(self, today=None):
        if today is None:
            from datetime import date
            today = date.today()
        overdue_items = []
        for batch in self.stock_route.batches:
            if hasattr(batch, 'items') and isinstance(batch.items, list):
                for item in batch.items:
                    due_date = getattr(item, 'due_date', None)
                    expected_delivery = getattr(item, 'expected_delivery', None)
                    if due_date is not None and due_date < today:
                        overdue_items.append({
                            'item_id': item.item_id,
                            'batch_id': batch.batch_id,
                            'due_date': due_date.isoformat(),
                            'overdue_days': (today - due_date).days,
                        })
                    elif expected_delivery is not None and expected_delivery < today:
                        overdue_items.append({
                            'item_id': item.item_id,
                            'batch_id': batch.batch_id,
                            'expected_delivery': expected_delivery.isoformat(),
                            'overdue_days': (today - expected_delivery).days,
                        })
        return overdue_items

    def get_overdue_summary(self):
        today = date.today()
        overdue_count = len(self.check_overdue(today))
        total_batches = len(self.stock_route.batches) if self.stock_route.batches else 0
        return {
            'overdue_items': overdue_count,
            'total_batches': total_batches,
            'status': 'critical' if overdue_count > 0 else 'ok',
        }

# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: StockRoute
class StockRoute:
    def __init__(self):
        self.route = []
        self.checkpoints = {}
        self.batches = {}
        self.exceptions = []
    
    def add_route(self, origin, destination):
        if len(self.route) > 0 and not (self.route[-1][1] == origin):
            raise ValueError("Origin must match last checkpoint's destination")
        self.route.append((origin, destination))
        
    def set_checkpoint(self, location, status='active', estimated_time=None):
        self.checkpoints[location] = {'status': status, 'estimated_time': estimated_time}
    
    def add_batch(self, batch_id, items, delivery_date):
        self.batches[batch_id] = {'items': items, 'delivery_date': delivery_date}
        
    def note_exception(self, location, issue, severity='low'):
        self.exceptions.append({'location': location, 'issue': issue, 'severity': severity})
    
    def __str__(self):
        return f"StockRoute: {len(self.route)} checkpoints\n{self.route}\n{self.checkpoints}\n{self.batches}\nExceptions: {self.exceptions}"

class StockRouteDemo:
    def __init__(self):
        self.stock_route = StockRoute()
        self.stock_route.add_route('Warehouse A', 'Distribution Center')
        self.stock_route.set_checkpoint('Distribution Center', status='active', estimated_time='2024-12-31')
        self.stock_route.set_checkpoint('Retail Store B', status='pending', estimated_time='2025-01-05')
        self.stock_route.add_batch('BATCH-001', items=['Electronics', 'Clothing'], delivery_date='2025-01-10')
        self.stock_route.note_exception('Distribution Center', issue='Traffic congestion', severity='medium')
    
    def __str__(self):
        return f"StockRouteDemo: {self.stock_route}"

demo = StockRouteDemo()
print(demo)

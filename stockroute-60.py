# === Stage 60: Add saved views for frequently used filters ===
# Project: StockRoute
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}
    
    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d.get('filters', {}))
    
    def to_dict(self):
        return {'name': self.name, 'filters': self.filters}

class SavedViewManager:
    def __init__(self):
        self._views = []
    
    def add_view(self, name, filters=None):
        view = SavedView(name, filters)
        self._views.append(view)
        return view
    
    def get_view(self, index_or_name):
        if isinstance(index_or_name, int):
            return self._views[index_or_name]
        for v in self._views:
            if v.name == index_or_name:
                return v
        return None
    
    def list_views(self):
        return [v.to_dict() for v in self._views]
    
    def clear_all(self):
        self._views.clear()

# Example usage
manager = SavedViewManager()
manager.add_view("Active Today", {"status": "active", "date": "2024-01-15"})
manager.add_view("Pending Delivery", {"status": "pending"})
print(manager.list_views())

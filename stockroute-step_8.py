# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: StockRoute
class StockRouteFilter:
    def __init__(self, records):
        self.records = records

    def filter_by_status(self, status):
        return [r for r in self.records if r.get('status') == status]

    def filter_by_category(self, category):
        return [r for r in self.records if r.get('category') == category]

    def filter_by_owner(self, owner_id):
        return [r for r in self.records if r.get('owner_id') == owner_id]

    def filter_by_tag(self, tag):
        return [r for r in self.records if any(r.get('tags', {}).get(t) for t in [tag])]

    def apply_filters(self, status=None, category=None, owner_id=None, tags=None):
        result = self.records
        if status:
            result = self.filter_by_status(status)
        if category:
            result = self.filter_by_category(category)
        if owner_id:
            result = self.filter_by_owner(owner_id)
        if tags:
            result = self.filter_by_tag(tags[0])
        return result

    def get_filtered_records(self, status=None, category=None, owner_id=None, tags=None):
        filtered = self.apply_filters(status, category, owner_id, tags or [])
        return [r for r in filtered if not any(r.get('is_exception', False) and e['type'] != 'exception' for e in r.get('exceptions', []))]

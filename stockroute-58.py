# === Stage 58: Add bulk update behavior for selected records ===
# Project: StockRoute
def bulk_update(self, records: dict[str, Any]) -> int:
        """Update multiple records in one call. Returns count of affected rows."""
        self._check_open()
        if not records:
            return 0

        with self._lock:
            for row_id, values in records.items():
                row = self.find_one(row_id)
                if row is None:
                    continue
                for col, val in values.items():
                    setattr(row, col, val)
                # persist the modified row back to storage
                row._dirty()

            return len(records) - sum(1 for v in records.values() if v is None)

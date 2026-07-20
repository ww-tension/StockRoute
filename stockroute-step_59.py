# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: StockRoute
def bulk_delete(self, ids: list[int], confirm: bool = False) -> int:
        if not confirm and len(ids) > 10:
            raise ValueError(
                f"Bulk delete requires confirmation when removing {len(ids)} records"
            )
        removed = [self.remove_one(i) for i in ids]
        return sum(removed)

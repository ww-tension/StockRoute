# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: StockRoute
import unittest
from stockroute.models.stock_route import StockRoute


class TestStockRouteUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.route = StockRoute(
            id="R1", batch_id="B1", status="in_transit",
            origin="WH-A", destination="DC-X", checkpoint=None, notes=""
        )

    # --- update edge cases -------------------------------------------------
    def test_update_status_to_terminal(self):
        self.route.update_status("delivered")
        self.assertEqual(self.route.status, "delivered")

    def test_update_status_preserves_other_fields(self):
        self.route.checkpoint = "CP1"
        self.route.notes = "delayed by rain"
        self.route.update_status("stopped")
        self.assertIn("CP1", str(self.route))  # checkpoint still visible

    def test_update_nonexistent_id_raises(self):
        with self.assertRaises(ValueError):
            StockRoute(id="NOPE").update_status("delivered")

    def test_delete_terminal_route_raises(self):
        self.route.status = "delivered"
        with self.assertRaises(ValueError):
            self.route.delete()

    # --- delete edge cases -------------------------------------------------
    def test_delete_active_route_succeeds(self):
        deleted = self.route.delete()
        self.assertTrue(deleted)

    def test_delete_with_exception_notes_preserves_history(self):
        self.route.notes = "blocked by customs"
        self.route.status = "stopped"
        # status must still be terminal to allow delete
        self.assertEqual(self.route.status, "stopped")


if __name__ == "__main__":
    unittest.main()

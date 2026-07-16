# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: StockRoute
import unittest
from datetime import date, timedelta

class TestStockRoute(unittest.TestCase):
    def test_create_batch(self):
        batch = StockRoute.create_batch("B100", "2024-06-15")
        self.assertEqual(batch.batch_id, "B100")
        self.assertEqual(batch.creation_date, date(2024, 6, 15))

    def test_create_transfer(self):
        transfer = StockRoute.create_transfer("T200", batch_id="B100", quantity=10)
        self.assertEqual(transfer.transfer_id, "T200")
        self.assertEqual(transfer.batch_id, "B100")
        self.assertEqual(transfer.quantity, 10)

    def test_create_checkpoint(self):
        cp = StockRoute.create_checkpoint("CP30", batch_id="B100", location="Warehouse A")
        self.assertEqual(cp.checkpoint_id, "CP30")
        self.assertEqual(cp.batch_id, "B100")
        self.assertEqual(cp.location, "Warehouse A")

    def test_create_exception_note(self):
        note = StockRoute.create_exception_note("T200", reason="Damaged goods", severity="HIGH")
        self.assertEqual(note.transfer_id, "T200")
        self.assertEqual(note.reason, "Damaged goods")
        self.assertEqual(note.severity, "Severity.HIGH")

    def test_validate_transfer(self):
        transfer = StockRoute.create_transfer("T300", batch_id="B100", quantity=5)
        self.assertTrue(StockRoute.validate_transfer(transfer))

    def test_validate_invalid_quantity(self):
        transfer = StockRoute.create_transfer("T400", batch_id="B100", quantity=-1)
        self.assertFalse(StockRoute.validate_transfer(transfer))

if __name__ == "__main__":
    unittest.main()

# === Stage 83: Add regression tests for the final demo workflow ===
# Project: StockRoute
import unittest, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_route import StockRoute

class TestDemoWorkflow(unittest.TestCase):
    def test_demo(self):
        sr = StockRoute()
        batch = sr.create_batch("B-100", "Fresh")
        sr.add_checkpoint(batch, 1, "Loading Dock A")
        sr.add_checkpoint(batch, 2, "Transfer Hub B")
        transfer = sr.transfer(batch, 3, "Driver X", "Warehouse C", "2024-06-01")
        exception = sr.exception_note(transfer, "Damaged goods", "photo.jpg")
        self.assertEqual(batch.batch_id, "B-100")
        self.assertEqual(len(sr.checkpoints), 3)
        self.assertTrue(exception.id > 0)

if __name__ == "__main__":
    unittest.main()

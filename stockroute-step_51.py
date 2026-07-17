# === Stage 51: Add unit tests for search and filter behavior ===
# Project: StockRoute
import unittest
from stockroute.models import StockRoute, Transfer, Checkpoint, Batch, ExceptionNote


class TestSearchFilter(unittest.TestCase):

    def setUp(self):
        self.routes = [
            StockRoute(route_id="R1", origin="A", destination="B", status="active"),
            StockRoute(route_id="R2", origin="C", destination="D", status="completed"),
            StockRoute(route_id="R3", origin="E", destination="F", status="pending"),
        ]

    def test_filter_by_status(self):
        active_routes = [r for r in self.routes if r.status == "active"]
        self.assertEqual(len(active_routes), 1)
        self.assertEqual(active_routes[0].route_id, "R1")

    def test_search_by_origin(self):
        results = [r for r in self.routes if r.origin.startswith("A")]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].origin, "A")

    def test_search_with_no_matches(self):
        results = [r for r in self.routes if r.destination == "Z"]
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()

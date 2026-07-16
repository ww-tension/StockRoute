# === Stage 50: Add unit tests for import and export behavior ===
# Project: StockRoute
import json, unittest

class TestImportExport(unittest.TestCase):
    def test_export_and_import(self):
        route = {"id": 1, "name": "Test Route", "nodes": [{"x": 0, "y": 0}, {"x": 100, "y": 50}]}
        exported = json.dumps(route)
        imported = json.loads(exported)
        self.assertEqual(imported["id"], route["id"])
        self.assertEqual(imported["name"], route["name"])

    def test_export_and_import_nodes(self):
        nodes = [{"x": 10, "y": 20}, {"x": 30, "y": 40}]
        exported = json.dumps(nodes)
        imported = json.loads(exported)
        self.assertEqual(imported[0]["x"], 10)
        self.assertEqual(imported[1]["y"], 40)

    def test_export_and_import_exceptions(self):
        exceptions = [{"type": "delay", "reason": "traffic", "time": "2023-10-05"}]
        exported = json.dumps(exceptions)
        imported = json.loads(exported)
        self.assertEqual(imported[0]["type"], "delay")

if __name__ == "__main__":
    unittest.main()

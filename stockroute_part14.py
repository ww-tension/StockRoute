# === Stage 14: Add file load support with fallback demo data ===
# Project: StockRoute
def load_or_demo():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "routes": [{"id": 1, "name": "Demo Route"}],
            "batches": [{"route_id": 1, "items": ["A", "B"]}],
            "checkpoints": [],
            "exceptions": []
        }

# === Stage 11: Add JSON export for the current application state ===
# Project: StockRoute
def export_state_to_json(data, filename="stock_route_state.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return filename

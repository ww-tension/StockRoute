# === Stage 67: Add a function that returns key project metrics ===
# Project: StockRoute
def get_project_metrics(stocks, routes):
    """Return key metrics for the StockRoute project."""
    return {
        "total_stocks": len(stocks),
        "total_routes": len(routes),
        "stocks_with_transfers": sum(1 for s in stocks if s.get("transferred", False)),
        "routes_with_checkpoints": sum(1 for r in routes if any(cp["checked"] for cp in r.get("checkpoints", []))),
        "total_batches": sum(len(r.get("batches", [])) for r in routes),
    }

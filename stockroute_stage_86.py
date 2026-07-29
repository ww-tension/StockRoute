# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: StockRoute
import subprocess


def demo_stock_route():
    """Run compact CLI demos for StockRoute."""
    cmds = [
        "stockroute init",
        "stockroute add stock --name 'Widget A' --qty 100 --cost 5.25",
        "stockroute add checkpoint --id C-001 --loc 'Warehouse North'",
        "stockroute transfer --from C-001 --to C-002 --qty 30",
        "stockroute batch create --name B-101 --items 'Widget A' --qty 50",
        "stockroute add exception --batch B-101 --note 'Damaged in transit'",
    ]
    for cmd in cmds:
        print(f"$ {cmd}")


demo_stock_route()

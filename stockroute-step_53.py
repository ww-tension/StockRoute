# === Stage 53: Add command help text and usage examples ===
# Project: StockRoute
def print_help():
    """Print usage and help text for StockRoute CLI."""
    print("StockRoute - Delivery Route & Stock Movement Tracker")
    print("=" * 50)
    print("\nUsage: python stockroute.py <command> [options]")
    print("\nCommands:")
    print("  list         List all batches, transfers, and checkpoints")
    print("  add-batch    Add a new delivery batch")
    print("  add-transfer Add a transfer between locations")
    print("  add-checkpoint Add a checkpoint to a route")
    print("  add-exception Record an exception/issue note")
    print("  status       Show current stock and route status summary")
    print("  help         Show this help message")
    print("\nExamples:")
    print("  python stockroute.py list")
    print("  python stockroute.py add-batch --name 'Winter2024' --origin 'Warehouse A'")
    print("  python stockroute.py add-transfer --batch 'Winter2024' --from 'Warehouse A' --to 'Distribution Center B'")
    print("  python stockroute.py add-checkpoint --batch 'Winter2024' --location 'Highway Mile 55'")
    print("  python stockroute.py status")

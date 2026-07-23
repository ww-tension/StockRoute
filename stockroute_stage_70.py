# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: StockRoute
def clear_state():
    """Reset all tracking data to initial state."""
    if not _confirm_clear:
        print("⚠️  Clear state requires confirmation.")
        return
    confirm = input("Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Aborted. State unchanged.")
        return

    # Reset tracking data
    routes.clear()
    batches.clear()
    checkpoints.clear()
    transfers.clear()
    exceptions.clear()
    route_order = []
    batch_order = []
    checkpoint_order = []
    transfer_order = []
    exception_order = []

    print("✅ StockRoute state cleared successfully.")

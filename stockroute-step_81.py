# === Stage 81: Add final README text as a module string with usage examples ===
# Project: StockRoute
def stock_route_demo():
    """Compact usage example for StockRoute – append to README."""
    from stockroute import StockRoute, Transfer, Checkpoint, Batch, ExceptionNote

    sr = StockRoute(name="Warehouse A → Retail B")
    sr.add_checkpoint("Loading Dock", lat=40.7128, lon=-74.006)
    sr.add_checkpoint("Distribution Center", lat=41.8781, lon=-87.6298)

    batch = Batch(id="B-2024-001")
    batch.add_item("Widget X", qty=500, price=9.99)
    sr.create_transfer(batch=batch, driver="Maria", vehicle_id="TRK-42")

    exc_note = ExceptionNote(
        checkpoint_id="Distribution Center",
        description="Traffic delay – ETA +4h",
        severity="minor"
    )
    sr.add_exception(exc_note)

    print(sr.summary())

# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: StockRoute
def reset_demo_data():
    """Reset all tracked entities to demo state for manual testing."""
    from stockroute.models import (
        StockMovement, DeliveryRoute, Transfer, Checkpoint, Batch, ExceptionNote
    )
    # Clear existing records
    StockMovement.objects.all().delete()
    DeliveryRoute.objects.all().delete()
    Transfer.objects.all().delete()
    Checkpoint.objects.all().delete()
    Batch.objects.all().delete()
    ExceptionNote.objects.all().delete()

    # Re-create demo data
    route = DeliveryRoute.objects.create(
        name="Main Distribution Route",
        start_point="Warehouse A",
        end_point="Retail Center B"
    )

    movement = StockMovement.objects.create(
        quantity=500,
        status="in_transit",
        route=route
    )

    transfer = Transfer.objects.create(
        source=movement,
        destination_location="Depot C"
    )

    checkpoint = Checkpoint.objects.create(
        location="Mile 42 Junction",
        timestamp="2024-01-15T10:30:00",
        notes="Traffic delay reported"
    )

    batch = Batch.objects.create(
        product_id="SKU-789",
        quantity=120,
        movement=movement
    )

    exception_note = ExceptionNote.objects.create(
        movement=movement,
        severity="warning",
        description="Delivery delayed due to weather conditions"
    )

    print("Demo data reset successfully. All entities populated with sample records.")

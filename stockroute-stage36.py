# === Stage 36: Add templates for quickly creating common records ===
# Project: StockRoute
# StockRoute - Templates for quick record creation
def create_default_records():
    """Create common template records for StockRoute."""
    today = datetime.date.today()
    
    # Create a new batch with default settings
    batch_id = f"BR-{today.year}-{today.month:02d}-{today.day:02d}"
    batch = Batch(batch_id=batch_id, description=f"Daily batch {batch_id}")
    
    # Create a checkpoint for the batch
    checkpoint = Checkpoint(
        checkpoint_id=1,
        location="Main Warehouse",
        status="active",
        timestamp=today
    )
    
    # Create an exception note template
    exception_note = ExceptionNote(
        note_id=1,
        description="Standard delivery delay due to traffic conditions",
        severity="warning",
        solution="Reschedule route via alternative path"
    )
    
    return batch, checkpoint, exception_note

# Usage example:
batch, cp, note = create_default_records()
print(f"Batch: {batch.batch_id}, Checkpoint: {cp.location}, Note: {note.description}")

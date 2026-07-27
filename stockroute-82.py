# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: StockRoute
def end_to_end_demo():
    """Walkthrough: create stock, set checkpoints, ship a batch with an exception, then report."""
    from stockroute import (StockRoute, Stock, Checkpoint, Transfer, Batch, ExceptionNote)

    sr = StockRoute(name="Main Plant")
    src = Stock("SRC", "raw_material_A", 100)
    dst = Stock("DST", "finished_goods_B", 0)

    cp1 = Checkpoint(transfer_id=1, stock=sr.stocks[0], qty=50, status="OK")
    cp2 = Checkpoint(transfer_id=1, stock=sr.stocks[0], qty=50, status="OK")
    sr.add_checkpoints(cp1, cp2)

    trf = Transfer(src, dst, "TRF-001", sr)
    exc = ExceptionNote(trf, reason="damaged during transit", severity="MEDIUM")
    batch = Batch(trf, qty=48, status="PARTIAL", exception_notes=[exc])
    sr.add_batch(batch)

    print(f"Route: {sr.name}")
    print(f"Stocks: {list(sr.stocks)}")
    print(f"Batches: {len(sr.batches)}, Transfers: {len(sr.transfers)}, Checkpoints: {len(sr.checkpoints)}")
    print(f"Batch summary: qty={batch.qty}, status={batch.status}, exception='{exc.reason}' severity={exc.severity}")

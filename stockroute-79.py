# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: StockRoute
def self_check():
    print("=== StockRoute Self-Check ===")
    from stockroute import models, repo, transfers, checkpoints, batches, exceptions
    # Load a sample route and verify all modules work together
    r = models.Route(name="Test Route", source="Warehouse A", destination="Shop B")
    assert isinstance(r, models.Route)
    cp1 = checkpoints.Checkpoint(route=r, location="Dock 3", status=checkpoints.Status.OK)
    cp2 = checkpoints.Checkpoint(route=r, location="Gate 7", status=checkpoints.Status.PENDING)
    t1 = transfers.Transfer(source=cp1, destination=cp2, qty=50, item="Widget X")
    b1 = batches.Batch(items=[t1], driver="Dave", date="2026-05-20")
    e1 = exceptions.Exception(item=t1, note="Driver reported delay", severity=exceptions.Severity.MEDIUM)
    assert isinstance(b1, batches.Batch) and isinstance(e1, exceptions.Exception)
    print("All modules instantiated successfully.")
    # Demo repository operations
    repo.store(r)
    assert repo.exists(r.name)
    repo.delete(r.name)
    assert not repo.exists(r.name)
    print("Repository store/delete cycle OK.")
    # Demo transfer and batch lifecycle
    repo.store(t1); repo.store(b1); repo.store(e1)
    assert repo.count() >= 3
    print(f"Repository contains {repo.count()} records.")
    print("=== Self-Check PASSED ===")

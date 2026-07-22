# === Stage 66: Add export of a short status dashboard ===
# Project: StockRoute
def export_status_dashboard(data):
    """Export a compact status dashboard from StockRoute data."""
    total_trips = sum(d.get("trips", 0) for d in data.values())
    active_batches = sum(1 for b in data.get("batches", []) if b.get("status") == "in_progress")
    completed_batches = sum(1 for b in data.get("batches", []) if b.get("status") == "completed")
    exceptions = [e["note"] for e in data.get("exceptions", [])]
    
    dashboard = {
        "total_trips": total_trips,
        "active_batches": active_batches,
        "completed_batches": completed_batches,
        "exceptions_count": len(exceptions),
        "status_summary": {
            "in_transit": sum(1 for b in data.get("batches", []) if b.get("status") == "in_progress"),
            "delivered": sum(1 for b in data.get("batches", []) if b.get("status") == "completed"),
            "failed": sum(1 for b in data.get("batches", []) if b.get("status") == "failed"),
        }
    }
    
    return dashboard

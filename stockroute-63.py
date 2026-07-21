# === Stage 63: Add relationships between records where useful ===
# Project: StockRoute
class StockRoute:
    def __init__(self):
        self.checkpoints = {}
        self.batches = {}
        self.transfers = []
        self.exceptions = []

    def register_checkpoint(self, name, location, status="open"):
        if name not in self.checkpoints:
            self.checkpoints[name] = {"name": name, "location": location, "status": status}
        return self.checkpoints[name]

    def add_batch(self, batch_id, items):
        self.batches[batch_id] = {"batch_id": batch_id, "items": list(items)}
        return self.batches[batch_id]

    def record_transfer(self, from_checkpoint, to_checkpoint, batch_id=None):
        transfer = {
            "from": from_checkpoint,
            "to": to_checkpoint,
            "timestamp": datetime.now().isoformat(),
            "status": "completed" if batch_id else "pending",
            "batch_ref": batch_id or None
        }
        self.transfers.append(transfer)
        return transfer

    def log_exception(self, checkpoint_name, description):
        self.exceptions.append({
            "checkpoint": checkpoint_name,
            "description": description,
            "timestamp": datetime.now().isoformat(),
            "resolved": False
        })
        return self.exceptions[-1]

    def get_route_status(self):
        route = {
            "checkpoints": dict(self.checkpoints),
            "batches": dict(self.batches),
            "transfers_count": len(self.transfers),
            "exceptions_count": len(self.exceptions)
        }
        return route

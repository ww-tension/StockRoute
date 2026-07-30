# === Stage 90: Add a final version constant and print it in the help output ===
# Project: StockRoute
def _version():
    major, minor, patch = sys.version_info[:3]
    return f"{major}.{minor}.{patch}"


class StockRoute:
    """Stock movement and delivery route tracker with transfers, checkpoints, batches, and exception notes."""

    def __init__(self):
        self._transfers = []
        self._checkpoints = []
        self._batches = []
        self._exceptions = []
        self._version = _version()

    @property
    def version(self):
        return self._version

    @property
    def transfers(self):
        return list(self._transfers)

    @property
    def checkpoints(self):
        return list(self._checkpoints)

    @property
    def batches(self):
        return list(self._batches)

    @property
    def exceptions(self):
        return list(self._exceptions)

    def add_transfer(self, origin=None, destination=None):
        self._transfers.append({"origin": origin, "destination": destination})

    def set_checkpoint(self, location=None, status=None):
        self._checkpoints.append({"location": location, "status": status or "active"})

    def create_batch(self, items=None, label=None):
        self._batches.append({"items": items, "label": label or f"Batch-{len(self._batches)}"})

    def log_exception(self, note=None, detail=None):
        self._exceptions.append({"note": note, "detail": detail})

    def print_summary(self):
        print(f"StockRoute v{self.version}")
        print(f"Transfers: {len(self._transfers)}")
        for t in self._transfers:
            print(f"  -> {t['origin']} to {t['destination']}")
        print(f"Checkpoints: {len(self._checkpoints)}")
        for c in self._checkpoints:
            print(f"  @ {c['location']}: {c['status']}")
        print(f"Batches: {len(self._batches)}")
        for b in self._batches:
            print(f"  [{b['label']}] items={b['items']}")
        print(f"Exceptions: {len(self._exceptions)}")
        for e in self._exceptions:
            print(f"  ! {e['note']}: {e['detail']}")


if __name__ == "__main__":
    sr = StockRoute()
    sr.add_transfer("Warehouse A", "Distribution Center B")
    sr.set_checkpoint("Main Gate", "active")
    sr.create_batch(["Item X", "Item Y"], label="Morning Run")
    sr.log_exception(note="Late shipment", detail="Driver unavailable")
    sr.print_summary()

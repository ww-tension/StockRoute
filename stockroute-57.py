# === Stage 57: Add structured result objects for command handlers ===
# Project: StockRoute
class RouteResult:
    def __init__(self, status="ok", message="", data=None):
        self.status = status
        self.message = message
        self.data = data

    @property
    def is_ok(self):
        return self.status == "ok"

    def to_dict(self):
        out = {"status": self.status}
        if self.message:
            out["message"] = self.message
        if self.data is not None:
            out["data"] = self.data.to_dict() if hasattr(self.data, "to_dict") else self.data
        return out

    def __repr__(self):
        return f"RouteResult(status={self.status!r}, message={self.message!r})"

# === Stage 18: Add an activity log with timestamps and action names ===
# Project: StockRoute
class ActivityLogger:
    def __init__(self, log_file="stockroute.log"):
        self.log_file = log_file

    def _format_log(self, action_name, details=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] ACTION: {action_name}"
        if details:
            entry += f" | DETAILS: {details}"
        return entry

    def log(self, action_name, **kwargs):
        line = self._format_log(action_name, str(kwargs))
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

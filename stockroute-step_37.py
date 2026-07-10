# === Stage 37: Add recommendations for the next useful action ===
# Project: StockRoute
def suggest_next_action(self):
    """Recommend a useful next step based on current route state."""
    if self.batches and all(b.status != "completed" for b in self.batches):
        return "Complete the oldest batch or add a new one."
    if any(n.status == "unhandled" for n in self.notes):
        return "Review unhandled exception notes and update their status."
    if not self.checkpoints:
        return "Add initial checkpoints (e.g., warehouse, transit hub)."
    next_cp = min(self.checkpoints, key=lambda c: c.order)
    if next_cp.status != "reached":
        return f"Mark checkpoint '{next_cp.name}' as reached and log arrival time."
    if self.route_log and not any(l.type == "summary" for l in self.route_log):
        return "Generate a route summary with total distance and average speed."

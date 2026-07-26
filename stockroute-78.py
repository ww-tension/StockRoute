# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: StockRoute
class _Checkpoint:
    def __init__(self, id=None): self.id = id
    @property
    def name(self): return f"CP-{self.id}" if self.id else "Unnamed"

class _Transfer:
    def __init__(self, source, target, qty=0): self.source = source; self.target = target; self.qty = qty
    def log(self): return f"[{self.source}] -> [{self.target}]: {self.qty}"

class _Batch:
    def __init__(self, items=None): self.items = list(items) if items else []
    @property
    def count(self): return len(self.items)
    def add(self, item): self.items.append(item); return self

class _ExceptionNote:
    def __init__(self, message=""): self.message = message
    def severity(self): return "HIGH" if any(k in self.message for k in ("STOP","CRITICAL")) else "MEDIUM" if "?" in self.message else "LOW"

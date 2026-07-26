# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: StockRoute
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Checkpoint:
    """A checkpoint in a delivery route."""
    name: str
    passed: bool = True
    timestamp: Optional[date] = None

    def __repr__(self) -> str:
        status = "✓" if self.passed else "✗"
        return f"[{status}] {self.name}"


@dataclass
class Batch:
    """A batch of stock items moving together."""
    id: int
    items: List[str] = field(default_factory=list)

    def add_item(self, item: str) -> None:
        self.items.append(item)

    @property
    def size(self) -> int:
        return len(self.items)


@dataclass
class TransferRecord:
    """A transfer between locations."""
    from_location: str
    to_location: str
    quantity: float
    date: Optional[date] = None

    def __repr__(self) -> str:
        return f"Transfer({self.from_location} → {self.to_location}, qty={self.quantity})"


@dataclass
class ExceptionNote:
    """An exception or issue in the delivery process."""
    description: str
    severity: str = "low"  # low, medium, high
    resolved: bool = False

    def __repr__(self) -> str:
        flag = "RESOLVED" if self.resolved else ""
        return f"[{flag}] {self.description} (severity={self.severity})"


def validate_quantity(value: float) -> None:
    """Raise ValueError if quantity is negative."""
    if value < 0:
        raise ValueError(f"Quantity cannot be negative: {value}")


def format_report(checkpoints: List[Checkpoint], batches: List[Batch]) -> str:
    """Return a simple text report of checkpoints and batches."""
    lines = [f"=== StockRoute Report ==="]
    for cp in checkpoints:
        lines.append(str(cp))
    lines.append("---")
    for batch in batches:
        lines.append(f"Batch#{batch.id}: {', '.join(batch.items)} (size={batch.size})")
    return "\n".join(lines)

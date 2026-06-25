# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: StockRoute
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Checkpoint:
    id: int
    location: str
    timestamp: date
    status: str = "pending"
    
@dataclass 
class Batch:
    batch_id: str
    product_name: str
    quantity: int
    origin_checkpoint: Optional[Checkpoint] = None
    destination_checkpoint: Optional[Checkpoint] = None
    
@dataclass
class ExceptionNote:
    note_id: int
    batch_ref: str
    description: str
    severity: str = "low"
    resolved_at: Optional[date] = None

@dataclass
class TransferRecord:
    transfer_id: int
    from_batch: Batch
    to_batch: Optional[Batch] = None
    checkpoint_log: List[Checkpoint] = field(default_factory=list)
    exceptions: List[ExceptionNote] = field(default_factory=list)

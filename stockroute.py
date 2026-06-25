# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: StockRoute
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import uuid

@dataclass
class Checkpoint:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    location: str = ""
    timestamp: float = 0.0
    
@dataclass 
class Batch:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: int = 0
    status: str = "pending"

class StockRouteState:
    def __init__(self):
        self.batches: Dict[str, Batch] = {}
        self.checkpoints: List[Checkpoint] = []
        
    def create_batch(self) -> Batch:
        batch = Batch()
        self.batches[batch.id] = batch
        return batch
        
    def record_checkpoint(self, location: str):
        cp = Checkpoint(location=location)
        self.checkpoints.append(cp)

state = StockRouteState()
b1 = state.create_batch()
cp1 = state.record_checkpoint("Warehouse A")

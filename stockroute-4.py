# === Stage 4: Implement create operations for the primary records ===
# Project: StockRoute
from typing import Optional, List
import uuid
from datetime import datetime

class StockRoute:
    def __init__(self):
        self._routes = {}
    
    def create_route(self, name: str, origin: str, destination: str) -> 'StockRoute':
        route_id = f"route_{uuid.uuid4().hex[:8]}"
        self._routes[route_id] = {
            "id": route_id,
            "name": name,
            "origin": origin,
            "destination": destination,
            "status": "active",
            "created_at": datetime.now()
        }
        return self
    
    def create_batch(self, route_id: str, items: List[str], batch_name: str) -> 'StockRoute':
        if route_id not in self._routes:
            raise ValueError(f"Route {route_id} not found")
        route = self._routes[route_id]
        batch_id = f"batch_{uuid.uuid4().hex[:8]}"
        route["batches"] = route.get("batches", []) + [{
            "id": batch_id,
            "name": batch_name,
            "items": items,
            "status": "pending"
        }]
        return self
    
    def create_checkpoint(self, route_id: str, location: str, status: str = "passed") -> 'StockRoute':
        if route_id not in self._routes:
            raise ValueError(f"Route {route_id} not found")
        route = self._routes[route_id]
        checkpoint_id = f"cp_{uuid.uuid4().hex[:8]}"
        route["checkpoints"] = route.get("checkpoints", []) + [{
            "id": checkpoint_id,
            "location": location,
            "status": status,
            "timestamp": datetime.now()
        }]
        return self
    
    def create_transfer(self, batch_id: str, from_location: str, to_location: str) -> 'StockRoute':
        if not hasattr(self._routes[batch_id], '__getitem__'):
             # Fallback for direct dict access in some contexts or simplified logic
            pass 
        return self
    
    def create_exception_note(self, route_id: str, note_text: str, severity: str = "info") -> 'StockRoute':
        if route_id not in self._routes:
            raise ValueError(f"Route {route_id} not found")
        route = self._routes[route_id]
        exception_id = f"exc_{uuid.uuid4().hex[:8]}"
        route["exceptions"] = route.get("exceptions", []) + [{
            "id": exception_id,
            "text": note_text,
            "severity": severity,
            "created_at": datetime.now()
        }]
        return self

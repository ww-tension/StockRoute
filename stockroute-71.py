# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: StockRoute
def seed_demo_data(db):
    db["users"].insert_many([
        {"name": "Alice",  "role": "manager"},
        {"name": "Bob",    "role": "driver"},
        {"name": "Charlie","role": "supervisor"}
    ])
    db["warehouses"].insert_many([
        {"id": 1, "name": "WH-Central",   "city": "Paris"},
        {"id": 2, "name": "WH-North",     "city": "Lyon"},
        {"id": 3, "name": "WH-East",      "city": "Marseille"}
    ])
    db["vehicles"].insert_many([
        {"id": 10, "type": "truck",   "capacity_kg": 5000},
        {"id": 11, "type": "van",     "capacity_kg": 800},
        {"id": 12, "type": "bike",    "capacity_kg": 30}
    ])
    db["stock_items"].insert_many([
        {"sku": "A-101","name": "Widget",   "weight_kg": 5.0},
        {"sku": "B-202","name": "Gadget",   "weight_kg": 1.5},
        {"sku": "C-303","name": "Module",   "weight_kg": 12.0}
    ])
    db["batches"].insert_many([
        {"batch_id": "B001", "item_sku": "A-101", "qty": 50,  "status": "ready"},
        {"batch_id": "B002", "item_sku": "B-202", "qty": 30,  "status": "in_transit"},
        {"batch_id": "B003", "item_sku": "C-303", "qty": 10,  "status": "ready"}
    ])
    db["routes"].insert_many([
        {"route_id": "R001","from_wh": 2,"to_wh": 1},
        {"route_id": "R002","from_wh": 3,"to_wh": 2}
    ])
    db["transfers"].insert_many([
        {"transfer_id":"T001",   "batch_id":"B001","vehicle_id":10,"status":"completed"},
        {"transfer_id":"T002",   "batch_id":"B002","vehicle_id":11,"status":"in_transit"}
    ])
    db["checkpoints"].insert_many([
        {"cp_id":"CP01","route_id":"R001","location":"Paris Hub","arrival_time":"2025-06-01 08:00"},
        {"cp_id":"CP02","route_id":"R001","location":"Warehouse 1","arrival_time":"2025-06-01 10:30"}
    ])
    db

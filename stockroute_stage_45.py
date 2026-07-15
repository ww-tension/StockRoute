# === Stage 45: Add restore from backup with validation ===
# Project: StockRoute
import os, json, datetime, hashlib

def restore_backup(source_path, target_dir):
    if not os.path.isfile(source_path):
        raise FileNotFoundError("Backup file does not exist")
    
    with open(source_path, 'r') as f:
        data = json.load(f)
    
    required_keys = ['routes', 'batches', 'exceptions']
    for key in required_keys:
        if key not in data or not isinstance(data[key], list):
            raise ValueError(f"Invalid backup structure: missing '{key}'")
    
    if len(data['routes']) == 0 and len(data['batches']) == 0 and len(data['exceptions']) == 0:
        raise ValueError("Backup contains no valid data")
    
    target_file = os.path.join(target_dir, 'data.json')
    with open(target_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    checksum = hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()[:8]
    print(f"Backup restored to {target_file} (checksum: {checksum})")

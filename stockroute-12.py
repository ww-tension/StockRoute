# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: StockRoute
import json, sys

def load_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Malformed JSON in '{path}': {e}")
        sys.exit(1)

def export_safe(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write '{path}': {e}")
        return False

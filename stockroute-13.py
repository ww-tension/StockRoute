# === Stage 13: Add file save support using a configurable path ===
# Project: StockRoute
import os, json, uuid
from pathlib import Path
from datetime import datetime
class Config:
    def __init__(self):
        self.data_dir = Path.home() / ".stockroute" / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.config_file = self.data_dir / "config.json"
        if not self.config_file.exists():
            default_config = {
                "routes": [], "batches": {}, "exceptions": [], "users": []
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, ensure_ascii=False, indent=2)

    def save_state(self):
        state = {
            "routes": self.routes,
            "batches": self.batches,
            "exceptions": self.exceptions,
            "users": self.users,
            "last_updated": datetime.now().isoformat()
        }
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)

    def load_state(self):
        if not self.config_file.exists(): return None
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception: return None

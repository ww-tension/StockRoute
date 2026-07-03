# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: StockRoute
from datetime import datetime, timedelta
import json
from pathlib import Path

def archive_old_records(db_path: str, days_threshold: int = 365):
    """Move records older than threshold to an 'archive' subdirectory."""
    db_file = Path(db_path)
    if not db_file.exists(): return
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archive_dir = db_file.parent / "archive"
    
    with open(db_file, 'r', encoding='utf-8') as f:
        records = json.load(f)
    
    current_records = []
    archived_count = 0
    
    for record in records:
        if isinstance(record.get('completed_at'), str):
            try:
                completed_dt = datetime.fromisoformat(record['completed_at'].replace('Z', '+00:00'))
            except ValueError:
                continue
        else:
            continue
            
        if completed_dt < cutoff_date:
            archive_dir.mkdir(parents=True, exist_ok=True)
            filename = f"record_{record.get('id', 'unknown')}.json"
            with open(archive_dir / filename, 'w', encoding='utf-8') as af:
                json.dump(record, af, ensure_ascii=False, indent=2)
            archived_count += 1
        else:
            current_records.append(record)
    
    if archived_count > 0:
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(current_records, f, ensure_ascii=False, indent=2)

def restore_from_archive(archive_dir: str | None = None):
    """Restore all archived records back to the main database."""
    if archive_dir is None:
        return
    
    archive_path = Path(archive_dir)
    if not archive_path.exists(): return
    
    db_file = Path("stock_route_db.json") # Assumes default location relative to script or passed context
    
    restored_count = 0
    all_records = []
    
    for file in archive_path.glob("*.json"):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                record = json.load(f)
            all_records.append(record)
            restored_count += 1
        except (json.JSONDecodeError, IOError):
            continue
            
    if restored_count > 0:
        # Append to existing or create new main DB
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(all_records, f, ensure_ascii=False, indent=2)

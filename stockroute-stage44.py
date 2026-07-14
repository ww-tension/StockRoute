# === Stage 44: Add backup creation for the data file ===
# Project: StockRoute
import os, shutil, sys

def backup_data_file(source_path: str) -> tuple[str | None, bool]:
    """Create a timestamped backup of the data file and return (backup_path_or_None, success)."""
    try:
        parent = os.path.dirname(source_path)
        stem   = os.path.splitext(os.path.basename(source_path))[0]
        ext    = os.path.splitext(source_path)[1] or '.dat'
        now    = os.path.getmtime(source_path)
        backup_name = f"{stem}_backup_{now}.bkp"
        backup_path = os.path.join(parent, backup_name)
        shutil.copy2(source_path, backup_path)
        return backup_path, True
    except Exception:
        return None, False

if __name__ == '__main__':
    data_file = sys.argv[1] if len(sys.argv) > 1 else 'stock_route.dat'
    bk, ok = backup_data_file(data_file)
    print(f"Backup {'created at' if ok else 'failed'}: {bk}" if ok else f"Error: {data_file}")

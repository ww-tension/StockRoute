# === Stage 46: Add a schema version field and migration helper ===
# Project: StockRoute
# Step 46: Schema version + migration helper (append to existing project.py)
SCHEMA_VERSION = 3


def migrate(old_version, new_version):
    """Apply schema migrations between versions."""
    if old_version >= new_version:
        return
    if old_version == 0 and new_version == 1:
        print("Mig 0→1: added 'version' field to StockRecord.")
    elif old_version == 1 and new_version == 2:
        print("Mig 1→2: added 'note' field to StockRecord.")
    elif old_version == 2 and new_version == 3:
        print("Mig 2→3: added 'schema_version' meta-field.")

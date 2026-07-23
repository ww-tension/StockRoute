# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: StockRoute
def generate_changelog():
    """Generate a compact changelog from activity log entries."""
    changes = []
    with open("activity_log.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(", ", 3)
        version, date, description, author = parts[0], parts[1], parts[2], parts[3]
        changes.append(f"  - {version} ({date}): {description} by {author}")
    with open("CHANGELOG.txt", "w") as f:
        f.write("StockRoute Changelog\n")
        for change in changes:
            f.write(change + "\n")

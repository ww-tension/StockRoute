# === Stage 32: Add pagination helpers for long console output ===
# Project: StockRoute
def page_lines(lines, per_page=30):
    """Split a list of strings into chunks and display them paginated."""
    for i in range(0, len(lines), per_page):
        chunk = lines[i:i+per_page]
        print(f"--- Page {i // per_page + 1} ---")
        for line in chunk:
            print(line)

def paginate_output(records, title="StockRoute Output", per_page=30):
    """Paginate any iterable of records (strings or dicts)."""
    if not hasattr(records, '__iter__'):
        return
    if isinstance(records[0], dict):
        lines = [f"{r.get('id', '?')}: {r.get('desc', '')}" for r in records]
    else:
        lines = list(records)
    page_lines(lines, per_page=per_page)

def clear_screen():
    """Clear the console for a fresh view."""
    print("\033[H\033[2J", end="")

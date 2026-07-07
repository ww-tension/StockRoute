# === Stage 31: Add compact table rendering for long lists ===
# Project: StockRoute
def render_compact_table(items, columns):
    """Render a compact table for long lists of items."""
    header = " | ".join(columns) + " |"
    separator = "-+-".join(["-" * max(len(col), 8) for col in columns]) + "-"
    rows = []
    for item in items:
        row_values = [str(item.get(col, ""))[:40] if isinstance(item.get(col), str) else str(item.get(col)) for col in columns]
        rows.append(" | ".join(row_values) + " |")
    return "\n".join([header, separator] + rows)

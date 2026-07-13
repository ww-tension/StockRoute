# === Stage 41: Add plain text import for a simple line-based format ===
# Project: StockRoute
def parse_plain_lines(lines):
    """Parse a simple line-based plain text format into structured records.

    Expected input:
        Line 1: "header" keyword
        Subsequent lines: "field1;field2;field3..." separated by semicolons.
        A blank line separates logical groups (batches).

    Returns list of dicts with keys from the header row.
    """
    records = []
    current_header = None
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line == "header":
            continue
        fields = [f.strip() for f in line.split(";")]
        if current_header is None:
            current_header = [h.strip().lower() for h in fields]
            records.append({})  # placeholder to keep index aligned
        else:
            record = {}
            for key, val in zip(current_header, fields):
                record[key] = val
            if record.get("type") == "batch":
                records[-1].update(record)
            else:
                records.append(record)
    return records

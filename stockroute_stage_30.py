# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: StockRoute
def parse_date(date_str):
    """Parse date strings like '2024-01-15', 'Jan 15, 2024', and return a datetime.date."""
    if not isinstance(date_str, str) or not date_str.strip():
        raise ValueError(f"Invalid date string: '{date_str}'")
    
    formats = [
        ("%Y-%m-%d", None),
        ("%d/%m/%Y", None),
        ("%m/%d/%Y", None),
        ("%b %d, %Y", None),
        ("%B %d, %Y", None),
        ("%d-%m-%Y", None),
    ]
    
    for fmt, _ in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY, Mon DD YYYY")

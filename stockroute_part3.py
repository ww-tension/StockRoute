# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: StockRoute
def validate_required(value, field_name):
    if value is None:
        raise ValueError(f"{field_name} cannot be empty")
    return True

def validate_identifier(identifier, prefix="ID"):
    if identifier and (not isinstance(identifier, str) or not identifier.strip()):
        raise ValueError(f"Invalid {prefix}: must be a non-empty string")
    return identifier is None or len(identifier.replace("-", "").replace("_", "")) <= 20

def validate_short_text(text, max_length=100):
    if text and (not isinstance(text, str) or not text.strip()):
        raise ValueError(f"Text must be a non-empty string")
    return True if len(text) <= max_length else False

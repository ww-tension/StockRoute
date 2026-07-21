# === Stage 64: Add validation for relationship references ===
# Project: StockRoute
def validate_relationship_references(data, schema):
    errors = []
    for entity_name, fields in data.items():
        if entity_name not in schema:
            continue
        required_refs = [f["ref"] for f in schema[entity_name]["fields"].values() if "ref" in f]
        valid_values = set(schema[entity_name]["fields"][f]["allowed"]) if "allowed" in schema[entity_name]["fields"][f] else None
        for field, ref in zip(fields.keys(), required_refs):
            if field not in fields:
                errors.append(f"{ref} missing from {entity_name}")
                continue
            val = fields[field]
            if valid_values is not None and val not in valid_values:
                errors.append(f"Invalid {ref} value '{val}' for {entity_name}.{field}")

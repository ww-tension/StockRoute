# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: StockRoute
def toggle_tag(item_id, tag_name):
    if item_id in _tags:
        if tag_name in _tags[item_id]:
            del _tags[item_id][tag_name]
            return True
    else:
        _tags[item_id] = {tag_name: None}
        return True

def get_tag_summary(tag_name):
    items_with_tag = [k for k, v in _tags.items() if tag_name in v]
    return len(items_with_tag)

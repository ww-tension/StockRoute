# === Stage 35: Add active user switching and user-specific records ===
# Project: StockRoute
def switch_active_user(username):
    active_users = {u: u for u in _get_all_users()}
    if username not in active_users:
        raise ValueError(f"User '{username}' does not exist")
    current = next((user for user in active_users.values() if user.is_active), None)
    new_user = active_users[username]
    if current and current != new_user:
        current.is_active = False
    new_user.is_active = True

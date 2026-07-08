# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: StockRoute
DEFAULT_SETTINGS = {
    "default_batch_size": 10,
    "max_checkpoints_per_day": 24,
    "enable_notifications": False,
    "notification_timeout_seconds": 5,
    "allowed_exception_codes": ["TEMP", "DAMAGED", "DELAYED"],
}


def get_settings():
    """Return a copy of the current settings dictionary."""
    return DEFAULT_SETTINGS.copy()


def update_setting(key, value):
    """Update or add a single setting and return True on success.

    Returns False if the key is not recognised so callers can detect errors.
    """
    if key not in DEFAULT_SETTINGS:
        return False
    DEFAULT_SETTINGS[key] = value
    return True


def reset_settings():
    """Reset every setting to its default value."""
    for k in DEFAULT_SETTINGS:
        DEFAULT_SETTINGS[k] = DEFAULT_SETTINGS[k].copy() if isinstance(DEFAULT_SETTINGS[k], list) else DEFAULT_SETTINGS[k]

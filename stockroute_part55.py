# === Stage 55: Add a setting to disable colorized output ===
# Project: StockRoute
class Settings:
    """Central settings for StockRoute."""
    def __init__(self):
        self.colorize = True
    
    def disable_color(self):
        """Disable colorized output."""
        self.colorize = False
    
    @property
    def is_color_on(self):
        return self.colorize

settings = Settings()
print(f"Color on: {settings.is_color_on}")

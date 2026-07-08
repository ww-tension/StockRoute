# === Stage 34: Add support for multiple local user profiles ===
# Project: StockRoute
class UserProfiles:
    def __init__(self, profiles_dir="profiles"):
        self.profiles_dir = profiles_dir
        self._load()

    def _profile_path(self, name):
        return os.path.join(self.profiles_dir, f"{name}.json")

    def load_profile(self, name):
        path = self._profile_path(name)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Profile '{name}' not found at {path}")
        with open(path, "r") as f:
            return json.load(f)

    def save_profile(self, name, data):
        path = self._profile_path(name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def list_profiles(self):
        if not os.path.isdir(self.profiles_dir):
            return []
        return sorted(
            [p.replace(".json", "") for p in os.listdir(self.profiles_dir) if p.endswith(".json")]
        )

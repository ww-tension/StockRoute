# === Stage 22: Add favorite records and quick favorite listing ===
# Project: StockRoute
class FavoriteManager:
    def __init__(self, db):
        self.db = db
    
    def toggle_favorite(self, record_id):
        with self.db.cursor() as cur:
            cur.execute("SELECT is_fav FROM records WHERE id=?", (record_id,))
            row = cur.fetchone()
            if not row or row[0]: return False
            cur.execute("UPDATE records SET is_fav=1 WHERE id=?", (record_id,))
            self.db.commit()
            return True
    
    def get_favorites(self):
        with self.db.cursor() as cur:
            cur.execute("SELECT * FROM records WHERE is_fav=1 ORDER BY created_at DESC")
            return cur.fetchall()

def main():
    from stockroute import StockRouteApp
    app = StockRouteApp('data.sqlite')
    fav_mgr = FavoriteManager(app.db)
    
    # Toggle favorite for a specific record (e.g., ID 5)
    if fav_mgr.toggle_favorite(5):
        print("Record marked as favorite.")
    else:
        print("No change or already favorited.")
    
    # List all favorites
    favorites = fav_mgr.get_favorites()
    for rec in favorites:
        print(f"ID:{rec[0]} | Type:{rec[1]} | Status:{rec[2]}")

if __name__ == "__main__":
    main()

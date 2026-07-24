# === Stage 72: Add Markdown report export ===
# Project: StockRoute
import csv, datetime

def export_report(trips, output="report.csv"):
    with open(output, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["trip","from","to","distance_km","status","driver"])
        for t in trips:
            w.writerow([t["id"], t.get("origin"), t.get("destination"),
                         t.get("distance_km", ""), t.get("status", ""),
                         t.get("driver_name", "")])
    print(f"Report written to {output}")

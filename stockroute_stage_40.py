# === Stage 40: Add plain text report export ===
# Project: StockRoute
def export_plain_text_report(routes, output_path):
    """Export all stock routes as a plain text report."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== StockRoute Plain Text Report ===\n\n")
        for route in routes:
            f.write(f"Route ID : {route['id']}\n")
            f.write(f"  Driver : {route['driver']['name']} ({route['driver']['phone']})\n")
            f.write(f"  Status : {route['status']}\n")
            for check in route["checkpoints"]:
                f.write(f"    [{check['order']}] ")
                if check["type"] == "delivery":
                    f.write(
                        f"{check['location']['name']} | qty: {check.get('quantity', 0)}\n"
                    )
                else:
                    f.write(f"{check['location']['name']} (transferred)\n")
            if route["exceptions"]:
                for exc in route["exceptions"]:
                    f.write(
                        f"    EXCEPTION : {exc.get('type', 'unknown')} - "
                        f"{exc.get('description', '')}\n"
                    )
            f.write("\n")

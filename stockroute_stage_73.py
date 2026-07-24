# === Stage 73: Add a lightweight HTML report export ===
# Project: StockRoute
def export_html_report(routes, output_path):
    from html import escape
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>StockRoute Report</title>')
        f.write('<style>table{border-collapse:collapse;margin:16px;font-family:sans-serif}td,th{padding:4px 10px;border-bottom:1px solid #ccc}</style></head><body>')
        f.write(f'<h1>StockRoute Report</h1><p>Generated with {len(routes)} route(s).</p>')
        for r in routes:
            f.write('<table><tr><th>ID</th><th>Origin</th><th>Destination</th><th>Status</th></tr>')
            f.write(f'<tr><td>{r["id"]}</td><td>{escape(r.get("origin", "N/A"))}</td><td>{escape(r.get("destination", "N/A"))}</td><td>{escape(r.get("status", "unknown"))}</td></tr>')
            f.write('</table>')
        f.write('<p>Exported successfully.</p></body></html>')

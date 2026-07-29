# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: StockRoute
def compare_reports(ref, new):
    """Compare two exported reports and return a summary dict."""
    diffs = {}
    for key in ref:
        if key not in new:
            diffs[key] = ('missing', ref[key], None)
        elif ref[key] != new[key]:
            diffs[key] = ('changed', ref[key], new[key])

def report_checksum(report):
    """Return a simple string checksum for quick diffing."""
    return str(sorted(report.items()))

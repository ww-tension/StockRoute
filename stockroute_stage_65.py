# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: StockRoute
import os, sys
from pathlib import Path

# Merge imports across all .py files in a given directory (or current dir),
# keeping only the first occurrence of each module.
def merge_imports(directory=".", output=None):
    """Collect unique module top-level names from every .py file."""
    seen = set()
    merged_order = []  # preserve first-seen order
    for pyfile in sorted(Path(directory).rglob("*.py")):
        try:
            with open(pyfile, "r", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    # Match top-level import / from ... import statements.
                    m = re.match(r"^import\s+([\w,\s]+)", line)
                    if m:
                        mod = [x.strip().split(".")[0] for x in m.group(1).split(",") if x.strip()]
                    else:
                        m = re.match(r"^\s*from\s+([\w.]+)\s+import", line)
                        if m:
                            mod = [m.group(1).split(".")[0]]
                        else:
                            continue
                    for module in mod:
                        if module not in seen and module != "StockRoute":
                            seen.add(module)
                            merged_order.append((pyfile.name, line))
        except Exception:
            pass

    # Write a single consolidated Python file.
    out = output or Path(directory) / "_merged_imports.py"
    with open(out, "w") as f:
        for fname, line in merged_order[:60]:  # cap at 60 unique lines
            f.write(line + "\n")
    return len(merged_order)

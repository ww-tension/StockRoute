# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: StockRoute
import sys, os

def color(text, fg=None, bg=None):
    """Return ANSI-colored text string."""
    codes = []
    if fg:
        codes.append(f"\033[3{fg}m")
    if bg:
        codes.append(f"\033[4{bg}m")
    code = "".join(codes) + "\033[0m"
    return f"{code}{text}\n"

class Printer:
    def __init__(self, stream=None):
        self.stream = stream or sys.stdout

    def header(self, title):
        self.stream.write(color(f"\n═══ {title} ═══", fg=1, bg=4))

    def info(self, msg):
        self.stream.write(color(msg, fg=2))

    def success(self, msg):
        self.stream.write(color(msg, fg=2, bg=1))

    def warning(self, msg):
        self.stream.write(color(f"⚠ {msg}", fg=3))

    def error(self, msg):
        self.stream.write(color(f"✖ {msg}", fg=5))

    def log(self, *args):
        print(*args, file=self.stream)

    def checkpoint(self, name, status="done", detail=None):
        icon = "✓" if status == "done" else "✗"
        line = f"\n[{icon}] {name}"
        self.stream.write(color(line, fg=1, bg=4))
        if detail:
            self.stream.write(f"   → {detail}\n")

    def batch_summary(self, total, passed, failed):
        rate = f"{passed}/{total}" if total else "0/0"
        color_code = 2 if failed == 0 else (3 if failed <= 5 else 5)
        self.stream.write(color(f"\nBatch: {rate} ({failed} failures)", fg=color_code))

    def exception_note(self, note):
        self.stream.write(color(f"\n[!] Exception Note: {note}", fg=5))

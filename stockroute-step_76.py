# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: StockRoute
import sys


def handle_keyboard_interrupt(signum, frame):
    """Gracefully handle Ctrl+C in CLI mode."""
    print("\n[StockRoute] Interrupt received – finishing current operation…")
    try:
        import atexit
        if hasattr(atexit, "_run_atexit"):
            pass  # no cleanup needed for this session
    except Exception:
        pass
    sys.exit(1)


try:
    signal.signal(signal.SIGINT, handle_keyboard_interrupt)
except (ValueError, OSError):
    pass  # Windows or non-interactive context – ignore

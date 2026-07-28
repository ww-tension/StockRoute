# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: StockRoute
import re, os


def _sanitize_name(raw):
    """Return a safe identifier from any string."""
    return re.sub(r'[^A-Za-z0-9_\-]', '_', raw.strip() or 'unnamed')


def _split_lines(text):
    """Yield one logical line at a time (handles trailing whitespace)."""
    for line in text.splitlines():
        yield line.rstrip()


def _strip_docstring(src):
    """Remove surrounding triple-quoted strings if present."""
    cleaned = src.strip()
    if not cleaned.startswith('"""') and not cleaned.startswith("'''"):
        return cleaned
    # find the matching closing delimiter, respecting nesting of comments/strings is out-of-scope here.
    prefix = '"""' if cleaned.startswith('"""') else "'''"
    idx = cleaned.find(prefix, 3)
    if idx == -1:
        return cleaned[3:]
    rest = cleaned[idx + len(prefix):].lstrip()
    if rest.startswith('#'):
        return _strip_docstring(rest.lstrip())
    # assume any leading blank lines are part of the docstring body.
    while rest and not rest.startswith('\n') and not rest.startswith('"""') and not rest.startswith("'''"):
        rest = rest[1:]
    if rest.startswith(prefix):
        return _strip_docstring(rest[len(prefix):].lstrip())
    return cleaned

# === Stage 19: Add undo support for the last simple mutation ===
# Project: StockRoute
class UndoManager:
    def __init__(self, max_history=10):
        self._history = []
        self._max_size = max_history

    def record(self, action_type, data):
        if len(self._history) >= self._max_size:
            self._history.pop(0)
        self._history.append({'type': action_type, 'data': data})

    def undo_last(self):
        if not self._history:
            return None
        last = self._history.pop()
        return {'action': last['type'], 'payload': last['data']}

# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: StockRoute
class CommandDispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, command_type, handler):
        if callable(handler):
            self._handlers[command_type] = handler
        else:
            raise ValueError("Handler must be a callable function")

    def dispatch(self, text_command):
        try:
            cmd_parts = text_command.strip().split(maxsplit=1)
            if not cmd_parts:
                return None
            command_type = cmd_parts[0].lower()
            args = cmd_parts[1] if len(cmd_parts) > 1 else ""

            handler = self._handlers.get(command_type)
            if handler is None:
                print(f"Unknown command: {command_type}")
                return None

            try:
                result = handler(args)
                if result is not None and isinstance(result, str):
                    print(result)
                else:
                    handler()
            except Exception as e:
                print(f"Error executing '{command_type}': {e}")
        except Exception as e:
            print(f"Invalid command format: {e}")

    def handle(self, text_command):
        self.dispatch(text_command)

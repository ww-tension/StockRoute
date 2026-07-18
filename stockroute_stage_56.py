# === Stage 56: Add compact error classes for domain failures ===
# Project: StockRoute
class StockRouteError(Exception):
    pass


class BatchNotFoundError(StockRouteError):
    def __init__(self, batch_id: str) -> None:
        super().__init__(f"Batch '{batch_id}' not found")
        self.batch_id = batch_id


class CheckpointNotFoundError(StockRouteError):
    def __init__(self, checkpoint_id: str) -> None:
        super().__init__(f"Checkpoint '{checkpoint_id}' not found")
        self.checkpoint_id = checkpoint_id


class TransferNotFoundError(StockRouteError):
    def __init__(self, transfer_id: str) -> None:
        super().__init__(f"Transfer '{transfer_id}' not found")
        self.transfer_id = transfer_id


class ExceptionNoteNotFound(StockRouteError):
    def __init__(self, note_id: str) -> None:
        super().__init__(f"Exception note '{note_id}' not found")
        self.note_id = note_id


class InvalidRouteError(StockRouteError):
    pass


class StockMovementError(StockRouteError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class BatchConflictError(StockRouteError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

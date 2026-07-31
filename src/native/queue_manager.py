"""Download queue management.

Owns queue items and their state transitions. Download execution is
handled by the download engine.
"""


class QueueManager:
    STATE_PENDING = "pending"
    STATE_ACTIVE = "active"
    STATE_PAUSED = "paused"
    STATE_FAILED = "failed"
    STATE_COMPLETED = "completed"
    STATE_CANCELLED = "cancelled"

    def __init__(self):
        self.items = []

    def add_item(self, item):
        raise NotImplementedError("Queue item addition is not implemented.")

    def pause_item(self, item_id):
        raise NotImplementedError("Queue pausing is not implemented.")

    def resume_item(self, item_id):
        raise NotImplementedError("Queue resuming is not implemented.")

    def remove_item(self, item_id):
        raise NotImplementedError("Queue item removal is not implemented.")

    def retry_item(self, item_id):
        raise NotImplementedError("Queue retry is not implemented.")

"""VaultTube native host entry point.

Reads Native Messaging requests from stdin, dispatches them to the
backend modules, and writes responses to stdout.
"""

import os
import sys

from database import Database
from download_engine import DownloadEngine
from file_manager import DEFAULT_DATA_DIRECTORY, FileManager
from messaging import (
    error_response,
    read_message,
    success_response,
    validate_request,
    write_message,
)
from queue_manager import QueueManager
from system_checks import SystemChecks

DATABASE_FILE_NAME = "vaulttube.db"


class Application:
    def __init__(self):
        self.system_checks = SystemChecks()
        self.database = Database(os.path.join(DEFAULT_DATA_DIRECTORY, DATABASE_FILE_NAME))
        self.queue_manager = QueueManager()
        self.download_engine = DownloadEngine()
        self.file_manager = FileManager()
        self.commands = {
            "system.check": self.system_checks.run,
            "system.ping": self.ping,
        }

    def ping(self):
        return {"message": "pong"}

    def dispatch(self, request):
        error = validate_request(request)
        if error is not None:
            raise ValueError(error)
        handler = self.commands.get(request["command"])
        if handler is None:
            raise ValueError(f"Unknown command: {request['command']}")
        return handler()


def main():
    application = Application()
    while True:
        request = read_message(sys.stdin.buffer)
        if request is None:
            break
        try:
            response = success_response(application.dispatch(request))
        except Exception as error:
            response = error_response(str(error))
        write_message(sys.stdout.buffer, response)


if __name__ == "__main__":
    main()

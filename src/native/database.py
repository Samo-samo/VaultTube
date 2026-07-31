"""SQLite database operations.

Owns the database connection and schema initialization. All persistent
data is stored locally in a single SQLite database file.
"""

import sqlite3


class Database:
    def __init__(self, path):
        self.path = path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row

    def initialize(self):
        raise NotImplementedError("Database schema initialization is not implemented.")

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

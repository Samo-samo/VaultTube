"""File and directory management.

Handles download directories, output file naming, and reporting of file
locations to the database.
"""

import os

DEFAULT_DATA_DIRECTORY = "user_data"


class FileManager:
    def ensure_directory(self, path):
        os.makedirs(path, exist_ok=True)

    def build_output_path(self, directory, title, extension):
        raise NotImplementedError("Output path building is not implemented.")

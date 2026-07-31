"""System dependency checks.

Verifies that required tools are available and that required paths are
accessible before downloads are started.
"""

import os
import subprocess
import sys


class SystemChecks:
    def __init__(self, database_path, data_directory):
        self.database_path = database_path
        self.data_directory = data_directory

    def _command_check(self, name, arguments):
        try:
            result = subprocess.run(
                [name, *arguments],
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired):
            return {"name": name, "ok": False, "version": None}
        if result.returncode != 0:
            return {"name": name, "ok": False, "version": None}
        return {"name": name, "ok": True, "version": result.stdout.splitlines()[0]}

    def check_python(self):
        return {"name": "python", "ok": True, "version": sys.version.split()[0]}

    def check_yt_dlp(self):
        return self._command_check("yt-dlp", ["--version"])

    def check_ffmpeg(self):
        return self._command_check("ffmpeg", ["-version"])

    def _directory_is_writable(self, path):
        if os.path.isdir(path):
            return os.access(path, os.W_OK)
        parent = os.path.dirname(path) or "."
        return os.path.isdir(parent) and os.access(parent, os.W_OK)

    def check_database(self):
        directory = os.path.dirname(self.database_path)
        exists = os.path.isfile(self.database_path)
        accessible = os.access(self.database_path, os.R_OK) if exists else True
        return {
            "name": "database",
            "ok": accessible and self._directory_is_writable(directory),
            "path": self.database_path,
            "exists": exists,
        }

    def check_directories(self):
        return {
            "name": "directories",
            "ok": self._directory_is_writable(self.data_directory),
            "path": self.data_directory,
            "exists": os.path.isdir(self.data_directory),
        }

    def run(self):
        checks = [
            self.check_python(),
            self.check_yt_dlp(),
            self.check_ffmpeg(),
            self.check_database(),
            self.check_directories(),
        ]
        return {"all_ok": all(check["ok"] for check in checks), "checks": checks}

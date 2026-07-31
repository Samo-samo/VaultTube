"""System dependency checks.

Verifies that required tools are available before downloads are started.
"""

import subprocess
import sys


class SystemChecks:
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

    def run(self):
        return {
            "checks": [
                self.check_python(),
                self.check_yt_dlp(),
                self.check_ffmpeg(),
            ]
        }

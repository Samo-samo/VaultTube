"""Download engine.

Coordinates media downloads. yt-dlp and FFmpeg are invoked through their
command-line interfaces via subprocess.
"""


class DownloadEngine:
    def get_media_info(self, url):
        raise NotImplementedError("Media info retrieval is not implemented.")

    def get_available_formats(self, url):
        raise NotImplementedError("Format discovery is not implemented.")

    def start_download(self, url, options):
        raise NotImplementedError("Download execution is not implemented.")

    def cancel_download(self, download_id):
        raise NotImplementedError("Download cancellation is not implemented.")

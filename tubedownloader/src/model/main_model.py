import yt_dlp

class YouTubeDownloader:
    def __init__(self, url, download_type="Video", resolution=None):
        self.url = url
        self.download_type = download_type
        self.resolution = resolution
        self.info = None

    def fetch_info(self):
        """Fetch video/audio info without downloading."""
        ydl_opts = {"quiet": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            self.info = ydl.extract_info(self.url, download=False)
        return self.info

    def get_formats(self):
        """Return available formats with resolution and file size."""
        if not self.info:
            self.fetch_info()

        formats = []
        if self.download_type == "Video":
            for f in self.info.get("formats", []):
                if f.get("vcodec") != "none" and f.get("acodec") == "none":
                    # Only video streams
                    resolution = f.get("format_note") or f.get("resolution") or "Unknown"
                    size = self._format_size(f.get("filesize"))
                    formats.append({
                        "id": f["format_id"],
                        "label": f"{resolution} - {size}",
                        "filesize": f.get("filesize", 0)
                    })
        else:  # MP3
            # Pick best audio
            best_audio = max(
                [f for f in self.info.get("formats", []) if f.get("acodec") != "none"],
                key=lambda x: x.get("abr", 0),
                default=None
            )
            if best_audio:
                size = self._format_size(best_audio.get("filesize"))
                formats.append({
                    "id": best_audio["format_id"],
                    "label": f"Best Audio - {size}",
                    "filesize": best_audio.get("filesize", 0)
                })
        return formats

    def download(self, format_id):
        """Download video or mp3 based on selection."""
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
        }

        if self.download_type == "Video":
            ydl_opts.update({
                "format": format_id + "+bestaudio/best",
                "merge_output_format": "mp4"
            })
        else:  # MP3
            ydl_opts.update({
                "format": format_id,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }]
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    @staticmethod
    def _format_size(size):
        if size is None:
            return "Unknown size"
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

from PySide6.QtCore import QThread, Signal, QObject
from src.model.main_model import YouTubeDownloader

class DownloadWorker(QObject):
    finished = Signal(str)

    def __init__(self, url, download_type, format_id):
        super().__init__()
        self.url = url
        self.download_type = download_type
        self.format_id = format_id

    def run(self):
        try:
            downloader = YouTubeDownloader(self.url, self.download_type)
            downloader.download(self.format_id)
            self.finished.emit("Download complete!")
        except Exception as e:
            self.finished.emit(f"Error: {str(e)}")

class MainController:
    def __init__(self, view):
        self.view = view
        self.formats = []

    def fetch_resolutions(self):
        url = self.view.lineEdit_url.text().strip()
        download_type = self.view.comboBox_downloadType.currentText()

        if not url:
            self.view.label_status.setText("Please enter a YouTube URL.")
            return

        try:
            downloader = YouTubeDownloader(url, download_type)
            self.formats = downloader.get_formats()

            self.view.comboBox_resolution.clear()
            for f in self.formats:
                self.view.comboBox_resolution.addItem(f["label"], f["id"])

            if not self.formats:
                self.view.label_status.setText("No formats found.")
            else:
                self.view.label_status.setText("Formats fetched successfully.")

        except Exception as e:
            self.view.label_status.setText(f"Error: {str(e)}")

    def start_download(self):
        url = self.view.lineEdit_url.text().strip()
        download_type = self.view.comboBox_downloadType.currentText()

        if not url:
            self.view.label_status.setText("Please enter a YouTube URL.")
            return

        if not self.formats:
            self.view.label_status.setText("Please fetch formats first.")
            return

        format_id = self.view.comboBox_resolution.currentData()
        if not format_id:
            self.view.label_status.setText("Please select a resolution/audio option.")
            return

        self.thread = QThread()
        self.worker = DownloadWorker(url, download_type, format_id)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.view.label_status.setText)

        self.thread.start()
        self.view.label_status.setText("Downloading...")

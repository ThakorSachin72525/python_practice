from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.view.ui.main_window_ui import Ui_MainWindow
from src.controller.main_controller import MainController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Controller instance
        self.controller = MainController(self)

        # Ensure download type combo has Video/MP3
        if self.comboBox_downloadType.count() == 0:
            self.comboBox_downloadType.addItems(["Video", "MP3"])

        # Connect buttons and signals
        self.pushButton_fetch.clicked.connect(self.controller.fetch_resolutions)
        self.pushButton_download.clicked.connect(self.controller.start_download)
        self.comboBox_downloadType.currentTextChanged.connect(self.on_download_type_changed)

        # Initial UI state
        self.label_status.setText("Status: Waiting...")
        self.on_download_type_changed(self.comboBox_downloadType.currentText())

    # Enable/disable resolution fetch depending on download type
    def on_download_type_changed(self, text):
        if text.lower() == "mp3":
            self.comboBox_resolution.setEnabled(False)
            self.pushButton_fetch.setEnabled(False)
        else:
            self.comboBox_resolution.setEnabled(True)
            self.pushButton_fetch.setEnabled(True)

    # Update resolutions comboBox from controller
    def update_resolutions(self, formats):
        self.comboBox_resolution.clear()
        for f in formats:
            # f is a dict: {'id': ..., 'label': ..., 'filesize': ...}
            self.comboBox_resolution.addItem(f["label"], f["id"])
        if formats:
            self.comboBox_resolution.setCurrentIndex(0)

    # Update status label
    def update_status(self, message):
        self.label_status.setText(message)

    # Show popup messages
    def show_message(self, message, title="YouTube Downloader"):
        QMessageBox.information(self, title, message)

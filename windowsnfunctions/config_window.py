import sys
import shutil
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QFileDialog, QApplication
from ui_files.configs import Ui_ApplicationSetup
from pathlib import Path

config_dir = Path.home() / ".safepaste"
config_file_loc = config_dir / "config.txt"

class ConfigWindow(QDialog, Ui_ApplicationSetup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()
        self.selected_file_path = ""

    def connect_signals(self):
        self.selectFileButton.clicked.connect(self.select_file)
        #self.buttonBox.accepted.connect(self.accept)


    def select_file(self):
        file_path, not_needed = QFileDialog.getOpenFileName(
            self,
            "Select Firebase Admin Credentials",
            "",
            "JSON Files (*.json)"
        )
        if file_path:
            self.selected_file_path = file_path
            self.selectedFileLabel.setText(file_path)

    def accept(self):
        database_url = self.lineEdit_url.text().strip()
        if not database_url:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid database URL !")
            return

        if not self.selected_file_path:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please select a valid Firebase Admin Credentials file.")
            return
        
        config_dir.mkdir(parents=True, exist_ok=True)

        with open(config_file_loc, "w") as config_file:
            config_file.write(f"{database_url}\n")
            config_file.write(f"{self.selected_file_path}\n")
        shutil.copy(self.selected_file_path, config_dir/"serviceAccountKey.json")
        #subprocess.run(["cp", self.selected_file_path, "serviceAccountKey.json"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        super().accept()      
        
#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = ConfigWindow()
    #window.show()
    #sys.exit(app.exec())
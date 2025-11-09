import sys
import os
from PyQt6.QtWidgets import QApplication,QDialog
from windowsnfunctions.config_window import ConfigWindow
from pathlib import Path

config_dir = Path.home() / ".safepaste"
config_file = config_dir / "config.txt"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(config_file.is_file() and os.path.isfile(config_dir/"serviceAccountKey.json")):
        window = ConfigWindow()
        result = window.exec()
        if result == QDialog.DialogCode.Rejected:
            sys.exit(0)
    from windowsnfunctions.app_window import MainWindow
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
import os
from PyQt6.QtWidgets import QApplication,QDialog
from windowsnfunctions.config_window import ConfigWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(os.path.isfile("config.txt") and os.path.isfile("serviceAccountKey.json")):
        window = ConfigWindow()
        result = window.exec()
        if result == QDialog.DialogCode.Rejected:
            sys.exit(0)
    from windowsnfunctions.app_window import MainWindow
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
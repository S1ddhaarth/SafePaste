import sys
import os
from PyQt6.QtWidgets import QApplication
from windowsnfunctions.config_window import ConfigWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if os.path.isfile("config.txt") and os.path.isfile("serviceAccountKey.json"):
        from windowsnfunctions.app_window import MainWindow
        window = MainWindow()
    else:
        window = ConfigWindow()
    window.show()
    sys.exit(app.exec())
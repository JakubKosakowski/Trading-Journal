from pathlib import Path
from src.main_window import MainWindow
from PyQt5.QtWidgets import *
import sys
from src.utils import Logger

def main():
    logger = Logger(__name__)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(Path("static/css/style.css").read_text())
    logger.logger.info('Style file loaded.')
    gui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

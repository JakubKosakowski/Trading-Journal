from pathlib import Path
from src.main_window import MainWindow
from PyQt5.QtWidgets import *
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = MainWindow()
    app.setStyleSheet(Path('static/css/style.css').read_text())
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
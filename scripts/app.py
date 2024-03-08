from src.main_window import MainWindow
from PyQt5.QtWidgets import *
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
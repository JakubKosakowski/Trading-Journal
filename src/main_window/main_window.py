from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trading Journal")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        btn = QPushButton('Click')
        grid = QGridLayout(self)
        grid.addWidget(btn, 0, 0, Qt.AlignHCenter)
        self.db = Database()
        print(self.db.cursor)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TransactionFormView(QWidget):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)
        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        
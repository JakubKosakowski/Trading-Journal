from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TransactionFormView(QWidget):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)
        self.setObjectName('transaction-form')
        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.load_reason_to_entry()

    def load_reason_to_entry(self):
        self.entry_reason_label = QLabel('', self)
        self.entry_reason_label.setFixedSize(780, 100)
        self.entry_reason_label.move(10, 10)
        
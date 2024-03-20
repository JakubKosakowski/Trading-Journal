from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TransactionFormView(QWidget):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)
        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.load_reason_to_entry()
        self.load_reason_to_entry_edit_lines()
        self.load_enter_and_exits_section()

    def load_reason_to_entry(self):
        self.entry_reason_label = QLabel('', self)
        self.entry_reason_label.setFixedSize(780, 100)
        self.entry_reason_label.move(10, 10)

    def load_reason_to_entry_edit_lines(self):
        self.entry_reason_textfield = QPlainTextEdit(self)
        self.entry_reason_textfield.setFixedSize(760, 30)
        self.entry_reason_textfield.move(20, 20)

    def load_enter_and_exits_section(self):
        self.enter_exit_label = QLabel('', self)
        self.enter_exit_label.setFixedSize(780, 200)
        self.enter_exit_label.move(10, 150)

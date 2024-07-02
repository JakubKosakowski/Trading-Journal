from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AddExitTacticPopupWindow(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add exit tactic')
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.exit_tactic_text = QLabel('Exit tactic', self)
        self.exit_tactic_text.move(10, 20)

        self.exit_tactic_value = QLineEdit(self)
        self.exit_tactic_value.resize(80, 20)
        self.exit_tactic_value.move(10, 40)

        self.submit = QPushButton('OK', self)
        self.submit.move(10, 80)
        self.submit.clicked.connect(self.send_values)

    def send_values(self):
        self.submitted.emit(self.exit_tactic_value.text())
        self.close()
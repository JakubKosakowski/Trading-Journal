from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AddExitTacticPopupWindow(QWidget):
    """A class used to show popup window for adding new exit tactic for transaction

    Arguments
    ---------
        QWidget (class): Class used to create widgets

    Attributes
    ----------
    submitted: pyqtSignal
        PyQt Emitter
    exit_tactic_text: QLabel
        Label with infomation
    exit_tactic_value(QLineEdit)
        QLineEdit field for exit tactic name

    Methods
    -------
    send_values()
        Emit values for method in other class
    """

    submitted = pyqtSignal(str)

    def __init__(self):
        """Initializes the instance of class"""

        super().__init__()
        # Set popup window parameters
        self.setWindowTitle('Add exit tactic')
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        # Set used attributes
        self.exit_tactic_text = QLabel('Exit tactic', self)
        self.exit_tactic_text.move(10, 20)

        self.exit_tactic_value = QLineEdit(self)
        self.exit_tactic_value.resize(80, 20)
        self.exit_tactic_value.move(10, 40)

        self.submit = QPushButton('OK', self)
        self.submit.move(10, 80)
        self.submit.clicked.connect(self.send_values)

    def send_values(self):
        """Emit exit tactic name for other method"""
        
        self.submitted.emit(self.exit_tactic_value.text())
        self.close()
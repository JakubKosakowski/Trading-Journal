from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TransactionFormView(QLayout):
    def __init__(self):
        super().__init__()
        self.glay = QGridLayout(self)
        self.label = QLabel(self)
        self.label.setText('New label')
        self.glay.addWidget(self.label, 0, 0, Qt.AlignHCenter)
        
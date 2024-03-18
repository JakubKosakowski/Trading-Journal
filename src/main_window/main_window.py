from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView

class MainWindow(QMainWindow):
    # def __init__(self, parent=None):
        # super(MainWindow, self).__init__(parent)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trading Journal")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.start_UI_Tool_Tab()

    def start_UI_Tool_Tab(self):
        pass
        
    # def set_transaction_layout(self):
    #     new_view = TransactionFormView()
    #     self.setLayout(new_view.glay)
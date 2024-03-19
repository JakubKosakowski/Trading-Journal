from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView

class MainWindowWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWindowWidget, self).__init__(parent)
        self.transaction_btn = QPushButton("Add transaction", self)
        self.transaction_btn.move(50, 140)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(800, 600)
        self.start_main_window_UI()

    def start_main_window_UI(self):
        self.main_tab = MainWindowWidget(self)
        self.setWindowTitle("Trading Journal")
        self.setCentralWidget(self.main_tab)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.show()

    def add_new_transaction_UI(self):
        self.transaction_tab = TransactionFormView(self)
        self.setWindowTitle("Add new transaction")
        self.setCentralWidget(self.transaction_tab)
        self.transaction_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
        
    # def set_transaction_layout(self):
    #     new_view = TransactionFormView()
    #     self.setLayout(new_view.glay)
        
# class UIToolTab(QWidget):
#     def __init__(self, parent=None):
#         super(UIToolTab, self).__init__(parent)
#         self.CPSBTN = QPushButton("text2", self)
#         self.CPSBTN.move(100, 350)

# class NextToolTab(QWidget):
#     def __init__(self, parent=None):
#         super(NextToolTab, self).__init__(parent)
#         self.CPSBTN = QPushButton("text4", self)
#         self.CPSBTN.move(150, 24)
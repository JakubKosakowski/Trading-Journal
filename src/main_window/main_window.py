from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView, AllTransactionsView
from src.utils import Logger

class MainWindowWidget(QWidget):
    def __init__(self, parent=None, logger=None):
        super(MainWindowWidget, self).__init__(parent)
        self.settings_btn = QPushButton("", self, objectName='settings-btn')
        self.settings_btn.move(750, 50)
        self.settings_btn.setIcon(QIcon('static/images/settings_icon.png'))
        logger.logger.info('Settings button generated.')
        self.transaction_btn = QPushButton("Add transaction", self, objectName='transaction-btn')
        self.transaction_btn.move(50, 140)
        logger.logger.info("Add transaction button generated")
        self.all_transactions_btn = QPushButton("Show all transactions", self, objectName='all-transactions-btn')
        self.all_transactions_btn.move(50, 200)
        logger.logger.info("Show all transactions button generated")
        self.showMaximized()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.logger = Logger(__name__)
        super(MainWindow, self).__init__(parent)
        self.logger.logger.info("Main window generated.")
        self.setGeometry(550, 250, 800, 600)
        self.start_main_window_UI()

    def start_main_window_UI(self):
        self.main_tab = MainWindowWidget(self, self.logger)
        self.logger.logger.info("Main window widget generated.")
        self.setWindowTitle("Trading Journal")
        self.setCentralWidget(self.main_tab)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.main_tab.all_transactions_btn.clicked.connect(self.show_all_transactions_UI)
        self.show()

    def add_new_transaction_UI(self):
        self.transaction_tab = TransactionFormView(self)
        self.logger.logger.info("Transaction form view generated.")
        self.setWindowTitle("Add new transaction")
        self.setCentralWidget(self.transaction_tab)
        self.transaction_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
        
    def show_all_transactions_UI(self):
        self.all_transactions_tab = AllTransactionsView(self)
        self.logger.logger.info("All transactions view generated.")
        self.setWindowTitle("All transactions")
        self.setCentralWidget(self.all_transactions_tab)
        self.all_transactions_tab.menu_btn.clicked.connect(self.start_main_window_UI)
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
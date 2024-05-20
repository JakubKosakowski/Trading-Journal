from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView, AllTransactionsView, SettingsView
from src.utils import Logger, Utils
from config.settings import load_toml_settings

class MainWindowWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWindowWidget, self).__init__(parent)
        self.parent_window = parent
        self.language = self.parent_window.toml_data['settings']['language']
        self.settings_btn = QPushButton("", self, objectName='settings-btn')
        self.settings_btn.move(750, 50)
        self.settings_btn.setIcon(QIcon('static/images/settings_icon.png'))
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.parent_window.logger.logger.info('Settings button generated.')

        self.transaction_btn = QPushButton("", self, objectName='transaction-btn')
        # self.set_language_text(self.transaction_btn, "Dodaj transakcję")
        self.transaction_btn.move(50, 140)
        self.parent_window.logger.logger.info("Add transaction button generated")

        self.all_transactions_btn = QPushButton("", self, objectName='all-transactions-btn')
        self.all_transactions_btn.move(50, 200)
        self.parent_window.logger.logger.info("Show all transactions button generated")
        
        self.exit_btn = QPushButton("", self, objectName='exit-btn')
        self.exit_btn.move(50, 260)
        self.version_label = QLabel(self.parent_window , objectName='version-label')
        self.version_label.setText(f"Version: {self.parent_window.toml_data['project']['version']}")
        self.version_label.move(700, 570)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.parent_window.logger.logger.info('Version label generated.')
        if self.parent_window.toml_data['settings']['fullscreen']:
            self.parent_window.showFullScreen()
        else:
            self.parent_window.setGeometry(550, 250, 800, 600)

        self.set_colors()
        self.load_text()

    def set_colors(self):
        self.set_transaction_btn_color()
        self.set_all_transactions_btn_color()
        self.set_exit_btn_color()
        self.parent_window.logger.logger.info("All window styles set.")

    def set_transaction_btn_color(self):
        self.transaction_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.parent_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        self.parent_window.logger.logger.info('Add transaction button color set.')
        
    def set_all_transactions_btn_color(self):
        self.all_transactions_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.parent_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        self.parent_window.logger.logger.info('All transactions button color set.')
        
    def set_exit_btn_color(self):
        self.exit_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.parent_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.parent_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        self.parent_window.logger.logger.info('Exit button color set.')

    def load_text(self):
        Utils.set_language_text(self.transaction_btn, "Dodaj transakcję", self.language, self.parent_window.toml_data)
        Utils.set_language_text(self.exit_btn, "Wyjdź", self.language, self.parent_window.toml_data)
        Utils.set_language_text(self.all_transactions_btn, "Pokaż wszystkie transakcje", self.language, self.parent_window.toml_data)
        self.parent_window.logger.logger.info('View text set.')



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.logger = Logger(__name__)
        self.toml_data = load_toml_settings()
        super(MainWindow, self).__init__(parent)
        self.logger.logger.info("Main window generated.")
        self.setGeometry(550, 250, 800, 600)
        self.start_main_window_UI()

    def start_main_window_UI(self):
        self.main_tab = MainWindowWidget(self)
        self.logger.logger.info("Main window widget generated.")
        self.setWindowTitle("Trading Journal")
        self.setCentralWidget(self.main_tab)
        self.main_tab.settings_btn.clicked.connect(self.settings_UI)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.main_tab.all_transactions_btn.clicked.connect(self.show_all_transactions_UI)
        self.main_tab.exit_btn.clicked.connect(self.close)
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

    def settings_UI(self):
        self.settings_tab = SettingsView(self)
        self.logger.logger.info('Settings view generated.')
        self.setWindowTitle("Settings")
        self.setCentralWidget(self.settings_tab)
        self.settings_tab.menu_btn.clicked.connect(self.start_main_window_UI)
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
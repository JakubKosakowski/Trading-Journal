from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView, AllTransactionsView, SettingsView, TestView
from src.utils import Logger, Utils
from config.settings import load_toml_settings
from src.setters import ButtonColorSetter, TextSetter, ProfitLossColorPicker, TextColorSetter
from src.abstract import ViewClass
from src.meta import MetaClass


class MainWindowWidget(QWidget, ViewClass, metaclass=MetaClass):
    def __init__(self, parent=None):
        super(MainWindowWidget, self).__init__(parent)
        self.parent_window = parent
        self.database = Database()
        self.language = self.parent_window.toml_data['settings']['language']
        self.currency = self.parent_window.toml_data['settings']['user_currency']
        self.settings_btn = QPushButton("", self, objectName='settings-btn')
        self.settings_btn.move(750, 50)
        self.settings_btn.setIcon(QIcon('static/images/settings_icon.png'))
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.parent_window.logger.logger.info('Settings button generated.')

        self.transaction_btn = QPushButton("", self, objectName='transaction-btn')
        self.transaction_btn.move(50, 140)
        self.parent_window.logger.logger.info("Add transaction button generated")

        self.all_transactions_btn = QPushButton("", self, objectName='all-transactions-btn')
        self.all_transactions_btn.move(50, 200)
        self.parent_window.logger.logger.info("Show all transactions button generated")
        
        self.exit_btn = QPushButton("", self, objectName='exit-btn')
        self.exit_btn.move(50, 320)
        self.parent_window.logger.logger.info("Exit button generated")

        self.test_btn = QPushButton("", self, objectName='test-btn')
        self.test_btn.move(50, 260)
        self.parent_window.logger.logger.info("Test view button generated")

        self.version_label = QLabel(self, objectName='version-label')
        self.version_label.setText(f"Version: {self.parent_window.toml_data['project']['version']}")
        self.version_label.move(700, 570)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.parent_window.logger.logger.info('Version label generated.')

        self.show_profit_loss_info()

        if self.parent_window.toml_data['settings']['fullscreen']:
            self.parent_window.showFullScreen()
        else:
            self.parent_window.setGeometry(550, 250, 800, 600)

        self.load_colors()
        self.load_text()

    def load_colors(self):
        button_color_setter = ButtonColorSetter(self.parent_window.toml_data['settings']['primary_color'])
        button_color_setter.set_color(self.transaction_btn)
        button_color_setter.set_color(self.all_transactions_btn)
        button_color_setter.set_color(self.exit_btn)
        button_color_setter.set_color(self.test_btn)
        self.parent_window.logger.logger.info("All window styles set.")

    def load_text(self):
        text_setter = TextSetter(self.language, self.parent_window.toml_data)
        text_setter.set_title(self.parent_window, 'Dziennik transakcji')
        text_setter.set_text(self.transaction_btn, "Dodaj transakcję")
        text_setter.set_text(self.exit_btn, "Wyjdź")
        text_setter.set_text(self.all_transactions_btn, "Wszystkie transakcje")
        text_setter.set_text(self.test_btn, "Test")
        text_setter.set_text(self.profit_loss_label, 'Z/S: ')
        self.parent_window.logger.logger.info('View text set.')

    def show_profit_loss_info(self):
        self.profit_loss_label = QLabel(self, objectName='profit-loss-label')
        self.profit_loss_label.move(50, 20)
        self.profit_loss_label.setStyleSheet(f"border-style: none;")
        self.parent_window.logger.logger.info('Profit/Loss label generated.')

        self.profit_loss_value = QLabel(self, objectName='profit-loss-label')
        self.profit_loss_value.move(80, 20)
        self.profit_loss_value.setText(f'{str(self.count_profit_loss_value())} {self.currency}')
        self.profit_loss_value.setStyleSheet(f"border-style: none;")

        self.picker = ProfitLossColorPicker()
        self.text_color_setter = TextColorSetter(['red', 'green'], self.picker)
        self.picker.check_profit(self.profit_loss_value.text())
        self.text_color_setter.set_color(self.profit_loss_value)

        self.parent_window.logger.logger.info('Profit/Loss value generated.')

    def count_profit_loss_value(self):
        values = self.database.select(columns='test_ident')
        return sum([x[0] for x in values])


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.logger = Logger(__name__)
        self.toml_data = load_toml_settings()
        self.language = self.toml_data['settings']['language']
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon('static/images/favicon.jpg'))
        self.logger.logger.info("Main window generated.")
        self.setGeometry(550, 250, 800, 600)
        self.start_main_window_UI()

    def start_main_window_UI(self):
        self.main_tab = MainWindowWidget(self)
        self.logger.logger.info("Main window widget generated.")
        self.setCentralWidget(self.main_tab)
        self.main_tab.settings_btn.clicked.connect(self.settings_UI)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.main_tab.all_transactions_btn.clicked.connect(self.show_all_transactions_UI)
        self.main_tab.test_btn.clicked.connect(self.test_view_UI)
        self.main_tab.exit_btn.clicked.connect(self.close)
        self.show()

    def add_new_transaction_UI(self):
        self.transaction_tab = TransactionFormView(self)
        self.logger.logger.info("Transaction form view generated.")
        self.setCentralWidget(self.transaction_tab)
        self.transaction_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
        
    def show_all_transactions_UI(self):
        self.all_transactions_tab = AllTransactionsView(self)
        self.logger.logger.info("All transactions view generated.")
        self.setCentralWidget(self.all_transactions_tab)
        self.all_transactions_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()

    def settings_UI(self):
        self.settings_tab = SettingsView(self)
        self.logger.logger.info('Settings view generated.')
        self.setCentralWidget(self.settings_tab)
        self.settings_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()

    def test_view_UI(self):
        self.test_tab = TestView(self)
        self.setCentralWidget(self.test_tab)
        self.test_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
        
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
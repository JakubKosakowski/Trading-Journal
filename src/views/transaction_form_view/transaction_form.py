from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger

class TransactionFormView(QWidget):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)
        self.main_window = parent
        self.logger = Logger(__name__)
        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 370)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')
        self.load_reason_to_entry()
        self.load_reason_to_entry_edit_lines()
        self.load_enter_and_exits_section()
        self.load_fields_labels()
        self.load_colors()

    def load_reason_to_entry(self):
        self.entry_reason_label = QLabel('', self)
        self.entry_reason_label.setFixedSize(780, 100)
        self.entry_reason_label.move(10, 10)
        self.logger.logger.info("Reason to entry section generated.")

    def load_reason_to_entry_edit_lines(self):
        self.entry_reason_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.entry_reason_textfield.setFixedSize(760, 30)
        self.entry_reason_textfield.move(20, 20)
        self.logger.logger.info("Reason to entry(edit line) section generated.")

    def load_enter_and_exits_section(self):
        self.enter_exit_label = QLabel('', self)
        self.enter_exit_label.setFixedSize(780, 220)
        self.enter_exit_label.move(10, 150)
        self.logger.logger.info("Enter and exits section generated.")

    def load_fields_labels(self):
        self.fields_labels = QLabel("        Date\t\tOrder Price           Filled Priced           Slippage           Filled Shares           Total Cost           Day's High           Day's Low           Grade        ", self)
        self.fields_labels.setObjectName('transaction-data-info')
        self.fields_labels.setFixedSize(760, 30)
        self.fields_labels.move(20, 300)
        self.logger.logger.info("Fields labels section generated.")
        self.load_input_lines()

    def load_reason_for_exit_section(self):
        pass

    def load_colors(self):
        self.load_menu_button_color()

    def load_menu_button_color(self):
        self.menu_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.main_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        
    def load_input_lines(self):
        self.load_company_code()
        self.load_transaction_date_picker()
        self.load_transaction_order_price()

    def load_transaction_date_picker(self):
        self.transaction_date = QDateEdit(self, calendarPopup=True)
        self.transaction_date.move(20, 320)
        self.transaction_date.setDateTime(QDateTime.currentDateTime())
        self.transaction_date.setStyleSheet(f"margin-top: 10px;")
        self.logger.logger.info("Transaction date picker generated.")

    def load_company_code(self):
        self.load_company_code_label()
        self.company_code = QLineEdit(self)
        self.company_code.setFixedSize(40, 20)
        self.company_code.move(100, 60)
        self.company_code.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Company code line edit generated.")

    def load_company_code_label(self):
        self.company_code_label = QLabel('Company code', self)
        self.company_code_label.setFixedSize(80, 20)
        self.company_code_label.move(20, 60)
        self.company_code_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Company code info label generated.")

    def load_transaction_order_price(self):
        self.transaction_order_price = QLineEdit(self)
        self.transaction_order_price.setValidator(QDoubleValidator(0.001,99999.999,3))
        self.transaction_order_price.setFixedSize(50, 20)
        self.transaction_order_price.move(120, 330)
        self.transaction_order_price.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Order price line edit generated.")

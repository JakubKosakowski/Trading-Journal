from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.setters import ButtonColorSetter, TextSetter, TextColorSetter, ButtonTextColorPicker
from src.abstract import FormClass
from src.meta import MetaFormClass
from src.popup_window import AddExitTacticPopupWindow
from src.postgres_database import Database


class TransactionFormView(QWidget, FormClass, metaclass=MetaFormClass):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)
        self.main_window = parent
        self.language = self.main_window.toml_data['settings']['language']
        self.logger = Logger(__name__)
        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 750)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.add_transaction_btn = QPushButton("Add", self)
        self.add_transaction_btn.move(250, 750)
        self.add_transaction_btn.setObjectName('add-transaction-btn')
        self.add_transaction_btn.clicked.connect(self.add_record)

        self.database = Database()

        self.load_reason_to_entry()
        self.load_reason_to_entry_edit_lines()
        self.load_enter_and_exits_section()
        self.load_reason_for_exit_section()
        self.load_exit_tactic_section()
        self.load_fields_labels()
        self.load_post_trade_analysis_section()
        self.load_colors()

        self.load_text()

    def load_reason_to_entry(self):
        self.entry_reason_label = QLabel('', self, objectName="section-label")
        self.entry_reason_label.setFixedSize(780, 100)
        self.entry_reason_label.move(10, 30)

        self.entry_reason_info = QLabel('Reason for Entry', self, objectName="reason-text")
        self.entry_reason_info.move(10, 10)

        self.logger.logger.info("Reason to entry section generated.")

    def load_reason_to_entry_edit_lines(self):
        self.entry_reason_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.entry_reason_textfield.setFixedSize(760, 30)
        self.entry_reason_textfield.move(20, 50)
        self.logger.logger.info("Reason to entry(edit line) section generated.")

    def load_enter_and_exits_section(self):
        self.enter_exit_label = QLabel('', self, objectName="section-label")
        self.enter_exit_label.setFixedSize(780, 200)
        self.enter_exit_label.move(10, 160)

        self.enter_exit_info = QLabel('Entries & Exits', self, objectName="reason-text")
        self.enter_exit_info.move(10, 140)

        self.logger.logger.info("Enter and exits section generated.")

    def load_fields_labels(self):
        self.fields_labels = QLabel("        Date\t\tOrder Price           Filled Priced           Slippage           Filled Shares           Total Cost           Day's High           Day's Low           Grade        ",
                                    self, objectName="section-label")
        self.fields_labels.setObjectName('transaction-data-info')
        self.fields_labels.setFixedSize(760, 30)
        self.fields_labels.move(20, 300)
        self.logger.logger.info("Fields labels section generated.")
        self.load_input_lines()

    def load_reason_for_exit_section(self):
        self.reason_for_exit_section = QLabel('', self, objectName="section-label")
        self.reason_for_exit_section.setFixedSize(380 ,200)
        self.reason_for_exit_section.move(10, 400)

        self.reason_for_exit_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.reason_for_exit_textfield.setFixedSize(360, 30)
        self.reason_for_exit_textfield.move(20, 410)
        
        self.reason_for_exit_info = QLabel('Reason for Exit', self, objectName="reason-text")
        self.reason_for_exit_info.move(10, 380)

        self.logger.logger.info("Reason for exit section generated.")

    def load_exit_tactic_section(self):
        self.exit_tactic_label = QLabel('Exit Tactic', self, objectName="text-label")
        self.exit_tactic_label.move(440, 380)

        self.exit_tactic_section = QLabel('', self, objectName="section-label")
        self.exit_tactic_section.setFixedSize(350 ,100)
        self.exit_tactic_section.move(440, 400)

        self.exit_tactic_cb = QComboBox(self)
        self.exit_tactic_cb.setFixedSize(300, 30)
        self.exit_tactic_cb.move(450, 410)

        self.load_exit_tactics_cb_items()

        self.add_exit_tactic_btn = QPushButton("", self, objectName='add-exit-tactic-btn')
        self.add_exit_tactic_btn.move(760, 415)
        self.add_exit_tactic_btn.setIcon(QIcon('static/images/plus.png'))
        self.add_exit_tactic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_exit_tactic_btn.clicked.connect(self.add_exit_tactic)
        self.logger.logger.info("Exit tactic section generated.")

    def load_colors(self):
        self.load_menu_button_color()

    def load_menu_button_color(self):
        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)
        button_text_color_picker.check_pick_condiditon(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'], text_color_setter)
        button_color_setter.set_color(self.menu_btn)
        button_color_setter.set_color(self.add_transaction_btn)
        
    def load_input_lines(self):
        self.load_company_code()
        self.load_transaction_date_picker()
        self.load_transaction_order_price()
        self.load_transaction_filled_priced()
        self.load_transaction_slippage()

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
        self.company_code.move(100, 100)
        self.company_code.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Company code line edit generated.")

    def load_company_code_label(self):
        self.company_code_label = QLabel('', self)
        self.company_code_label.setFixedSize(80, 20)
        self.company_code_label.move(20, 100)
        self.company_code_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Company code info label generated.")

    def load_transaction_order_price(self):
        self.transaction_order_price = QLineEdit(self)
        self.transaction_order_price.setValidator(QDoubleValidator(0.001,99999.999,3))
        self.transaction_order_price.setFixedSize(50, 20)
        self.transaction_order_price.move(122, 330)
        self.transaction_order_price.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Order price line edit generated.")

    def load_transaction_filled_priced(self):
        self.transaction_filled_priced = QLineEdit(self)
        self.transaction_filled_priced.setValidator(QDoubleValidator(0.001,99999.999,3))
        self.transaction_filled_priced.setFixedSize(50, 20)
        self.transaction_filled_priced.move(210, 330)
        self.transaction_filled_priced.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Filled priced line edit generated.")

    def load_transaction_slippage(self):
        self.transaction_slippage = QLineEdit(self)
        self.transaction_slippage.setReadOnly(True)
        self.transaction_slippage.setValidator(QDoubleValidator(0.001,99999.999,3))
        self.transaction_slippage.setText('0.000')
        self.transaction_slippage.setFixedSize(50, 20)
        self.transaction_slippage.move(290, 330)
        self.transaction_slippage.setStyleSheet(f"background-color: gray;")
        self.logger.logger.info("Slippage line edit generated.")

    def load_post_trade_analysis_section(self):
        self.post_trade_analysis_section = QLabel('', self, objectName="section-label")
        self.post_trade_analysis_section.setFixedSize(780, 100)
        self.post_trade_analysis_section.move(10, 630)

        self.post_trade_analysis_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.post_trade_analysis_textfield.setFixedSize(760, 50)
        self.post_trade_analysis_textfield.move(20, 640)

        self.post_trade_analysis_info = QLabel('Post Trade Analysis', self, objectName="reason-text")
        self.post_trade_analysis_info.move(10, 610)

    def load_text(self):
        text_setter = TextSetter(self.language)
        text_setter.set_title(self.main_window, 'Dodaj transakcję')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        text_setter.set_text(self.company_code_label, "Kod spółki")

    def load_exit_tactics_cb_items(self):
        exit_tactics_list = self.database.select('exit_tactics')
        for exit_tactic in exit_tactics_list:
            self.exit_tactic_cb.addItem(f'{exit_tactic[0]} {exit_tactic[1]}')

    @pyqtSlot(str)
    def update_exit_tactic(self, exit_tactic):
        self.database.insert([exit_tactic], "exit_tactics")
        self.exit_tactic_cb.clear()
        self.load_exit_tactics_cb_items()

    def add_exit_tactic(self):
        self.ui = AddExitTacticPopupWindow()
        self.ui.submitted.connect(self.update_exit_tactic)
        self.ui.show()

    def add_record(self):
        pass

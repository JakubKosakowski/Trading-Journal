from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.setters import ButtonColorSetter, TextSetter, TextColorSetter, ButtonTextColorPicker
from src.abstract import FormClass
from src.meta import MetaFormClass
from src.popup_window import AddExitTacticPopupWindow
from src.postgres_database import Database
from src.generators import QLineEditGenerator, QPushButtonGenerator


class TransactionFormView(QWidget, FormClass, metaclass=MetaFormClass):
    def __init__(self, parent=None):
        super(TransactionFormView, self).__init__(parent)


        self.main_window = parent
        self.language = self.main_window.toml_data['settings']['language']
        self.logger = Logger(__name__)
        self.qline_edit_generator = QLineEditGenerator(self, 0.000)

        self.text_setter = TextSetter(self.language)
        self.qpush_button_generator = QPushButtonGenerator(self, self.main_window.toml_data['settings']['primary_color'], self.text_setter)

        self.database = Database()

        self.load_buttons()
        self.load_reason_to_entry()
        self.load_reason_to_entry_edit_lines()
        self.load_enter_and_exits_section()
        self.load_reason_for_exit_section()
        self.load_exit_tactic_section()
        self.load_fields_labels()
        self.load_post_trade_analysis_section()

        self.load_type_of_transaction_combobox()

        self.load_text()

    def load_buttons(self):
        self.menu_btn = self.qpush_button_generator.generate_element('menu-btn', 'Wróć do menu', 100, 750)
        self.add_transaction_btn = self.qpush_button_generator.generate_element('add-btn', 'Dodaj transakcję', 250, 750)
        self.add_transaction_btn.clicked.connect(self.add_record)
        self.main_window.logger.logger.info('Buttons loaded.')

    def load_reason_to_entry(self):
        """Load reason for entry section"""

        # Create reason to entry section label with border
        self.entry_reason_label = QLabel('', self, objectName="section-label")
        self.entry_reason_label.setFixedSize(780, 100)
        self.entry_reason_label.move(10, 30)

        # Create entry reason info label
        self.entry_reason_info = QLabel('Reason for Entry', self, objectName="reason-text")
        self.entry_reason_info.move(10, 10)

        self.logger.logger.info("Reason to entry section generated.")

    def load_reason_to_entry_edit_lines(self):
        """Load edit line for reason to entry"""

        self.entry_reason_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.entry_reason_textfield.setFixedSize(760, 30)
        self.entry_reason_textfield.move(20, 50)
        self.logger.logger.info("Reason to entry(edit line) section generated.")

    def load_enter_and_exits_section(self):
        """Load entry and exits section"""

        # Create Entries and exits section with border
        self.enter_exit_label = QLabel('', self, objectName="section-label")
        self.enter_exit_label.setFixedSize(780, 200)
        self.enter_exit_label.move(10, 160)

        # Create Entries and Exits info
        self.enter_exit_info = QLabel('Entries & Exits', self, objectName="reason-text")
        self.enter_exit_info.move(10, 140)

        self.logger.logger.info("Enter and exits section generated.")

    def load_fields_labels(self):
        """Load section with input field info's"""

        self.fields_labels = QLabel("        Date\t\tOrder Price           Filled Priced           Slippage           Filled Shares           Total Cost           Day's High           Day's Low           Grade        ",
                                    self, objectName="section-label")
        self.fields_labels.setObjectName('transaction-data-info')
        self.fields_labels.setFixedSize(760, 30)
        self.fields_labels.move(20, 300)
        self.logger.logger.info("Fields labels section generated.")

        # Generate input fields
        self.load_input_lines()

    def load_reason_for_exit_section(self):
        """Load reason for exit section"""

        # Create reason for exit section with border
        self.reason_for_exit_section = QLabel('', self, objectName="section-label")
        self.reason_for_exit_section.setFixedSize(380 ,200)
        self.reason_for_exit_section.move(10, 400)

        # Create reason for exit textfield
        self.reason_for_exit_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.reason_for_exit_textfield.setFixedSize(360, 30)
        self.reason_for_exit_textfield.move(20, 410)
        
        # Create reason for exit info
        self.reason_for_exit_info = QLabel('Reason for Exit', self, objectName="reason-text")
        self.reason_for_exit_info.move(10, 380)

        self.logger.logger.info("Reason for exit section generated.")

    def load_exit_tactic_section(self):
        """Load exit tactic section with ComboBox and plus button for adding new exit tactic"""

        # Create info label
        self.exit_tactic_label = QLabel('Exit Tactic', self, objectName="text-label")
        self.exit_tactic_label.move(440, 380)

        # Create section label
        self.exit_tactic_section = QLabel('', self, objectName="section-label")
        self.exit_tactic_section.setFixedSize(350 ,100)
        self.exit_tactic_section.move(440, 400)

        # Create ComboBox
        self.exit_tactic_cb = QComboBox(self)
        self.exit_tactic_cb.setFixedSize(300, 30)
        self.exit_tactic_cb.move(450, 410)

        # Load exit tactics from database
        self.load_exit_tactics_cb_items()

        # Create button and connect them into method
        self.add_exit_tactic_btn = QPushButton("", self, objectName='add-exit-tactic-btn')
        self.add_exit_tactic_btn.move(760, 415)
        self.add_exit_tactic_btn.setIcon(QIcon('static/images/plus.png'))
        self.add_exit_tactic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_exit_tactic_btn.clicked.connect(self.add_exit_tactic)
        self.logger.logger.info("Exit tactic section generated.")
        
    def load_input_lines(self):
        """Load all input lines in transaction form view"""
        
        self.load_company_code()
        self.load_transaction_date_picker()
        self.load_transaction_order_price()
        self.load_transaction_filled_priced()
        self.load_transaction_slippage()
        self.load_transaction_filled_shares()
        self.load_transaction_total_cost()
        self.load_transaction_days_high()
        self.load_transaction_days_low()

    def load_transaction_date_picker(self):
        """Load data field in form"""

        self.transaction_date = QDateEdit(self, calendarPopup=True)
        self.transaction_date.move(20, 320)
        self.transaction_date.setDateTime(QDateTime.currentDateTime())
        self.transaction_date.setStyleSheet(f"margin-top: 10px;")
        self.logger.logger.info("Transaction date picker generated.")

    def load_company_code(self):
        """Load company code section"""

        # Create company code info label
        self.load_company_code_label()

        # Create company code edit line
        self.company_code = self.qline_edit_generator.generate_element(100, 100)
        # self.company_code.move()
        self.logger.logger.info("Company code line edit generated.")

    def load_type_of_transaction_combobox(self):

        self.load_type_of_transaction_label()

        self.transaction_type_cb = QComboBox(self)
        self.transaction_type_cb.setFixedSize(100, 20)
        self.transaction_type_cb.move(300, 100)

    def load_company_code_label(self):
        """Load company code info label"""
        self.company_code_label = QLabel('', self)
        self.company_code_label.setFixedSize(80, 20)
        self.company_code_label.move(20, 100)
        self.company_code_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Company code info label generated.")

    def load_type_of_transaction_label(self):
        """Load type of transaction info label"""
        
        self.transaction_type_label = QLabel('', self)
        self.transaction_type_label.setFixedSize(100, 20)
        self.transaction_type_label.move(200, 100)
        self.transaction_type_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Type of Transaction info label generated.")

    def load_transaction_order_price(self):
        """Load transaction order price input section"""
        
        self.transaction_order_price = self.qline_edit_generator.generate_element(122, 330)
        self.logger.logger.info("Order price line edit generated.")

    def load_transaction_filled_priced(self):
        """Load transaction filled price input section"""
        
        self.transaction_filled_priced = self.qline_edit_generator.generate_element(210, 330)
        self.logger.logger.info("Filled priced line edit generated.")

    def load_transaction_slippage(self):
        """Load transaction slippage input section"""
        
        self.transaction_slippage = self.qline_edit_generator.generate_element(290, 330, readonly=True)
        self.logger.logger.info("Slippage line edit generated.")

    def load_transaction_filled_shares(self):
        """Load transaction filled shares input section"""

        self.transaction_filled_shares = self.qline_edit_generator.generate_element(370, 330)
        self.logger.logger.info("Filled share line edit generated.")

    def load_transaction_total_cost(self):
        """Load transaction total cost input section"""

        self.transaction_total_cost = self.qline_edit_generator.generate_element(460, 330, readonly=True)
        self.logger.logger.info("Total cost line edit generated.")

    def load_transaction_days_high(self):
        """Load transaction days high input section"""

        self.transaction_days_high = self.qline_edit_generator.generate_element(545, 330)
        self.logger.logger.info("Day's high line edit generated.")

    def load_transaction_days_low(self):
        """Load transaction days low input section"""
        
        self.transaction_days_low = self.qline_edit_generator.generate_element(630, 330)
        self.logger.logger.info("Day's low line edit generated.")

    def load_post_trade_analysis_section(self):
        """load post trade analysis section"""

        # Create section label
        self.post_trade_analysis_section = QLabel('', self, objectName="section-label")
        self.post_trade_analysis_section.setFixedSize(780, 100)
        self.post_trade_analysis_section.move(10, 630)

        # Create input textfield 
        self.post_trade_analysis_textfield = QPlainTextEdit(self, objectName='reason-text')
        self.post_trade_analysis_textfield.setFixedSize(760, 50)
        self.post_trade_analysis_textfield.move(20, 640)

        # Create info label
        self.post_trade_analysis_info = QLabel('Post Trade Analysis', self, objectName="reason-text")
        self.post_trade_analysis_info.move(10, 610)
        self.logger.logger.info("Post Trade Analysis section generated.")

    def load_text(self):
        """Load text in choosed language for all elements in view"""
        
        text_setter = TextSetter(self.language)
        text_setter.set_title(self.main_window, 'Dodaj transakcję')
        text_setter.set_text(self.entry_reason_info, 'Powód wejścia')
        text_setter.set_text(self.enter_exit_info, 'Wejścia i Wyjścia')
        text_setter.set_text(self.company_code_label, "Kod spółki")
        text_setter.set_text(self.transaction_type_label, "Rodzaj transakcji")
        text_setter.set_text(self.reason_for_exit_info, 'Powód wyjścia')
        text_setter.set_text(self.exit_tactic_label, 'Taktyka wyjścia')
        text_setter.set_text(self.post_trade_analysis_info, 'Analiza potransakcyjna')

    def load_exit_tactics_cb_items(self):
        """Load exit tactic combobox items"""
        
        exit_tactics_list = self.database.select('exit_tactics')
        for exit_tactic in exit_tactics_list:
            self.exit_tactic_cb.addItem(f'{exit_tactic[0]} {exit_tactic[1]}')

    @pyqtSlot(str)
    def update_exit_tactic(self, exit_tactic: str):
        """Add new created exit tactic into database

        Arguments
        ---------
            exit_tactic (str): Exit tactic description
        """

        # Insert exit tactic into database table
        self.database.insert([exit_tactic], "exit_tactics")

        # Clear whole exit tactic combobox
        self.exit_tactic_cb.clear()

        # Load exit tactics again
        self.load_exit_tactics_cb_items()

    def add_exit_tactic(self):
        """Show popup window for adding new exit tactic"""

        self.ui = AddExitTacticPopupWindow()
        self.ui.submitted.connect(self.update_exit_tactic)
        self.ui.show()

    def add_record(self):
        pass

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
        self.menu_btn.move(100, 350)
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
        self.enter_exit_label.setFixedSize(780, 200)
        self.enter_exit_label.move(10, 150)
        self.logger.logger.info("Enter and exits section generated.")

    def load_fields_labels(self):
        self.fields_labels = QLabel("        Date\t\tOrder Price           Filled Priced           Slippage           Filled Shares           Total Cost           Day's High           Day's Low           Grade        ", self)
        self.fields_labels.setFixedSize(760, 30)
        self.fields_labels.move(20, 300)
        self.logger.logger.info("Fields labels section generated.")

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
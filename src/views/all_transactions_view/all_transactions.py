from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.postgres_database import Database

class AllTransactionsView(QWidget):
    def __init__(self, parent=None):
        super(AllTransactionsView, self).__init__(parent)
        self.main_window = parent
        self.logger = Logger(__name__)
        self.database = Database()
        self.logger.logger.info("Database loaded.")
        self.menu_btn = QPushButton("Go back to menu", self)
        self.logger.logger.info('Go back to menu button generated.')
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')

        self.create_table()
        self.logger.logger.info('Table widget generated.')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.menu_btn)
        self.setLayout(self.layout)
        self.logger.logger.info("Table layout set up.")

        self.load_colors()

    def create_table(self):
        self.table_widget = QTableWidget()
        self.table_widget.setShowGrid(False)
        self.records = self.database.select()
        self.table_widget.setRowCount(len(self.records))
        self.table_widget.setColumnCount(2)

        self.table_widget.setHorizontalHeaderLabels(["name", "age"])
        for ind, record in enumerate(self.records):
            self.table_widget.setItem(ind,0, QTableWidgetItem(record[1]))
            self.table_widget.setItem(ind,1, QTableWidgetItem(str(record[2])))
            self.logger.logger.debug(f"Record nr. {ind}: {record}")

    def load_colors(self):
        self.load_menu_button_color()
        self.load_background_color()

    def load_menu_button_color(self):
        self.menu_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.main_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        
    def load_background_color(self):
        self.table_widget.setStyleSheet("QTableWidget {"
                                        f"background-color: {self.main_window.toml_data['settings']['secondary_color']};"
                                        "}"
                                        "QHeaderView {"
                                        f"background-color: {self.main_window.toml_data['settings']['secondary_color']};"
                                        "}")
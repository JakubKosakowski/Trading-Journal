from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger, Utils
from src.postgres_database import Database
from src.setters import ButtonColorSetter, TextSetter, BackgroundColorSetter

class AllTransactionsView(QWidget):
    def __init__(self, parent=None):
        super(AllTransactionsView, self).__init__(parent)
        self.main_window = parent
        self.language = self.main_window.toml_data['settings']['language']

        self.logger = Logger(__name__)
        self.database = Database()
        self.logger.logger.info("Database loaded.")
        self.menu_btn = QPushButton("", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.create_table()
        self.logger.logger.info('Table widget generated.')

        columns = ["", "name", "age"]
        self.sort_cb = QComboBox(self)
        self.sort_cb.addItems(columns)
        self.sort_cb.move(100, 200)
        self.sort_cb.setCurrentIndex(0)
        self.sort_cb.currentIndexChanged.connect(self.sort_records)
        self.logger.logger.info('Sort column ComboBox generated.')

        order_method = ['ASC', 'DESC']
        self.order_method_cb = QComboBox(self)
        self.order_method_cb.addItems(order_method)
        self.order_method_cb.move(100, 200)
        self.order_method_cb.setCurrentIndex(0)
        self.order_method_cb.currentIndexChanged.connect(self.sort_records)
        self.logger.logger.info('Order method ComboBox generated.')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sort_cb)
        self.layout.addWidget(self.order_method_cb)
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.menu_btn)
        self.setLayout(self.layout)
        self.logger.logger.info("Table layout set up.")

        self.load_colors()

        self.load_text()

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

    def sort_records(self):
        if self.sort_cb.currentText() != "":
            self.records = self.database.select(order_by=f'{self.sort_cb.currentText()}')
            self.logger.logger.debug(self.records)
            for ind, record in enumerate(self.records):
                self.table_widget.setItem(ind,0, QTableWidgetItem(record[1]))
                self.table_widget.setItem(ind,1, QTableWidgetItem(str(record[2])))

    def load_colors(self):
        self.load_menu_button_color()
        self.load_background_color()
        self.logger.logger.info("All view colors loaded.")

    def load_menu_button_color(self):
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter.set_color(self.menu_btn)
        self.logger.logger.info('Menu button color set.')
        
    def load_background_color(self):
        background_color_setter = BackgroundColorSetter(self.main_window.toml_data['settings']['secondary_color'])
        background_color_setter.set_color(self.table_widget)
        self.logger.logger.info('Table background color set.')

    def load_text(self):
        text_setter = TextSetter(self.language, self.main_window.toml_data)
        text_setter.set_title(self.main_window, 'Wszystkie transakcje')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        self.logger.logger.info('View text set.')
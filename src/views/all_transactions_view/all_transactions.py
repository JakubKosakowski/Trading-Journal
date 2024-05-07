from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger

class AllTransactionsView(QWidget):
    def __init__(self, parent=None):
        super(AllTransactionsView, self).__init__(parent)
        self.logger = Logger(__name__)
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

    def create_table(self):
       self.table_widget = QTableWidget()
       self.table_widget.setRowCount(2)
       self.table_widget.setColumnCount(1)

       self.table_widget.setItem(0,0, QTableWidgetItem("Name"))
       self.table_widget.setItem(1,0, QTableWidgetItem("Jakub")) 
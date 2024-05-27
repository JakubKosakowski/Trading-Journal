from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.abstract import ViewClass


class TestView(QWidget):
    def __init__(self, parent=None):
        super(TestView, self).__init__(parent)

        self.main_window = parent

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')
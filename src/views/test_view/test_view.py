from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.abstract import ViewClass
from src.setters import TextSetter, ButtonColorSetter


class TestViewMeta(type(QWidget), type(ViewClass)):
    pass


class ViewClass(QWidget):
    pass


class TestView(ViewClass):
    def __init__(self, parent=None):
        __metaclass__ = TestViewMeta
        super(TestView, self).__init__(parent)

        self.main_window = parent

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.load_colors()

    def load_colors(self):
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter.set_color(self.menu_btn)
        self.logger.logger.info('Go back to menu button generated.')
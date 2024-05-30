from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.abstract import ViewClass
from src.setters import TextSetter, ButtonColorSetter
from src.meta import MetaClass

class TestView(QWidget, ViewClass, metaclass=MetaClass):
    def __init__(self, parent=None):
        super(TestView, self).__init__(parent)

        self.main_window = parent

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.load_colors()
        self.load_text()

        self.show_edit_fields()

    def load_colors(self):
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter.set_color(self.menu_btn)
        self.logger.logger.info('Go back to menu button generated.')

    def load_text(self):
        self.language = self.main_window.toml_data['settings']['language']
        text_setter = TextSetter(self.language, self.main_window.toml_data)
        text_setter.set_title(self.main_window, 'Test')
        text_setter.set_text(self.menu_btn, "Wróć do menu")

    def show_edit_fields(self):
        self.show_name_field()

    def show_name_field(self):
        self.name_label = QLineEdit(self)
        self.name_label.setFixedSize(100, 20)
        self.name_label.move(100, 60)
        self.name_label.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Name line edit generated.")

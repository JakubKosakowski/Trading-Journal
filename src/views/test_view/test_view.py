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

        self.show_edit_fields()

        self.load_colors()
        self.load_text()

    def load_colors(self):
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter.set_color(self.menu_btn)
        self.logger.logger.info('Go back to menu button generated.')

    def load_text(self):
        self.language = self.main_window.toml_data['settings']['language']
        text_setter = TextSetter(self.language, self.main_window.toml_data)
        text_setter.set_title(self.main_window, 'Test')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        text_setter.set_text(self.age_label, 'Wiek')
        text_setter.set_text(self.name_label, 'Imię')

    def show_edit_fields(self):
        self.show_name_field()
        self.show_age_field()

    def show_name_field(self):
        self.load_name_field_label()
        self.name = QLineEdit(self)
        self.name.setFixedSize(100, 20)
        self.name.move(100, 60)
        self.name.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Name line edit generated.")

    def show_age_field(self):
        self.load_age_field_label()
        self.age = QLineEdit(self)
        self.age.setFixedSize(100, 20)
        self.age.setValidator(QIntValidator(18,200))
        self.age.move(100, 120)
        self.age.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Age edit generated.")

    def load_age_field_label(self):
        self.age_label = QLabel('', self)
        self.age_label.setFixedSize(50, 20)
        self.age_label.move(100, 100)
        # self.age_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Age info label generated.")

    def load_name_field_label(self):
        self.name_label = QLabel('', self)
        self.name_label.setFixedSize(50, 20)
        self.name_label.move(100, 40)
        # self.age_label.setStyleSheet(f"border-style: none;")
        self.logger.logger.info("Name info label generated.")
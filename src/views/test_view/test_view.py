from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.abstract import FormClass
from src.setters import TextSetter, ButtonColorSetter, TextColorSetter, ButtonTextColorPicker
from src.meta import MetaFormClass
from src.postgres_database import Database

class TestView(QWidget, FormClass, metaclass=MetaFormClass):
    def __init__(self, parent=None):
        super(TestView, self).__init__(parent)

        self.main_window = parent
        self.db = Database()

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.add_test_btn = QPushButton('', self)
        self.add_test_btn.move(100, 170)
        self.add_test_btn.setObjectName('add-btn')
        self.add_test_btn.clicked.connect(self.add_record)
        self.logger.logger.info('Add button generated.')

        self.show_edit_fields()

        self.load_colors()
        self.load_text()

    def load_colors(self):
        """Load color for all buttons in view"""

        # Create and set button_text_color_picker
        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)
        button_text_color_picker.check_pick_condiditon(self.main_window.toml_data['settings']['primary_color'])

        # Create button_color_setter
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'], text_color_setter)

        # Set buttons color with proper text color
        button_color_setter.set_color(self.menu_btn)
        button_color_setter.set_color(self.add_test_btn)

        self.logger.logger.info('Go back to menu button generated.')

    def load_text(self):
        """Load text in choosed language"""

        # Get language code
        self.language = self.main_window.toml_data['settings']['language']

        # Create text_setter
        text_setter = TextSetter(self.language)

        # Load text for all texts in widget
        text_setter.set_title(self.main_window, 'Test')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        text_setter.set_text(self.add_test_btn, 'Dodaj')
        text_setter.set_text(self.age_label, 'Wiek')
        text_setter.set_text(self.name_label, 'Imię')

    def show_edit_fields(self):
        """Show input fields"""

        self.show_name_field()
        self.show_age_field()

    def show_name_field(self):
        """Show input field for name"""

        # Load edit field info label
        self.load_name_field_label()

        # Create input field
        self.name = QLineEdit(self)
        self.name.setFixedSize(100, 20)
        self.name.move(100, 60)
        self.name.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Name line edit generated.")

    def show_age_field(self):
        """Show input field for age"""

        # Load edit ffield info label
        self.load_age_field_label()

        # Create input field
        self.age = QLineEdit(self)
        self.age.setFixedSize(100, 20)
        self.age.setValidator(QIntValidator(18,200))
        self.age.move(100, 120)
        self.age.setStyleSheet(f"background-color: #ffffff;")
        self.logger.logger.info("Age edit generated.")

    def load_age_field_label(self):
        """Load age field input info"""
        
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

    def add_record(self):
        self.logger.logger.debug(self.name.text())
        self.logger.logger.debug(self.age.text())
        self.db.insert([self.name.text(), int(self.age.text()), 35])
        self.logger.logger.info('Record added.')
        self.main_window.start_main_window_UI()
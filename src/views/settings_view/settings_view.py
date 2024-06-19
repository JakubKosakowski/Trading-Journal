from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger, Utils
from src.setters import ButtonColorSetter, TextSetter, TextColorSetter, ButtonTextColorPicker
from src.abstract import ViewClass
from src.meta import MetaClass
import toml


class SettingsView(QWidget, ViewClass, metaclass=MetaClass):
    """A class used to build settings widget

    Arguments
    ---------
        QWidget (class): Class used to create widgets
        ViewClass (class): Abstract class used to override methods for view type classes
        metaclass (class, optional): Class used to inherit by two classes. Defaults to MetaClass.

    Attributes
    ----------
        logger: Logger
            Application logger
        main_window: QMainWindow
            Main window object
        full_screen_checkbox: QCheckBox
            Full screen checkbox

        app_language: QComboBox
            ComboBox for selecting application language
        currency_cb: QComboBox
            ComboBox for selecting main application currency

        menu_btn: QPushButton
            'Go back to menu' button
        primary_color_picker: QPushButton
            Primary color picker
        secondary_color_picker: QPushButton
            Secondary color picker

        app_language_label: QLabel
            Language info label
        currency_cb_label: QLabel
            Currency info label
        primary_color_label: QLabel
            Primary color info label
        secondary_color_label: QLabel
            Secondary color info label

    Methods
    -------
        change_primary_color()
            Set picked color as primary color
        change_secondary_color()
            Set picked color as secondary color
        load_colors()
            Load colors for buttons
        load_text()
            Load text in selected language
        load_combobox_style()
            Load style for comboboxes(test method)
        primary_on_click()
            PyQtslot method for loading pop-up color picker window for primary color
        secondary_on_click()
            PyQtslot method for loading pop-up color picker window for secondary color
        set_app_language()
            Set selected language as application language
        set_screen_size()
            Set size of screen
        set_user_currency()
            Set selected currency as main application currency
    """

    def __init__(self, parent=None):
        """Initializes the instance based on parent window.

        Arguments:
            parent (QMainWindow, optional): window, which show this widget. Defaults to None.
        """

        super(SettingsView, self).__init__(parent)

        # Initiate all used attributes
        self.main_window = parent

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        # Create fullscreen checkbox
        self.full_screen_checkbox = QCheckBox('', self)
        if self.main_window.toml_data['settings']['fullscreen']:
            self.full_screen_checkbox.setChecked(True)
        self.full_screen_checkbox.move(100, 100)
        self.full_screen_checkbox.stateChanged.connect(self.set_screen_size)
        self.logger.logger.info('Full screen mode checkbox generated.')

        # Create currency combobox
        currencies = ['PLN', 'USD', 'GBP', 'CHF', 'JPY']
        self.currency_cb = QComboBox(self)
        self.currency_cb.addItems(currencies)
        self.currency_cb.move(100, 150)
        self.currency_cb.setCurrentIndex(currencies.index(self.main_window.toml_data['settings']['user_currency']))
        self.currency_cb.currentIndexChanged.connect(self.set_user_currency)
        self.logger.logger.info('User currency ComboBox generated.')

        self.currency_cb_label = QLabel(self)
        self.currency_cb_label.move(160, 153)
        self.logger.logger.info('User currency info label generated.')

        # Create language combobox
        languages = ['US', 'PL']
        self.app_language = QComboBox(self)
        self.app_language.addItems(languages)
        self.app_language.move(100, 200)
        self.app_language.setCurrentIndex(languages.index(self.main_window.toml_data['settings']['language']))
        self.app_language.currentIndexChanged.connect(self.set_app_language)
        self.logger.logger.info('Application language ComboBox generated.')

        self.app_language_label = QLabel(self)
        self.app_language_label.move(160, 203)
        self.logger.logger.info('Application language info label generated.')

        # Create primary color picker
        self.primary_color_picker = QPushButton('', self, objectName='primary-color-btn')
        self.primary_color_picker.move(300, 100)
        self.primary_color_picker.resize(20, 20)
        self.primary_color_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.primary_color_picker.clicked.connect(self.primary_on_click)
        self.logger.logger.info('Primary color picker generated.')

        self.primary_color_label = QLabel(self)
        self.primary_color_label.move(330, 100)

        # Create secondary color picker
        self.secondary_color_picker = QPushButton('', self, objectName='secondary-color-btn')
        self.secondary_color_picker.move(300, 130)
        self.secondary_color_picker.resize(20, 20)
        self.secondary_color_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondary_color_picker.clicked.connect(self.secondary_on_click)
        self.logger.logger.info('Secondary color picker generated.')

        self.secondary_color_label = QLabel(self)
        self.secondary_color_label.move(330, 130)

        # Load colors and text
        self.load_colors()
        self.load_text()
        

    def set_screen_size(self):
        """Set screen size as fullscreen or window"""
        try:
            self.main_window.toml_data['settings']['fullscreen'] = not self.main_window.toml_data['settings']['fullscreen']
            if self.main_window.toml_data['settings']['fullscreen']:
                self.main_window.showFullScreen()
                self.logger.logger.info('Full screen enable.')
            else:
                self.main_window.setGeometry(550, 250, 800, 600)
                self.logger.logger.info('Full screen disable.')
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    def set_user_currency(self):
        """Get application main currency and update it in .toml file"""
        try:
            self.main_window.toml_data['settings']['user_currency'] = self.currency_cb.currentText()
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    def set_app_language(self):
        """Get application language and update it in .toml file"""
        try:
            self.main_window.toml_data['settings']['language'] = self.app_language.currentText()
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
            self.load_text()
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    @pyqtSlot()
    def primary_on_click(self):
        self.change_primary_color()

    @pyqtSlot()
    def secondary_on_click(self):
        self.change_secondary_color()

    def change_primary_color(self):
        color = QColorDialog.getColor()

        try:
            self.main_window.toml_data['settings']['primary_color'] = color.name()
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
            self.load_colors()
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    def change_secondary_color(self):
        color = QColorDialog.getColor()

        try:
            self.main_window.toml_data['settings']['secondary_color'] = color.name()
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
            self.load_colors()
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    def load_colors(self):
        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)
        button_text_color_picker.check_pick_condiditon(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'], text_color_setter)
        button_color_setter.set_color(self.menu_btn)
        self.load_combobox_style()
        self.primary_color_picker.setStyleSheet(f"border-style: none; background-color: {self.main_window.toml_data['settings']['primary_color']}")
        self.secondary_color_picker.setStyleSheet(f"border-style: none; background-color: {self.main_window.toml_data['settings']['secondary_color']}")
        
    def load_combobox_style(self):
        self.currency_cb.setStyleSheet(f"background-color: {self.main_window.toml_data['settings']['primary_color']};")

    def load_text(self):
        self.language = self.main_window.toml_data['settings']['language']
        text_setter = TextSetter(self.language)
        text_setter.set_title(self.main_window, 'Ustawienia')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        text_setter.set_text(self.full_screen_checkbox, "Tryb pełnego ekranu")
        text_setter.set_text(self.currency_cb_label, "Waluta użytkownika")
        text_setter.set_text(self.primary_color_label, "Kolory przycisków")
        text_setter.set_text(self.secondary_color_label, "Tło widoku transakcji")
        text_setter.set_text(self.app_language_label, "Język")
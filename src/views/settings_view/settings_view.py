from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger, Utils
import toml

class SettingsView(QWidget):
    def __init__(self, parent=None):
        super(SettingsView, self).__init__(parent)
        self.main_window = parent
        self.language = self.main_window.toml_data['settings']['language']

        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.full_screen_checkbox = QCheckBox('', self)
        if self.main_window.toml_data['settings']['fullscreen']:
            self.full_screen_checkbox.setChecked(True)
        self.full_screen_checkbox.move(100, 100)
        self.full_screen_checkbox.stateChanged.connect(self.set_screen_size)
        self.logger.logger.info('Full screen mode checkbox generated.')

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

        languages = ['US', 'PL']
        self.app_language = QComboBox(self)
        self.app_language.addItems(languages)
        self.app_language.move(100, 200)
        self.app_language.setCurrentIndex(languages.index(self.main_window.toml_data['settings']['language']))
        self.app_language.currentIndexChanged.connect(self.set_app_language)
        self.logger.logger.info('Application language ComboBox generated.')

        self.app_language_label = QLabel(self)
        self.app_language_label.setText('Application language')
        self.app_language_label.move(220, 203)
        self.logger.logger.info('Application language info label generated.')

        self.primary_color_picker = QPushButton('', self, objectName='primary-color-btn')
        self.primary_color_picker.move(300, 100)
        self.primary_color_picker.resize(20, 20)
        self.primary_color_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.primary_color_picker.clicked.connect(self.primary_on_click)
        self.logger.logger.info('Primary color picker generated.')

        self.secondary_color_picker = QPushButton('', self, objectName='secondary-color-btn')
        self.secondary_color_picker.move(300, 130)
        self.secondary_color_picker.resize(20, 20)
        self.secondary_color_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondary_color_picker.clicked.connect(self.secondary_on_click)
        self.logger.logger.info('Secondary color picker generated.')

        self.load_colors()

        self.primary_color_label = QLabel(self)
        self.primary_color_label.move(330, 100)

        self.secondary_color_label = QLabel(self)
        self.secondary_color_label.move(330, 130)

        self.load_text()
        

    def set_screen_size(self):
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
        try:
            self.main_window.toml_data['settings']['user_currency'] = self.currency_cb.currentText()
            with open("config/myproject.toml", "w") as file:
                toml.dump(self.main_window.toml_data, file)
                self.logger.logger.info('Toml data updated.')
        except Exception as err:
            self.logger.logger.error(f'An error occurred: {err}')

    def set_app_language(self):
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
        self.load_menu_button_color()
        self.load_combobox_style()
        self.primary_color_picker.setStyleSheet(f"border-style: none; background-color: {self.main_window.toml_data['settings']['primary_color']}")
        self.secondary_color_picker.setStyleSheet(f"border-style: none; background-color: {self.main_window.toml_data['settings']['secondary_color']}")

    def load_menu_button_color(self):
        self.menu_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.main_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
        
    def load_combobox_style(self):
        self.currency_cb.setStyleSheet(f"background-color: {self.main_window.toml_data['settings']['primary_color']};")

    def load_text(self):
        Utils.set_language_text(self.menu_btn, "Wróć do menu", self.language, self.main_window.toml_data)
        Utils.set_language_text(self.full_screen_checkbox, "Tryb pełnego ekranu", self.language, self.main_window.toml_data)
        Utils.set_language_text(self.currency_cb_label, "Waluta użytkownika", self.language, self.main_window.toml_data)
        Utils.set_language_text(self.primary_color_label, "Kolory przycisków", self.language, self.main_window.toml_data)
        Utils.set_language_text(self.secondary_color_label, "Tło widoku transakcji", self.language, self.main_window.toml_data)
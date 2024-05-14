from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
import toml

class SettingsView(QWidget):
    def __init__(self, parent=None):
        super(SettingsView, self).__init__(parent)
        self.main_window = parent
        self.logger = Logger(__name__)

        self.menu_btn = QPushButton("Go back to menu", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        self.full_screen_checkbox = QCheckBox('Full screen mode', self)
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

        self.primary_color_picker = QPushButton('', self, objectName='primary-color-btn')
        self.primary_color_picker.move(300, 100)
        self.primary_color_picker.resize(20, 20)
        self.primary_color_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.primary_color_picker.clicked.connect(self.primary_on_click)
        self.logger.logger.info('Primary color picker generated.')

        self.load_colors()

        self.primary_color_label = QLabel(self)
        self.primary_color_label.setText("Buttons' color")
        self.primary_color_label.move(330, 100)
        

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

    @pyqtSlot()
    def primary_on_click(self):
        self.change_primary_color()

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

    def load_colors(self):
        self.load_menu_button_color()
        self.primary_color_picker.setStyleSheet(f"border-style: none; background-color: {self.main_window.toml_data['settings']['primary_color']}")

    def load_menu_button_color(self):
        self.menu_btn.setStyleSheet("QPushButton {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid {self.main_window.toml_data['settings']['primary_color']};"
                                            "}"
                                            "QPushButton:hover {"
                                            f"background-color: {self.main_window.toml_data['settings']['primary_color']};"
                                            f"border: 1px solid #005b60;"
                                            "}")
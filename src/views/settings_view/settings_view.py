from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger
from src.postgres_database import Database
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
from pathlib import Path
from src.main_window import MainWindow
from PyQt5.QtWidgets import *
import sys
from src.utils import Logger, Utils

def main():
    logger = Logger(__name__)
    try:
        Utils.download_file('https://static.nbp.pl/dane/kursy/Archiwum/archiwum_tab_a_2024.csv', 'currencies.csv', destination='./config')
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        app.setStyleSheet(Path("static/css/style.css").read_text())
        logger.logger.info('Style file loaded.')
        gui = MainWindow()
        sys.exit(app.exec_())
    except Exception as e:
        logger.logger.error(f'Error: {e}')  

if __name__ == '__main__':
    main()

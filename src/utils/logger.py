import logging
import datetime as dt

class Logger:
    def __init__(self, logger_name):
        logging.basicConfig(level=logging.DEBUG)
        today = dt.datetime.today()
        self.logger = logging.getLogger(logger_name)
        self.filename = f'logs/{today.day:02d}-{today.month:02d}-{today.year}.log'
        self.set_file_handler()
        self.set_formatter()
        self.logger.addHandler(self.file_handler)

    def set_file_handler(self):
        """Set file handler for logger"""
        
        self.file_handler = logging.FileHandler(self.filename)
        self.file_handler.setLevel('INFO')

    def set_formatter(self):
        self.formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s (Line: %(lineno)d [%(filename)s])")
        self.file_handler.setFormatter(self.formatter)

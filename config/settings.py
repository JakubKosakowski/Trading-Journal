from configparser import ConfigParser
import os
import toml
from src.utils import Logger


logger = Logger(__name__)

def config(filename=f"{os.path.dirname(__file__)}/database.ini", section="postgresql"):
    parser = ConfigParser()

    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            f'Section {section} is not found in the {filename} file.'
        )
    logger.logger.info("Database config loaded successfully.")
    return db

def load_toml_settings(filename=f"{os.path.dirname(__file__)}/myproject.toml"):
    try:
        config = toml.load(filename)
        logger.logger.info("Toml file data loaded successfully.")
        return config
    except Exception as err:
        logger.logger.error(f"An error occurred: {err}")
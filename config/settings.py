from configparser import ConfigParser
import os

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
    return db
from urllib.request import urlretrieve
from urllib import error
import csv, json
from .logger import Logger
from static.lang.lang import LANGUAGES

logger = Logger(__name__)

class Utils:
    """Class used to supply utility methods

    Methods
    -------
    download_file(url, filename, destination='./config')
        Download file from given URL path
    convert_csv_to_json(csv_file_path, json_file_path="config/data.json")
        Get .csv file and convert all columns into JSON data
    get_list_of_csv_file_columns(file_path)
        Get list of all columns in given .csv file
    set_language_text(obj, text, lang_code, toml_data)
        Set text in choosen language
    set_title(obj, text, lang_code, toml_data)
        Set window title in choosen language
    hex_to_rgb(value)
        Convert hexadecimal color value into RGB tuple
    """

    @staticmethod
    def download_file(url, filename, destination='./config'):
        """Download file from given URL path

        Arguments
        ---------
            url (str): URL path
            filename (str): name of file
            destination (str, optional): file main directory. Defaults to './config'.

        Returns
        -------
            str: information about success
        """

        try:
            urlretrieve(url, f'{destination}/{filename}')
        except (error.URLError) as err:
            logger.logger.error(f"An error occurred: {err}")
        return 'Success'
    
    @staticmethod
    def convert_csv_to_json(csv_file_path, json_file_path="config/data.json"):
        """Convert .csv file columns into JSON data

        Arguments
        ---------
            csv_file_path (str): path of .csv file
            json_file_path (str, optional): path of .json file. Defaults to "config/data.json".

        Returns
        -------
            str: information about success
        """

        csvfile = open(csv_file_path, 'r')
        jsonfile = open(json_file_path, 'w')

        fieldnames = tuple(Utils.get_list_of_csv_file_columns(csv_file_path))

        reader = csv.DictReader(csvfile, fieldnames)

        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

        return 'Success'

    @staticmethod
    def get_list_of_csv_file_columns(file_path):
        """Get list of all columns names from .csv file

        Arguments
        ---------
            file_path (str): path of .csv file

        Returns
        -------
            list: list of all columns names
        """

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            list_of_columns_names = []

            for row in csv_reader:
                list_of_columns_names.append(row)
                break
        return list_of_columns_names[0]
    
    @staticmethod
    def set_language_text(obj, text, lang_code): # It works without toml_data !!! Remove it!
        """Get object and set text in language choosen in settings

        Arguments
        ---------
            obj (object): PyQt object
            text (str): Text showed in object
            lang_code (str): Choosen language code
            toml_data (dict): .toml data dictionary
        """

        if lang_code == 'PL':
            obj.setText(text)
        else:
            obj.setText(LANGUAGES[lang_code][text])
        logger.logger.info('Object text generated.')

    @staticmethod
    def set_title(obj, text, lang_code): # It works without toml_data !!! Remove it!
        """Get window and set title in language choosen in settings

        Arguments
        ---------
            obj (object): PyQT window
            text (str): Window title
            lang_code (str): Choosen language code
            toml_data (dict): .toml data dictionary
        """
        if lang_code == 'PL':
            obj.setWindowTitle(text)
        else:
            obj.setWindowTitle(LANGUAGES[lang_code][text])
        logger.logger.info('Window title generated.')

    @staticmethod
    def hex_to_rgb(value):
        """Convert hexadecimal color into RGB tuple

        Arguments
        ---------
            value (str): Hexadecimal representation of color

        Returns
        -------
            tuple: Red, Green and Blue values of color
        """
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
from PyQt5.QtWidgets import *
from src.utils import Utils

class TextSetter:
    """
    A class used to creating the TextSetter

    Attributes
    ----------
    lang: str
        Language choosen in settings
    data:
        Data from .toml file

    Methods
    -------
    set_text(obj, text)
        Use Utils class static method to find words in lang dictionary for choosen language
    set_titles(obj, text)
        Use Utils class static method to set widnow title as words in lang dictionary for choosen language
    """

    def __init__(self, lang: str):
        """
        Parameters
        ----------
        lang: str
            Language choosen in settings
        data:
            Data from .toml file
        """

        self.lang = lang

    def set_text(self, obj, text):
        """
        Set text on object in choosen language

        Parameters
        ----------
        obj: Qt Object
            Object, which text we want to set
        text: str
            Text, which we will set in object
        """

        Utils.set_language_text(obj, text, self.lang)

    def set_title(self, obj: QMainWindow | QWidget, text: str):
        """
        Set text on window in choosen language

        Parameters
        ----------
        obj: QMainWindow
            Object, which text we want to set
        text: str
            Text, which we will set in object
        """
        
        Utils.set_title(obj, text, self.lang)

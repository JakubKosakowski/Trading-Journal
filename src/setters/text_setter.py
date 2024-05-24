from abc import ABC, abstractmethod
from src.utils import Utils

class TextSetter:
    def __init__(self, lang, data):
        self.lang = lang
        self.data = data

    def set_text(self, obj, text):
        Utils.set_language_text(obj, text, self.lang, self.data)

    def set_title(self, obj, text):
        Utils.set_title(obj, text, self.lang, self.data)

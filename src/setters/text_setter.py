from abc import ABC, abstractmethod
from src.utils import Utils

class TextSetter:
    def __init__(self, obj, lang, data):
        self.obj = obj
        self.lang = lang
        self.data = data

    def set_text(self, text):
        Utils.set_language_text(self.obj, text, self.lang, self.data)
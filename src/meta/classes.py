from PyQt5.QtWidgets import *
from src.abstract import ViewClass, FormClass


class MetaClass(type(QWidget), type(ViewClass)):
    pass


class MetaFormClass(type(QWidget), type(FormClass)):
    pass
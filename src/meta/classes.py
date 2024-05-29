from PyQt5.QtWidgets import *
from src.abstract import ViewClass

class MetaClass(type(QWidget), type(ViewClass)):
    pass
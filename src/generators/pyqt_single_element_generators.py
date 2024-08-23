from src.abstract import GenerateSinglePyQtElement
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QLineEditGenerator(GenerateSinglePyQtElement):
    def __init__(self, widget: QWidget, default_value: (int | float)):
        self.widget = widget
        self.defalt_value = default_value

    def generate_element(self, position_x: int, position_y: int, readonly: bool = False):
        """Generate single QLineEdit input

        Arguments
        ---------
            readonly (bool, optional): Check, if this input is readonly. Defaults to False.
        """

        element = QLineEdit(self.widget)
        element.setValidator(QDoubleValidator(0.001,99999.999,3))
        element.setReadOnly(readonly)
        element.setGeometry(position_x, position_y, 50, 20)
        # element.setFixedSize(50, 20)
        if readonly:
            element.setStyleSheet(f"background-color: gray;")
        else:
            element.setStyleSheet(f"background-color: #ffffff;")
        return element
    

class QPushButtonGenerator(GenerateSinglePyQtElement):
    pass
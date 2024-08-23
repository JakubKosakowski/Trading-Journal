from types import FunctionType
from src.abstract import GenerateSinglePyQtElement, GenerateButtonElement
from src.setters import ButtonColorSetter, TextColorSetter, ButtonTextColorPicker, TextSetter
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
    

class QPushButtonGenerator(GenerateButtonElement):
    def __init__(self, widget: QWidget, color: str, text_setter: TextSetter):
        self.widget = widget
        self.color = color

        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)
        button_text_color_picker.check_pick_condiditon(self.color)

        self.button_color_setter = ButtonColorSetter(self.color, text_color_setter)
        self.text_setter = text_setter

    def generate_element(self, name: str, text: str, position_x: int, position_y: int):
        element = QPushButton('', self.widget, objectName=name)
        element.move(position_x, position_y)

        self.button_color_setter.set_color(element)
        self.text_setter.set_text(element, text)
        
        return element
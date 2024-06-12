from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.abstract import ColorSetter, ColorPicker
from src.utils import Utils
from typing import List


class ProfitLossColorPicker(ColorPicker):
    """Color picker used to check if value is positive or negatice an choice correct text color

    Arguments
    ---------
        ColorPicker (class): An abstract class

    Returns
    --------
        boolean: tell if text should be in profit color
    """
    profit = False

    def check_pick_condiditon(self, value: str):
        """Check if value is positive or negative

        Arguments
        ---------
            value (str): Transactions result value
        """

        self.profit = int([x for x in value.split()][0]) >= 0

    def get_condition_value(self):
        """Class main attribute getter

        Returns
        -------
            boolean: tell if text should be in profit color
        """

        return self.profit


class ButtonTextColorPicker(ColorPicker):
    """Color picker used to check button color and choice properly text color

    Arguments
    ---------
        ColorPicker (class): An abstract class

    Returns
    -------
        boolean: tell if text should be dark
    """

    dark_text = False

    def check_pick_condiditon(self, value: str):
        """Check if button background color is enough bright to set dark text

        Arguments
        ---------
            value (str): Hexadecimal color value
        """

        r, g, b = Utils.hex_to_rgb(value)
        if (r > 200 and g > 230) or (b > 220):
            self.dark_text = True

    def get_condition_value(self):
        """Class main attribute getter

        Returns
        -------
            boolean: tell if text should be dark
        """
        
        return self.dark_text
    

class ButtonColorSetter(ColorSetter):
    """A class used to coloring buttons for choosen primary color

    Arguments
    ---------
    ColorSetter (class): An abstract class

    Attributes
    ----------
    color: str
        buttons' color
    text_color_setter: ColorSetter
        object used to set the button text color 

    Methods
    -------
    set_color(element: QPushButton)
        Set background and text color for button
    """
    
    def __init__(self, color: str, text_color_setter: ColorSetter):
        """Initializes the instance based on primary color and text color

        Arguments
        ---------
            color (str): Color choosen for button
            text_color_setter (ColorSetter): object checked button color to choose proper text color
        """
        self.color = color
        self.text_color_setter = text_color_setter

    def set_color(self, element: QPushButton) -> None:
        """Set text and background color for button

        Arguments
        ---------
            element (QPushButton): button object
        """
        element.setStyleSheet("QPushButton {"
                                f"background-color: {self.color};"
                                f"border: 1px solid {self.color};"
                                "}"
                                "QPushButton:hover {"
                                f"background-color: {self.color};"
                                f"border: 1px solid #005b60;"
                                "}")
        self.text_color_setter.set_color(element)
        

class BackgroundColorSetter(ColorSetter):
    """Class used to set transactions table background color

    Arguments
    ---------
    ColorSetter (class): An abstract class 

    Attributes
    ----------
    color: str
        secondary color choosen in settings 
    
    Methods
    -------
    set_color(element)
        set background color for transactions table
    """

    def __init__(self, color: str):
        """Initializes the instance based on secondary color

        Arguments
        ---------
            color (str): Color choosen for background
        """
        self.color = color

    def set_color(self, element: QTableWidget) -> None:
       """Set background color for table

        Arguments
        ---------
            element (QPushButton): table object
        """
       element.setStyleSheet("QTableWidget {"
                                f"background-color: {self.color};"
                                "}"
                                "QHeaderView {"
                                f"background-color: {self.color};"
                                "}") 
       

class TextColorSetter(ColorSetter):
    """Class used to set text color in buttons

    Arguments
    ---------
        ColorSetter (class): An abstract class
    
    Attributes
    ----------
    color: List[str]
        list of available text colors
    picker: ColorPicker
        object used to check condition to pick a correct color

    Methods
    -------
    set_color(element)
        set text color for button
    """

    def __init__(self, color: List[str], picker: ColorPicker):
        """Initializes the instance based on list of available text colors and color picker with specific condition checker

        Arguments
        ---------
            color (List[str]): List of available colors
            picker (ColorPicker): object used to check condition
        """

        self.color = color
        self.picker = picker

    def set_color(self, element) -> None:
        """Set text color in button

        Arguments
        ---------
            element (QPushButton): button object
        """

        if self.picker.get_condition_value():
            if element.styleSheet() == '':
                element.setStyleSheet(f'color: {self.color[1]}')
            else:
                element.setStyleSheet(element.styleSheet().replace("}", f'color: {self.color[1]}'+"}"))
        else:
            if element.styleSheet() == '':
                element.setStyleSheet(f'color: {self.color[0]}')
            else:
                element.setStyleSheet(element.styleSheet().replace("}", f'color: {self.color[0]}'+"}"))
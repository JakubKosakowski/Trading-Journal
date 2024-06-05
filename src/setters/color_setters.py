from PyQt5.QtWidgets import *
from src.abstract import ColorSetter, ColorPicker
from src.utils import Utils
from typing import List


class ProfitLossColorPicker(ColorPicker):
    profit = False

    def check_pick_condiditon(self, value: str):
        self.profit = int([x for x in value.split()][0]) >= 0

    def get_condition_value(self):
        return self.profit


class ButtonTextColorPicker(ColorPicker):
    dark_text = False

    def check_pick_condiditon(self, value: str):
        r, g, b = Utils.hex_to_rgb(value)
        if (r > 200 and g > 230) or (b > 220):
            self.dark_text = True

    def get_condition_value(self):
        return self.dark_text
    

class ButtonColorSetter(ColorSetter):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, element: QPushButton) -> None:
        element.setStyleSheet("QPushButton {"
                                f"background-color: {self.color};"
                                f"border: 1px solid {self.color};"
                                "}"
                                "QPushButton:hover {"
                                f"background-color: {self.color};"
                                f"border: 1px solid #005b60;"
                                "}")
        

class BackgroundColorSetter(ColorSetter):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, element: QTableWidget) -> None:
       element.setStyleSheet("QTableWidget {"
                                f"background-color: {self.color};"
                                "}"
                                "QHeaderView {"
                                f"background-color: {self.color};"
                                "}") 
       

class TextColorSetter(ColorSetter):
    def __init__(self, color: List[str], picker: ColorPicker):
        self.color = color
        self.picker = picker

    def set_color(self, element) -> None:
        if self.picker.get_condition_value():
            element.setStyleSheet(f'color: {self.color[1]}')
        else:
            element.setStyleSheet(f"color: {self.color[0]}")
from PyQt5.QtWidgets import *
from src.abstract import ColorSetter, ColorPicker
from typing import List


class ProfitLossColorPicker(ColorPicker):
    profit = False

    def check_pick_condiditon(self, value: str):
        self.profit = int([x for x in value.split()][0]) >= 0

    def is_profit(self):
        return self.profit


class ButtonTextColorPicker(ColorPicker):
    pass
    

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
    def __init__(self, color: List[str], picker: ProfitLossColorPicker):
        self.color = color
        self.picker = picker

    def set_color(self, element: QLabel) -> None:
        if self.picker.is_profit():
            element.setStyleSheet("QLabel {"
                                f"color: {self.color[1]}"
                                "}")
        else:
            element.setStyleSheet("QLabel {"
                                f"color: {self.color[0]}"
                                "}")
from abc import ABC, abstractmethod

class ColorSetter(ABC):
    @abstractmethod
    def set_color(self, element):
        pass


class ButtonColorSetter(ColorSetter):
    def __init__(self, color):
        self.color = color

    def set_color(self, element):
        element.setStyleSheet("QPushButton {"
                                f"background-color: {self.color};"
                                f"border: 1px solid {self.color};"
                                "}"
                                "QPushButton:hover {"
                                f"background-color: {self.color};"
                                f"border: 1px solid #005b60;"
                                "}")
        

class BackgroundColorSetter(ColorSetter):
    def __init__(self, color):
        self.color = color

    def set_color(self, element):
       element.setStyleSheet("QTableWidget {"
                                f"background-color: {self.color};"
                                "}"
                                "QHeaderView {"
                                f"background-color: {self.color};"
                                "}") 
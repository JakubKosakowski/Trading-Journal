from abc import ABC, abstractmethod

class ColorSetter(ABC):
    @abstractmethod
    def set_color(self, element):
        pass
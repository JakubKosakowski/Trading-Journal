from abc import ABC, abstractmethod

class GenerateSinglePyQtElement(ABC):
    @abstractmethod
    def generate_element(self, position_x: int, position_y: int, readonly: bool = False):
        pass


class GenerateButtonElement(ABC):
    @abstractmethod
    def generate_element(self, name: str, text: str, position_x: int, position_y: int):
        pass
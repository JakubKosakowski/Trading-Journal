from abc import ABC, abstractmethod
from types import FunctionType

class GenerateSinglePyQtElement(ABC):
    @abstractmethod
    def generate_element(self, position_x: int, position_y: int, readonly: bool = False):
        pass


class GenerateButtonElement(ABC):
    @abstractmethod
    def generate_element(self, position_x: int, position_y: int, connect_func: FunctionType):
        pass
from abc import ABC, abstractmethod

class GenerateSinglePyQtElement(ABC):
    @abstractmethod
    def generate_element(self, readonly: bool = False):
        pass
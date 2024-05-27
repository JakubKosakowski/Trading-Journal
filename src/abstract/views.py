from abc import ABC, abstractmethod

class ViewClass(ABC):

    @abstractmethod
    def load_colors(self):
        pass

    @abstractmethod
    def load_text(self):
        pass
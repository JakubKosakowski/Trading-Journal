from abc import ABC, abstractmethod


#Abstract class for every view class in application
class ViewClass(ABC):

    @abstractmethod
    def load_colors(self):
        pass

    @abstractmethod
    def load_text(self):
        pass
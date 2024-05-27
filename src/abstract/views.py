from abc import ABCMeta, abstractmethod


#Abstract class for every view class in application
class ViewClass(ABCMeta):

    @abstractmethod
    def load_colors(self):
        pass

    @abstractmethod
    def load_text(self):
        pass
from abc import ABC, abstractmethod


#Abstract class for every view class in application
class ViewClass(ABC):

    @abstractmethod
    def load_colors(self) -> None:
        pass

    @abstractmethod
    def load_text(self) -> None:
        pass


class FormClass(ABC):

    @abstractmethod
    def add_record(self, values: list) -> None:
        pass

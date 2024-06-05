from abc import ABC, abstractmethod

class ColorPicker(ABC):
    @abstractmethod
    def check_pick_condiditon(self, value: str):
        pass

    @abstractmethod
    def get_condition_value(self):
        pass
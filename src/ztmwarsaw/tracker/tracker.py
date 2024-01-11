from abc import ABC, abstractmethod


class Tracker(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def build(self, api_caller):
        pass

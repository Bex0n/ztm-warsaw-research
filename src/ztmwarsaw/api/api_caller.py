from abc import ABC, abstractmethod


class APICaller(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def call(self):
        pass

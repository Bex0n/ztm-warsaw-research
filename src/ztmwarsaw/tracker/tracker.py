from abc import ABC, abstractmethod
from ztmwarsaw.api.api_caller import APICaller


class Tracker(ABC):
    def __init__(self, api_caller: APICaller):
        super().__init__()
        self.api_caller = api_caller

    @abstractmethod
    def track(self, params):
        pass

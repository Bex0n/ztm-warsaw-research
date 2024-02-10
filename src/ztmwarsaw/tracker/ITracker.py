from abc import ABC, abstractmethod
from typing import Any, List

from ztmwarsaw.api.ICaller import ICaller


class ITracker(ABC):
    def __init__(self, api_caller: ICaller) -> None:
        super().__init__()
        self.api_caller = api_caller

    @abstractmethod
    def track(self, *args: Any, **kwargs: Any) -> List[Any]:
        pass

    def save(self, filename: str) -> None:
        pass

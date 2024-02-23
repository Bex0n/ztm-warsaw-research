from abc import ABC, abstractmethod
from typing import Any, List

from ztmwarsaw.api.ICaller import ICaller


class ITracker(ABC):
    """
    An abstract base class that defines the interface for tracker classes.
    These trackers utilize an API caller to fetch and process real-time data.
    """

    def __init__(self, api_caller: ICaller) -> None:
        """
        Initializes the tracker with an API caller.

        :param api_caller: An instance of a class that implements the ICaller interface.
        """
        super().__init__()
        self.api_caller = api_caller

    @abstractmethod
    def track(self, *args: Any, **kwargs: Any) -> List[Any]:
        """
        Abstract method that must be implemented by subclasses to track and return
        real-time data based on specified criteria.

        :return: A list of data points collected during tracking.
        """
        pass

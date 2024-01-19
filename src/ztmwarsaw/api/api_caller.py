from abc import ABC, abstractmethod
from typing import Any, Dict


class APICaller(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_location(self) -> Dict[str, Any]:
        pass

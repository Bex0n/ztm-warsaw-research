from abc import ABC, abstractmethod
from typing import Dict, Optional

from pydantic import BaseModel


class LocationRequest(BaseModel):
    line: str
    brigade: Optional[str] = None


class ICaller(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_location(self, params: LocationRequest) -> Optional[Dict]:
        pass

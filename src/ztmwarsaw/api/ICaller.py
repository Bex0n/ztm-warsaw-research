from abc import ABC, abstractmethod
from typing import Dict, Optional

from pydantic import BaseModel


class LocationRequest(BaseModel):
    """
    Defines optional query parameters for location requests with attributes for line and brigade,
    allowing filtering of the location data.
    """

    line: Optional[str] = None
    brigade: Optional[str] = None


class ICaller(ABC):
    """
    An abstract base class that outlines the interface for API caller classes.
    It defines a contract for subclasses to implement the get_location method.
    """

    def __init__(self) -> None:
        """
        An abstract base class defining the interface for caller classes
        """
        pass

    @abstractmethod
    def get_location(self, params: LocationRequest) -> Optional[Dict]:
        """
        Abstract method to be implemented by subclasses to fetch location data
        """
        pass

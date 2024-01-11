import requests

from typing import Any, Dict
from .api_caller import APICaller
from pydantic import BaseModel


class LocationRequest(BaseModel):
    line: str
    brigade: str


class BusCaller(APICaller):
    def __init__(self, api_key: str):
        APICaller.__init__(self)
        self.location_url = "https://api.um.warszawa.pl/api/action/busestrams_get/"
        self.schedule_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get/"

    def __get_data(self, url: str, params: LocationRequest) -> Dict[str, Any]:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
        else:
            raise Exception("Error while calling API")

        if result["result"] is None:
            raise Exception("Error while calling API")

        return result["result"]

    def get_location(self, params: LocationRequest) -> Dict[str, Any]:
        return self.__get_data(self.location_url, params)

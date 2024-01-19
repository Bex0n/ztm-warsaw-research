import requests

from typing import Any, Dict, Optional
from .api_caller import APICaller
from pydantic import BaseModel


class LocationRequest(BaseModel):
    line: str
    apikey: Optional[str]
    brigade: Optional[str]
    resource_id: Optional[str]
    vehicle_type: Optional[int]


class BusCaller(APICaller):
    def __init__(self, apikey: str):
        APICaller.__init__(self)
        self.location_url = "https://api.um.warszawa.pl/api/action/busestrams_get/"
        self.schedule_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get/"
        self.resource_id = "f2e5503e-927d-4ad3-9500-4ab9e55deb59"
        self.apikey = apikey
        self.vehicle_type = 1

    def __get_obligatory_params(self, params: LocationRequest) -> Dict[str, Any]:
        params["apikey"] = self.apikey
        params["resource_id"] = self.resource_id
        params["type"] = self.vehicle_type

        return params

    def __get_data(self, url: str, params: LocationRequest) -> Dict[str, Any]:
        params = self.__get_obligatory_params(params)
        response = requests.get(url, params=params)
        print(response.json())
        if response.status_code == 200:
            result = response.json()
        else:
            raise Exception("Error while calling API")

        if result["result"] is None:
            raise Exception("Error while calling API")

        return result["result"]

    def get_location(self, params: LocationRequest) -> Dict[str, Any]:
        return self.__get_data(self.location_url, params)

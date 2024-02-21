from typing import Any, Dict, Optional

import requests

from ztmwarsaw.api.ICaller import ICaller, LocationRequest


class BusCaller(ICaller):
    def __init__(self, apikey: str):
        ICaller.__init__(self)
        self.location_url = "https://api.um.warszawa.pl/api/action/busestrams_get/"
        self.schedule_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get/"
        self.stop_url = "https://api.um.warszawa.pl/api/action/dbstore_get/"
        self.location_resource_id = "f2e5503e-927d-4ad3-9500-4ab9e55deb59"
        self.stop_resource_id = "ab75c33d-3a26-4342-b36a-6e5fef0a3ac3"
        self.apikey = apikey
        self.vehicle_type = 1

    def __get_location_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        obligatory_params = {
            "apikey": self.apikey,
            "resource_id": self.location_resource_id,
            "type": self.vehicle_type,
            **params,
        }
        return obligatory_params

    def __get_stop_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        obligatory_params = {
            "apikey": self.apikey,
            "id": self.stop_resource_id,
            **params,
        }
        return obligatory_params

    def __get_data(self, url: str, params: Dict[str, Any]) -> Optional[Dict]:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return None

        result = response.json()
        if result.get("result") == "Błędna metoda lub parametry wywołania":
            return None

        return result.get("result", None)

    def get_location(self, params: LocationRequest) -> Optional[Dict]:
        params_dict = self.__get_location_obligatory_params(params.dict())
        return self.__get_data(self.location_url, params_dict)

    def get_all_locations(self) -> Optional[Dict]:
        params = self.__get_location_obligatory_params({})
        return self.__get_data(self.location_url, params)

    def get_all_stops(self) -> Optional[Dict]:
        params = self.__get_stop_obligatory_params({})
        return self.__get_data(self.stop_url, params=params)

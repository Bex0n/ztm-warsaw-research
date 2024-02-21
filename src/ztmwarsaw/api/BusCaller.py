from typing import Any, Dict, Optional

import requests

from ztmwarsaw.api.ICaller import ICaller, LocationRequest


class BusCaller(ICaller):
    def __init__(self, apikey: str):
        ICaller.__init__(self)
        self.location_url = "https://api.um.warszawa.pl/api/action/busestrams_get/"
        self.schedule_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get/"
        self.resource_id = "f2e5503e-927d-4ad3-9500-4ab9e55deb59"
        self.apikey = apikey
        self.vehicle_type = 1

    def __get_obligatory_params(self, params: LocationRequest) -> Dict[str, Any]:
        obligatory_params = {
            "apikey": self.apikey,
            "resource_id": self.resource_id,
            "type": self.vehicle_type,
            **params.dict(),
        }
        return obligatory_params

    def __get_data(self, url: str, params: LocationRequest) -> Optional[Dict]:
        params_dict = self.__get_obligatory_params(params)
        print("Url: ", url)
        print("Params: ", params_dict)
        response = requests.get(url, params=params_dict)
        if response.status_code != 200:
            return None

        result = response.json()
        if result.get("result") == "Błędna metoda lub parametry wywołania":
            return None

        return result.get("result", None)

    def get_location(self, params: LocationRequest) -> Optional[Dict]:
        return self.__get_data(self.location_url, params)

    def get_all_locations(self) -> Optional[Dict]:
        return self.__get_data(self.location_url, LocationRequest())

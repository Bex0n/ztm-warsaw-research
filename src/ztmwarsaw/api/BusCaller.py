from typing import Any, Dict, Optional

import requests

from ztmwarsaw.api.ICaller import ICaller, LocationRequest


class BusCaller(ICaller):
    """
    Concrete implementation of the ICaller interface for fetching bus-related data
    from the Warsaw public transport API.
    """

    def __init__(self, apikey: str):
        """
        Initializes the BusCaller with necessary API configuration.
        :param apikey: API key for authenticating requests to the public transport API.
        """
        ICaller.__init__(self)
        # API URLs and resource IDs for different types of requests
        self.location_url = "https://api.um.warszawa.pl/api/action/busestrams_get/"
        self.schedule_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get/"
        self.stop_url = "https://api.um.warszawa.pl/api/action/dbstore_get/"
        # Additional initialization for other URLs and resource IDs
        self.location_resource_id = "f2e5503e-927d-4ad3-9500-4ab9e55deb59"
        self.stop_lines_resource_id = "88cd555f-6f31-43ca-9de4-66c479ad5942"
        self.stop_resource_id = "ab75c33d-3a26-4342-b36a-6e5fef0a3ac3"
        self.schedule_resource_id = "e923fa0e-d96c-43f9-ae6e-60518c9f3238"
        self.apikey = apikey
        self.vehicle_type = 1

    def __get_location_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Constructs and returns obligatory parameters for location API requests.

        :param params: Additional parameters for the request.
        :return: A dictionary of obligatory parameters merged with additional params.
        """
        obligatory_params = {
            "apikey": self.apikey,
            "resource_id": self.location_resource_id,
            "type": self.vehicle_type,
            **params,
        }
        return obligatory_params

    def __get_stop_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Constructs and returns obligatory parameters for busstops API requests.

        :param params: Additional parameters for the request.
        :return: A dictionary of obligatory parameters merged with additional params.
        """
        obligatory_params = {
            "apikey": self.apikey,
            "id": self.stop_resource_id,
            **params,
        }
        return obligatory_params

    def __get_stop_lines_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Constructs and returns obligatory parameters for busstop lines API requests.

        :param params: Additional parameters for the request.
        :return: A dictionary of obligatory parameters merged with additional params.
        """
        obligatory_params = {
            "apikey": self.apikey,
            "id": self.stop_lines_resource_id,
            **params,
        }
        return obligatory_params

    def __get_schedule_obligatory_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Constructs and returns obligatory parameters for schedule API requests.

        :param params: Additional parameters for the request.
        :return: A dictionary of obligatory parameters merged with additional params.
        """
        obligatory_params = {
            "apikey": self.apikey,
            "id": self.schedule_resource_id,
            **params,
        }
        return obligatory_params

    def __get_data(self, url: str, params: Dict[str, Any]) -> Optional[Dict]:
        """
        Performs an HTTP GET request to the specified URL with given parameters
        and processes the response.

        :param url: The API endpoint URL.
        :param params: Parameters for the request.
        :return: Optional dictionary containing the API response data.
        """
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return None

        result = response.json()
        if result.get("result") == "Błędna metoda lub parametry wywołania":
            return None

        return result.get("result", None)

    def get_location(self, params: LocationRequest) -> Optional[Dict]:
        """
        Fetches location data for a specific vehicle or set of vehicles based on the provided parameters.

        :param params: LocationRequest object containing query parameters.
        :return: Optional dictionary containing the location data.
        """
        params_dict = self.__get_location_obligatory_params(params.dict())
        return self.__get_data(self.location_url, params_dict)

    def get_all_locations(self) -> Optional[Dict]:
        """
        Fetches the locations of all vehicles currently available in the dataset.

        :return: An optional dictionary containing all vehicle location data if the request is successful; None otherwise.
        """
        params = self.__get_location_obligatory_params({})
        return self.__get_data(self.location_url, params)

    def get_all_stops(self) -> Optional[Dict]:
        """
        Retrieves a list of all bus stops within the dataset.

        :return: An optional dictionary containing data for all bus stops if the request is successful; None otherwise.
        """
        params = self.__get_stop_obligatory_params({})
        return self.__get_data(self.stop_url, params=params)

    def get_stop_lines(self, stop_id: str, stop_nr: str) -> Optional[Dict]:
        """
        Fetches the bus lines that stop at a specified bus stop.

        :param stop_id: The identifier of the bus stop.
        :param stop_nr: The number of the specific stop at the bus stop.
        :return: An optional dictionary containing the lines stopping at the specified bus stop if the request is successful; None otherwise.
        """
        params = self.__get_stop_lines_obligatory_params(
            {
                "busstopId": stop_id,
                "busstopNr": stop_nr,
            }
        )
        return self.__get_data(self.schedule_url, params=params)

    def get_schedule(self, stop_id: str, stop_nr: str, line: str) -> Optional[Dict]:
        """
        Retrieves the schedule for a specific bus line at a given bus stop.

        :param stop_id: The identifier of the bus stop.
        :param stop_nr: The number of the specific stop at the bus stop.
        :param line: The bus line for which to retrieve the schedule.
        :return: An optional dictionary containing the schedule for the specified line and bus stop if the request is successful; None otherwise.
        """
        params = self.__get_schedule_obligatory_params(
            {
                "busstopId": stop_id,
                "busstopNr": stop_nr,
                "line": line,
            }
        )
        return self.__get_data(self.schedule_url, params=params)

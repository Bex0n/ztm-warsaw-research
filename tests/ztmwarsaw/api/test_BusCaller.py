from typing import Dict, Optional

import pytest
import requests_mock

from ztmwarsaw import BusCaller, LocationRequest


@pytest.fixture
def bus_caller() -> BusCaller:
    apikey: str = "test_api_key"
    return BusCaller(apikey=apikey)


def test_get_location_success(bus_caller: BusCaller) -> None:
    with requests_mock.Mocker() as m:
        mock_response: Dict[str, str] = {"result": "success"}
        m.get("https://api.um.warszawa.pl/api/action/busestrams_get/", json=mock_response)

        params: LocationRequest = LocationRequest(line="1", brigade="1")
        result: Optional[Dict] = bus_caller.get_location(params=params)

        assert result == "success"


def test_get_location_failure(bus_caller: BusCaller) -> None:
    with requests_mock.Mocker() as m:
        m.get("https://api.um.warszawa.pl/api/action/busestrams_get/", status_code=500)

        params: LocationRequest = LocationRequest(line="1", brigade="1")
        result: Optional[Dict] = bus_caller.get_location(params=params)

        assert result is None

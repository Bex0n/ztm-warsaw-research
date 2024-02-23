import json
from tempfile import NamedTemporaryFile
from typing import Generator, List
from unittest.mock import Mock, create_autospec, patch

import pytest

from ztmwarsaw.api.ICaller import ICaller
from ztmwarsaw.tracker.BusTracker import BusTracker


@pytest.fixture
def api_caller_mock() -> Mock:
    return create_autospec(ICaller)


@pytest.fixture
def bus_tracker(api_caller_mock: Mock) -> BusTracker:
    return BusTracker(apicaller=api_caller_mock)


@pytest.fixture
def temp_file() -> Generator[str, None, None]:
    with NamedTemporaryFile(mode="w+", delete=False) as tmp:
        yield tmp.name


def test_track_with_valid_parameters(bus_tracker: BusTracker, api_caller_mock: Mock) -> None:
    mock_response: List[dict] = [{"VehicleNumber": "123", "SomeOtherKey": "SomeValue"}]
    api_caller_mock.get_location.return_value = mock_response

    with patch("time.sleep", return_value=None):
        result: List[dict] = bus_tracker.track(
            line="1", brigade="1", duration=10, frequency=5, vehicle_number="123"
        )

    assert len(result) == 2
    assert result[0]["VehicleNumber"] == "123"
    api_caller_mock.get_location.assert_called()


def test_track_writes_to_file(
    bus_tracker: BusTracker, api_caller_mock: Mock, temp_file: str
) -> None:
    mock_response: List[dict] = [{"VehicleNumber": "123", "SomeOtherKey": "SomeValue"}]
    api_caller_mock.get_location.return_value = mock_response

    with patch("time.sleep", return_value=None):
        bus_tracker.track(
            line="1",
            brigade="1",
            duration=10,
            frequency=5,
            vehicle_number="123",
            filepath=temp_file,
        )

    with open(temp_file, "r") as f:
        lines: List[str] = f.readlines()
        assert len(lines) == 2
        assert json.loads(lines[0]) == mock_response[0]

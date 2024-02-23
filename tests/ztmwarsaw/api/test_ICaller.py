from typing import Dict, Optional
from unittest.mock import Mock

import pytest

from ztmwarsaw.api.ICaller import ICaller, LocationRequest


class MockCaller(ICaller):
    def get_location(self, params: LocationRequest) -> Optional[Dict[str, str]]:
        return {"location": "mock"} if params.line and params.brigade else None


@pytest.fixture
def location_request() -> LocationRequest:
    return LocationRequest(line="10", brigade="1")


@pytest.fixture
def mock_caller() -> MockCaller:
    return MockCaller()


def test_icaller_subclass_can_be_instantiated(mock_caller: MockCaller) -> None:
    assert mock_caller is not None


def test_icaller_subclass_get_location_with_valid_params(
    mock_caller: MockCaller, location_request: LocationRequest
) -> None:
    result = mock_caller.get_location(params=location_request)
    assert result is not None
    assert result["location"] == "mock"


def test_icaller_subclass_get_location_with_invalid_params(mock_caller: MockCaller) -> None:
    result = mock_caller.get_location(params=LocationRequest())
    assert result is None

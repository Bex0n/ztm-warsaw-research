from typing import Any, List
from unittest.mock import create_autospec

import pytest

from ztmwarsaw.api.ICaller import ICaller
from ztmwarsaw.tracker.ITracker import ITracker


class MockCaller(ICaller):
    def get_location(self, params: Any) -> Any:
        return {"mock_key": "mock_value"}


class MockTracker(ITracker):
    def track(self, *args: Any, **kwargs: Any) -> List[Any]:
        return [args, kwargs]


@pytest.fixture
def mock_api_caller() -> MockCaller:
    return create_autospec(MockCaller)


@pytest.fixture
def mock_tracker(mock_api_caller: MockCaller) -> MockTracker:
    return MockTracker(api_caller=mock_api_caller)


def test_itracker_subclass_can_be_instantiated(mock_tracker: MockTracker) -> None:
    assert mock_tracker is not None


def test_itracker_subclass_track_with_args(mock_tracker: MockTracker) -> None:
    args = (1, 2, 3)
    result: List[Any] = mock_tracker.track(*args)
    assert result[0] == args


def test_itracker_subclass_track_with_kwargs(mock_tracker: MockTracker) -> None:
    kwargs = {"a": 1, "b": 2}
    result: List[Any] = mock_tracker.track(**kwargs)
    assert result[1] == kwargs

import pytest
from ztmwarsaw.api.bus_caller import BusCaller
from unittest.mock import patch, MagicMock


@pytest.fixture
def bus_caller():
    return BusCaller()


def test_build(bus_caller):
    test_url = 'https://test.url'
    bus_caller.build(url=test_url)
    assert bus_caller.url == test_url, "URL should be set to the provided URL"


@patch('urllib.request.urlopen')
def test_call(mock_urlopen, bus_caller):
    test_response = 'mock_response'
    mock_urlopen.return_value = MagicMock(read=MagicMock(return_value=test_response))

    bus_caller.build()  # Set default URL
    response = bus_caller.call()

    assert mock_urlopen.called, "urlopen should be called"
    assert response == test_response, "Response should match the mock response"

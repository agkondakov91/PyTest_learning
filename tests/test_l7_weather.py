from unittest.mock import MagicMock, patch

from lections.L7.weather import is_cold


@patch("lections.L7.weather.get_temperature")
def test_is_cold_returns_true_when_below_10(mock_get_temperature: MagicMock):
    mock_get_temperature.return_value = 5.0
    assert is_cold("Moscow") is True


@patch("lections.L7.weather.get_temperature")
def test_is_cold_returns_false_when_above_10(mock_get_temperature: MagicMock):
    mock_get_temperature.return_value = 20.0
    assert is_cold("Moscow") is False


def test_is_cold_with_monkeypatch(monkeypatch):
    def fake_get_temperature(city: str) -> float:
        return 3.0

    monkeypatch.setattr("lections.L7.weather.get_temperature", fake_get_temperature)
    assert is_cold("Moscow") is True

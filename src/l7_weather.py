import json
import urllib.request


def get_temperature(city: str) -> float:
    """Получает текущую температуру в городе через внешний API."""
    url = f"https://api.weather.example.com/current?city={city}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data["temperature"]


def is_cold(city: str) -> bool:
    """Возвращает True, если температура ниже 10 градусов."""
    return get_temperature(city) < 10

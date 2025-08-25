from unittest.mock import patch
from weather import get_weather

def test_get_weather_mocked():
    mock_response = {"temp": "20°C", "condition": "Sunny"}

    with patch("weather.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        result = get_weather("London")
        assert result == mock_response
from unittest.mock import patch
from weather import get_weather

def test_get_weather_calls_requests_correctly():
    mock_response = {"temp": "20°C", "condition": "Sunny"}

    with patch("weather.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        result = get_weather("London")
        # re assertion: of course it passes
        assert result == mock_response

        # ✅ Assert the correct URL was called
        mock_get.assert_called_once_with("https://api.weather.com/xLondon")



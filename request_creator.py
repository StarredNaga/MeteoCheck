from api_models import WeatherRequest, Language, Units

def get_weekly_request(api_key : str, lat : float, lon : float) -> WeatherRequest:
    """Создает запрос для получения недельного прогноза погоды"""

    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["current", "minutely", "hourly", "alerts"],
        lang=Language.RUSSIAN,
        units=Units.METRIC
    )

def get_current_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения текущей погоды"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["daily", "minutely", "hourly", "alerts"],
        lang=Language.RUSSIAN,
        units=Units.METRIC
    )

def get_hourly_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения почасового прогноза на 48 часов"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["current", "daily", "minutely", "alerts"],
        lang=Language.RUSSIAN,
        units=Units.METRIC
    )

def get_all_weather_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения всей доступной информации о погоде"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=None,
        lang=Language.RUSSIAN,
        units=Units.METRIC
    )
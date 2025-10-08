from api_models import WeatherRequest, Language, Units
from settings import Settings

# Инициализируем настройки
settings = Settings()

match settings.language:

    case "RUSSIAN": language = Language.RUSSIAN

    case "ENGLISH": language = Language.ENGLISH

    case "GERMAN": language = Language.GERMAN

    case "FRENCH": language = Language.FRENCH

    case _: raise ValueError("Incorrect language property")

match settings.units:
    
    case "METRIC": units = Units.METRIC

    case "STANDARD": units = Units.STANDARD

    case "IMPERIAL": units = Units.IMPERIAL

    case _: raise ValueError("Incorrect units property")


def get_weekly_request(api_key : str, lat : float, lon : float) -> WeatherRequest:
    """Создает запрос для получения недельного прогноза погоды"""

    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["current", "minutely", "hourly", "alerts"],
        lang=language,
        units=units
    )

def get_current_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения текущей погоды"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["daily", "minutely", "hourly", "alerts"],
        lang=language,
        units=units
    )

def get_hourly_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения почасового прогноза на 48 часов"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=["current", "daily", "minutely", "alerts"],
        lang=language,
        units=units
    )

def get_all_weather_request(api_key: str, lat: float, lon: float) -> WeatherRequest:
    """Создает запрос для получения всей доступной информации о погоде"""
    return WeatherRequest(
        api_key=api_key,
        lat=lat,
        lon=lon,
        exclude=None,
        lang=language,
        units=units
    )
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Dict, Any
from enum import Enum

# Перечисление для единиц измерения
class Units(str, Enum):
    STANDARD = "standard"
    METRIC = "metric"
    IMPERIAL = "imperial"

# Перечисление для языков
class Language(str, Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"
    GERMAN = "de"
    FRENCH = "fr"
    SPANISH = "es"

# Модель для запроса погоды
class WeatherRequest(BaseModel):
    api_key: str = Field(..., description="API ключ для доступа к OpenWeatherMap")
    lat: float = Field(..., ge=-90, le=90, description="Широта")
    lon: float = Field(..., ge=-180, le=180, description="Долгота")
    exclude: Optional[List[str]] = Field(None, description="Исключаемые части ответа")
    lang: Optional[Language] = Field(Language.RUSSIAN, description="Язык ответа")
    units: Optional[Units] = Field(Units.METRIC, description="Единицы измерения")

    @field_validator('exclude')
    @classmethod
    def validate_exclude(cls, v):
        if v is not None:
            valid_excludes = {'current', 'minutely', 'hourly', 'daily', 'alerts'}
            for item in v:
                if item not in valid_excludes:
                    raise ValueError(f'Invalid exclude item: {item}')
        return v

# Модель для координат
class Coordinates(BaseModel):
    lat: float = Field(..., description="Широта")
    lon: float = Field(..., description="Долгота")

# Модель для описания погоды
class WeatherDescription(BaseModel):
    id: int = Field(..., description="Идентификатор погодных условий")
    main: str = Field(..., description="Группа параметров (Rain, Snow, Clouds и т.д.)")
    description: str = Field(..., description="Текстовое описание погоды")
    icon: str = Field(..., description="Идентификатор иконки")

# Модель основных метеорологических данных
class MainData(BaseModel):
    temp: float = Field(..., description="Температура")
    feels_like: float = Field(..., description="Ощущаемая температура")
    temp_min: float = Field(..., description="Минимальная температура")
    temp_max: float = Field(..., description="Максимальная температура")
    pressure: int = Field(..., description="Атмосферное давление (гПа)")
    humidity: float = Field(..., description="Влажность (%)")
    sea_level: Optional[int] = Field(None, description="Давление на уровне моря")
    grnd_level: Optional[int] = Field(None, description="Давление на уровне земли")

# Модель данных о ветре
class WindData(BaseModel):
    speed: float = Field(..., description="Скорость ветра")
    deg: float = Field(..., description="Направление ветра в градусах")  # Исправлено deq -> deg

# Модель системных данных
class SysData(BaseModel):
    id: Optional[int] = Field(None, description="Идентификатор системы")
    country: str = Field(..., description="Код страны")
    sunrise: int = Field(..., description="Время восхода (Unix timestamp)")
    sunset: int = Field(..., description="Время заката (Unix timestamp)")
    type: Optional[int] = Field(None, description="Тип системы")

# Модель для ответа о текущей погоде
class CurrentWeatherResponse(BaseModel):
    name: str = Field(..., description="Название местоположения")
    timezone: int = Field(..., description="Смещение времени от UTC в секундах")
    coord: Coordinates = Field(..., description="Координаты местоположения")
    main: MainData = Field(..., description="Основные метеорологические данные")
    weather: List[WeatherDescription] = Field(..., description="Описание погодных условий")
    wind: WindData = Field(..., description="Данные о ветре")
    sys: SysData = Field(..., description="Системные данные")
    dt: int = Field(..., description="Время расчета данных (Unix timestamp)")
    visibility: Optional[int] = Field(None, description="Видимость (метры)")
    clouds: Optional[Dict[str, Any]] = Field(None, description="Данные об облачности")
    pop: Optional[float] = Field(None, description="Вероятность осадков")

# Модель для дневной температуры в недельном прогнозе
class DailyTemperature(BaseModel):
    day: float = Field(..., description="Дневная температура")
    min: float = Field(..., description="Минимальная температура")
    max: float = Field(..., description="Максимальная температура")
    night: float = Field(..., description="Ночная температура")
    eve: float = Field(..., description="Температура вечером")
    morn: float = Field(..., description="Температура утром")

# Модель для дневного прогноза
class DailyForecast(BaseModel):
    dt: int = Field(..., description="Время прогноза (Unix timestamp)")
    sunrise: Optional[int] = Field(None, description="Время восхода (Unix timestamp)")
    sunset: Optional[int] = Field(None, description="Время заката (Unix timestamp)")
    temp: DailyTemperature = Field(..., description="Температурные данные")
    feels_like: Optional[Dict[str, float]] = Field(None, description="Ощущаемая температура")
    pressure: int = Field(..., description="Атмосферное давление (гПа)")
    humidity: int = Field(..., description="Влажность (%)")
    weather: List[WeatherDescription] = Field(..., description="Погодные условия")
    speed: float = Field(..., description="Скорость ветра")
    deg: float = Field(..., description="Направление ветра в градусах")
    gust: Optional[float] = Field(None, description="Порывы ветра")
    clouds: int = Field(..., description="Облачность (%)")
    pop: float = Field(..., description="Вероятность осадков")
    rain: Optional[float] = Field(None, description="Количество осадков (мм)")
    snow: Optional[float] = Field(None, description="Количество снега (мм)")
    uvi: Optional[float] = Field(None, description="УФ-индекс")

# Модель для ответа о недельном прогнозе
class WeeklyWeatherResponse(BaseModel):
    lat: float = Field(..., description="Широта")
    lon: float = Field(..., description="Долгота")
    timezone: str = Field(..., description="Часовой пояс")
    timezone_offset: int = Field(..., description="Смещение времени от UTC в секундах")
    daily: List[DailyForecast] = Field(..., description="Дневные прогнозы на 7 дней")

# Универсальная модель ответа API
class APIResponse(BaseModel):
    success: bool = Field(True, description="Успешность выполнения запроса")
    data: Optional[Any] = Field(None, description="Данные ответа")
    error: Optional[str] = Field(None, description="Сообщение об ошибке")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Метаданные ответа")
import argparse
from argument_types import lat, lon

# Создает парсер для аргументов командной строки
def create_parser():
    parser = argparse.ArgumentParser(
        description='Приложение для получения  погоды в указанном городе',
        epilog='Пример использования: python weather.py --city Новосибирск --units metric'
    )

    parser.add_argument(
        '--lat',
        type=lat,
        help='Широта'
    )

    parser.add_argument(
        '--lon',
        type=lon,
        help='Долгота'
    )

    return parser












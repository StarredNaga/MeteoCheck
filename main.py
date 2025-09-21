import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description='Приложение для получения  погоды в указанном городе',
        epilog='Пример использования: python weather.py --city Новосибирск --units metric'
    )

    parser.add_argument(
        '--city',
        '-c',
        type=str,
        required=True,
        help='Название города для получения погоды'
    )

    return parser












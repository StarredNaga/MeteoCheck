from argparse import ArgumentError


def lat(inpt : str) -> float:

    latitude = float(inpt)

    if not (-90 < latitude < 90): raise ArgumentError('Incorrect latitude data')

    return latitude

def lon(inpt: str) -> float:

    longitude = float(inpt)

    if not (-180 < longitude < 180): raise ArgumentError('Incorrect longitude data')

    return longitude

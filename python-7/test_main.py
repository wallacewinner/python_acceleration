import pytest
from main import get_temperature


def get_temperature_by_lat_lng(temperature):
    if not temperature:
        return
    return int((temperature - 32) * 5.0 / 9.0)

def teste_temperature_is_sixteen():
    temperature = 62
    resp = get_temperature_by_lat_lng(temperature)
    assert resp == 16

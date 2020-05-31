import pytest
from main import get_temperature

temperature_positive = [
    (62, 16),
    (67, 19),
]

temperature_negative = [
    (20, -6),
    (33, 0)
]

def get_temperature_by_lat_lng(temperature):
    if not temperature:
        return
    return int((temperature - 32) * 5.0 / 9.0)

@pytest.mark.parametrize('temperature, expected', temperature_positive)
def test_temperature_is_positive(temperature, expected):
    resp = get_temperature_by_lat_lng(temperature)
    assert resp == expected

@pytest.mark.parametrize('temperature, expected', temperature_negative)
def test_temperature_is_negative(temperature, expected):
    resp = get_temperature_by_lat_lng(temperature)
    assert resp == expected

@pytest.mark.parametrize('temperature, expected', [('', None)])
def test_temperature_is_error(temperature, expected):
    resp = get_temperature_by_lat_lng(temperature)
    assert resp == expected

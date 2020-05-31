import pytest
from main import get_temperature

def get_temperature_by_lat_lng(temperature):
    if not temperature:
        return
    return int((temperature - 32) * 5.0 / 9.0)

@pytest.mark.parametrize('temperature, expected', [(62, 16)])
def test_temperature_is_sixteen(temperature, expected):
    resp = get_temperature_by_lat_lng(temperature)
    assert resp == expected

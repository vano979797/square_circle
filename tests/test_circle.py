import pytest
import math

from geometry.circle import Circle


def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)

def test_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)

def test_radius_less_than_zero():
    with pytest.raises(ValueError):
        Circle(-0.1)

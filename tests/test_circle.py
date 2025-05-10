import pytest
from geometry.circle import Circle
import math

def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)

def test_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)

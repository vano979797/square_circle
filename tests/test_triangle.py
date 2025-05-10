import pytest
from geometry.triangle import Triangle
import math

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
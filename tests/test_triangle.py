import pytest
import math

from geometry.triangle import Triangle


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)

def test_invalid_triangle_zero_side():
    with pytest.raises(ValueError,
                       match="Стороны должны быть положительными."):
        Triangle(0, 4, 5)

def test_invalid_triangle_negative_side():
    with pytest.raises(ValueError,
                       match="Стороны должны быть положительными."):
        Triangle(-3, 4, 5)

def test_invalid_triangle_sum_violation():
    with pytest.raises(ValueError,
                       match="Невалидные стороны."):
        Triangle(1, 2, 3)

import math

from .calculation import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = sorted([a, b, c])
        if any(side <= 0 for side in sides):
            raise ValueError("Стороны должны быть положительными.")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Невалидные стороны.")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return math.isclose(self.a ** 2 + self.b ** 2, self.c ** 2)

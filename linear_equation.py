import math
from point import Point


class LinearEquation(object):
    def __init__(self, A: float, B: float, C: float, name: str = ""):
        assert A != 0 or B != 0
        self.A = A
        self.B = B
        self.C = C
        self.name = name

    def __repr__(self):
        flag_1 = "" if self.A >= 0 else "-"
        flag_2 = "+" if self.B >= 0 else "-"
        flag_3 = "+" if self.C > 0 else ""
        s = "{0.__class__.__name__} {0.name}: ".format(self) + flag_1
        if self.A != 1 and self.A != -1:
            s += str(self.A)
        s += "x " + flag_2
        if self.B != 1 and self.B != -1:
            s += str(self.B)
        s += " y " + flag_3
        if self.C != 0:
            s += str(self.C)
        s += " = 0"
        return s

    def point_on_line(self, point: Point) -> bool:
        return self.A * point.x + self.B * point.y + self.C == 0

    def distance_of_point(self, point: Point) -> float:
        return abs(self.A * point.x + self.B * point.y + self.C) / math.sqrt(self.A ** 2 + self.B ** 2)

    @property
    def slope(self):
        if self.B == 0:
            return math.inf
        return -self.A / self.B

    @property
    def intercept_y(self):
        assert self.B != 0
        return -self.C / self.B

    @property
    def intercept_x(self):
        assert self.A != 0
        return -self.C / self.A

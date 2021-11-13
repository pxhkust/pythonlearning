from linear_equation import LinearEquation
from point import Point
import math


class LaneSegment(object):
    def __init__(self, begin: Point, end: Point, name: str = ""):
        assert begin.x != end.x or begin.y != end.y
        self.begin = begin
        self.end = end
        self.name = name

    def __repr__(self):
        return "{0.__class__.__name__} {0.name}: ({0.begin}, {0.end})".format(self)

    @property
    def length(self) -> float:
        return math.sqrt((self.end.x - self.begin.x)**2 + (self.end.y - self.begin.y)**2)

    @property
    def slope(self) -> float:
        if self.begin.x == self.end.x:
            return math.inf
        else:
            return (self.end.y - self.begin.y) / (self.end.x - self.begin.x)

    @property
    def middle_point(self) -> Point:
        return Point((self.begin.x + self.end.x)/2, (self.begin.y + self.end.y)/2)

    def to_linear_equation(self) -> LinearEquation:
        return LinearEquation(self.end.y - self.begin.y,
                              self.begin.x - self.end.x,
                              self.end.x * self.begin.y - self.begin.x * self.end.y)

    def point_to_distance(self, point: Point) -> float:
        return self.to_linear_equation().distance_of_point(point)



from point import Point
from ploygon import Ploygon
from typing import List
import math


class Square(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)

    @property
    def side(self) -> float:
        side_distance = (self.points[0].x - self.center.x) ** 2 + \
                        (self.points[0].y - self.center.y) ** 2
        return math.sqrt(2 * side_distance)

    @property
    def perimeter(self) -> float:
        return 4 * self.side

    @property
    def area(self) -> float:
        return self.side ** 2


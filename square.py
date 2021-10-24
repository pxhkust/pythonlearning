from point import Point
from ploygon import Ploygon
from typing import List
import math


class Square(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)

    @property
    def side(self) -> float:
        return math.sqrt((self.points[0].x - self.points[1].x) ** 2 +
                         (self.points[0].y - self.points[1].y) ** 2)


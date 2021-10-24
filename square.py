from point import Point
from ploygon import Ploygon
from lane_segment import LaneSegment
from typing import List
import math


class Square(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    @property
    def side(self) -> float:
        line_segment = LaneSegment(self.points[0], self.center)
        return math.sqrt(2) * line_segment.length

    @property
    def perimeter(self) -> float:
        return 4 * self.side

    @property
    def area(self) -> float:
        return self.side ** 2


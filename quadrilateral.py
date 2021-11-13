import math
from point import Point
from ploygon import Ploygon
from lane_segment import LaneSegment
from typing import List


class Quadrilateral(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        assert len(points) == 4
        super(Quadrilateral, self).__init__(points, name)
        self.line_1 = LaneSegment(self.convex_hull[0], self.convex_hull[1])
        self.line_2 = LaneSegment(self.convex_hull[1], self.convex_hull[2])
        self.line_3 = LaneSegment(self.convex_hull[2], self.convex_hull[3])
        self.line_4 = LaneSegment(self.convex_hull[3], self.convex_hull[0])

    @property
    def area(self) -> float:
        return math.sqrt((self.perimeter / 2 - self.line_1.length) *
                         (self.perimeter / 2 - self.line_2.length) *
                         (self.perimeter / 2 - self.line_3.length) *
                         (self.perimeter / 2- self.line_4.length))

    @property
    def perimeter(self) -> float:
        return self.line_1.length + self.line_2.length + self.line_3.length + self.line_4.length

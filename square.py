from point import Point
from rectangle import Rectangle
from lane_segment import LaneSegment
from typing import List
import math


class Square(Rectangle):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)
        assert(self.__is_valid())

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    def __is_valid(self) -> bool:
        if self.cross_line_1.length != self.cross_line_2.length:
            return False
        if self.cross_line_1.slope == math.inf and self.cross_line_2.slope == 0:
            return True
        if self.cross_line_2.slope == math.inf and self.cross_line_1.slope == 0:
            return True
        return self.cross_line_1.slope * self.cross_line_2.slope == -1

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



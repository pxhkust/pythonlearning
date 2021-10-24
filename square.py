from point import Point
from ploygon import Ploygon
from lane_segment import LaneSegment
from typing import List
import math


class Square(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)
        assert(self.__is_valid())

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    def __is_valid(self) -> bool:
        if len(self) != 4:
            return False
        sorted_points = self.sorted_by_x_and_y()
        line_1 = LaneSegment(sorted_points[0], sorted_points[1])
        line_2 = LaneSegment(sorted_points[1], sorted_points[3])
        line_3 = LaneSegment(sorted_points[3], sorted_points[2])
        line_4 = LaneSegment(sorted_points[2], sorted_points[0])
        if line_1.length != line_2.length:
            return False
        if line_2.length != line_3.length:
            return False
        if line_3.length != line_4.length:
            return False
        if line_4.length != line_1.length:
            return False
        cross_line_1 = LaneSegment(sorted_points[0], sorted_points[3])
        cross_line_2 = LaneSegment(sorted_points[1], sorted_points[2])
        if cross_line_1.length != cross_line_2.length:
            return False
        return True

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


from point import Point
from ploygon import Ploygon
from lane_segment import LaneSegment
from typing import List
import math


class Square(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        assert len(points) == 4
        super(Square, self).__init__(points, name)
        assert(self.__is_valid())

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    def __is_valid(self) -> bool:
        sorted_points = self.sorted_by_x_and_y()
        LaneSegment(sorted_points[0], sorted_points[1])
        LaneSegment(sorted_points[1], sorted_points[3])
        LaneSegment(sorted_points[3], sorted_points[2])
        LaneSegment(sorted_points[2], sorted_points[0])

        cross_line_1 = LaneSegment(sorted_points[0], sorted_points[3])
        cross_line_2 = LaneSegment(sorted_points[1], sorted_points[2])
        if cross_line_1.length != cross_line_2.length:
            return False
        if cross_line_1.slope == math.inf and cross_line_2.slope == 0:
            return True
        if cross_line_2.slope == math.inf and cross_line_1.slope == 0:
            return True
        return cross_line_1.slope * cross_line_2.slope == -1

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



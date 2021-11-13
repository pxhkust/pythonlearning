from point import Point
from ploygon import Ploygon
from lane_segment import LaneSegment
from spatial_relationship import segment_vertical_to_segment
from typing import List


class Rectangle(Ploygon):
    def __init__(self, points: List[Point], name: str = ""):
        assert len(points) == 4
        super(Rectangle, self).__init__(points, name)
        sorted_points = self.sorted_by_x_and_y()
        self.line_1 = LaneSegment(sorted_points[0], sorted_points[1])
        self.line_2 = LaneSegment(sorted_points[1], sorted_points[3])
        self.line_3 = LaneSegment(sorted_points[3], sorted_points[2])
        self.line_4 = LaneSegment(sorted_points[2], sorted_points[0])
        self.cross_line_1 = LaneSegment(sorted_points[0], sorted_points[3])
        self.cross_line_2 = LaneSegment(sorted_points[1], sorted_points[2])
        assert self.__is_valid()

    def __is_valid(self) -> bool:
        if self.line_1.length != self.line_3.length or self.line_2.length != self.line_4.length:
            return False
        return segment_vertical_to_segment(self.line_1, self.line_2)


    @property
    def length(self) -> float:
        return max(self.line_1.length, self.line_2.length)

    @property
    def width(self) -> float:
        return min(self.line_1.length, self.line_2.length)

    @property
    def area(self) -> float:
        return self.line_1.length * self.line_2.length

    @property
    def perimeter(self) -> float:
        return (self.line_1.length + self.line_2.length) * 2









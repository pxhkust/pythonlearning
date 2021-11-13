from point import Point
from lane_segment import LaneSegment
from quadrilateral import Quadrilateral
from spatial_relationship import segment_parallel_and_equal_to_segment
from typing import List


class Parallelogram(Quadrilateral):
    def __init__(self, points: List[Point], name: str = ""):
        super(Parallelogram, self).__init__(points, name)
        self.cross_line_1 = LaneSegment(self.convex_hull[0], self.convex_hull[3])
        self.cross_line_2 = LaneSegment(self.convex_hull[1], self.convex_hull[2])
        assert self.__is_valid()
        if self.line_1.length < self.line_2.length:
            self.line_1, self.line_2 = self.line_2, self.line_1
            self.line_3, self.line_4 = self.line_4, self.line_3

    def __is_valid(self) -> bool:
        return segment_parallel_and_equal_to_segment(self.line_1, self.line_3) and \
               segment_parallel_and_equal_to_segment(self.line_2, self.line_4)

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    @property
    def length(self) -> float:
        return self.line_1.length

    @property
    def width(self) -> float:
        return self.line_2.length

    @property
    def height_of_length(self) -> float:
        return self.line_1.point_to_distance(self.find_corner_point(self.line_1.begin))

    @property
    def height_of_width(self) -> float:
        return self.line_2.point_to_distance(self.find_corner_point(self.line_2.begin))
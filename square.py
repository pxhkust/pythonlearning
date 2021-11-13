from point import Point
from rectangle import Rectangle
from spatial_relationship import segment_vertical_and_equal_to_segment
from typing import List


class Square(Rectangle):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)
        assert self.__is_valid()

    def find_corner_point(self, point: Point) -> Point:
        return Point(self.center.x * 2 - point.x, self.center.y * 2 - point.y)

    def __is_valid(self) -> bool:
        return segment_vertical_and_equal_to_segment(self.cross_line_1, self.cross_line_2)

    @property
    def side(self) -> float:
        return self.length

    @property
    def perimeter(self) -> float:
        return 4 * self.side

    @property
    def area(self) -> float:
        return self.side ** 2



from point import Point
from rectangle import Rectangle
from spatial_relationship import segment_vertical_to_segment
from typing import List


class Square(Rectangle):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)
        assert self.__is_valid()

    def __is_valid(self) -> bool:
        return segment_vertical_to_segment(self.cross_line_1, self.cross_line_2)

    @property
    def side(self) -> float:
        return self.length
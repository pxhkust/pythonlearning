from parallelogram import Parallelogram
from point import Point
from spatial_relationship import segment_vertical_to_segment
from typing import List


class Rectangle(Parallelogram):
    def __init__(self, points: List[Point], name: str = ""):
        super(Rectangle, self).__init__(points, name)
        assert self.__is_valid()

    def __is_valid(self) -> bool:
        return segment_vertical_to_segment(self.line_1, self.line_2)

    @property
    def area(self) -> float:
        return self.line_1.length * self.line_2.length
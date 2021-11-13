from parallelogram import Parallelogram
from point import Point
from typing import List


class Diamond(Parallelogram):
    def __init__(self, points: List[Point], name: str = ""):
        super(Diamond, self).__init__(points, name)
        assert self.__is_valid()

    def __is_valid(self) -> bool:
        return self.line_1.length == self.line_2.length
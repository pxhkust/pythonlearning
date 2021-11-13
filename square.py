from diamond import Diamond
from point import Point
from rectangle import Rectangle
from spatial_relationship import segment_vertical_to_segment
from typing import List


class Square(Rectangle, Diamond):
    def __init__(self, points: List[Point], name: str = ""):
        super(Square, self).__init__(points, name)

    @property
    def side(self) -> float:
        return self.length
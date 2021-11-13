from point import Point
from lane_segment import LaneSegment
from quadrilateral import Quadrilateral
from spatial_relationship import segment_parallel_to_segment
from typing import List


class Trapezoid(Quadrilateral):
    def __init__(self, points: List[Point], name: str = ""):
        super(Trapezoid, self).__init__(points, name)
        self.lower_line, self.upper_line = None, None
        assert self.__is_valid()

    def __classify_upper_and_lower_line(self, lines: List[LaneSegment]) -> bool:
        assert len(lines) == 4
        if not segment_parallel_to_segment(lines[1], lines[3]) and segment_parallel_to_segment(lines[0], lines[2]):
            if lines[0].length > lines[2].length:
                self.upper_line = lines[0]
                self.lower_line = lines[2]
            else:
                self.upper_line = lines[2]
                self.lower_line = lines[0]
            return True
        return False

    def __is_valid(self) -> bool:
        flag_1 = self.__classify_upper_and_lower_line([self.line_1, self.line_2, self.line_3, self.line_4])
        flag_2 = self.__classify_upper_and_lower_line([self.line_2, self.line_1, self.line_4, self.line_3])
        return flag_1 + flag_2 == 1

    @property
    def height(self) -> float:
        return self.lower_line.point_to_distance(self.upper_line.begin)
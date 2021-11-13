from lane_segment import LaneSegment
import math


def segment_vertical_to_segment(line_1: LaneSegment, line_2: LaneSegment) -> bool:
    if line_1.slope == math.inf and line_2.slope == 0:
        return True
    if line_2.slope == math.inf and line_1.slope == 0:
        return True
    return line_1.slope * line_2.slope == -1


def segment_vertical_and_equal_to_segment(line_1: LaneSegment, line_2: LaneSegment) -> bool:
    return line_1.length == line_2.length and segment_vertical_to_segment(line_1, line_2)



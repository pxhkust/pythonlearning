from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment


def main():
    point_A = Point(0, 0, "A")
    point_B = Point(1, 1, "B")
    point_C = Point(0, 0, "C")
    point_D = Point(1, 1, "D")
    square = Square([point_A, point_B, point_C, point_D])


if __name__ == '__main__':
    main()

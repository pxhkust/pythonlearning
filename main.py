from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment


def main():
    point_A = Point(1, 1, "A")
    point_B = Point(0, 0, "B")
    point_C = Point(0, 2, "C")
    point_D = Point(-1, 1, "D")
    square_ABCD = Square([point_A, point_B, point_C, point_D], "ABCD")


if __name__ == '__main__':
    main()

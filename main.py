from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment


def main():
    point_A = Point(x=1, y=1, name="A")
    point_B = Point(x=0, y=0, name="B")
    point_C = Point(x=0, y=2, name="C")
    point_D = Point(x=-1, y=1, name="D")
    square_ABCD = Square([point_A, point_B, point_C, point_D], "ABCD")


if __name__ == '__main__':
    main()

from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment


def main():
    point_A = Point(x=1.0, y=1.0, name="A")
    point_B = Point(x=3.0, y=1.0, name="B")
    point_C = Point(x=3.0, y=3.0, name="C")
    point_D = Point(x=1.0, y=3.0, name="D")
    square_ABCD = Square([point_A, point_B, point_C, point_D], "ABCD")
    print(square_ABCD)
    print(square_ABCD.side)


if __name__ == '__main__':
    main()

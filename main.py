from ploygon import Ploygon
from point import Point
from lane_segment import LaneSegment


def main():
    point_A = Point(x=1.0, y=3.0, name="A")
    point_B = Point(x=3.0, y=1.0, name="B")
    point_C = Point(x=1.0, y=3.0, name="C")
    point_D = Point(x=3.0, y=3.0, name="D")
    lane_AB = LaneSegment(begin=point_A, end=point_B, name="AB")
    ploygon_ABCD = Ploygon([point_A, point_B, point_C, point_D], name="ABCD")
    print(ploygon_ABCD.sorted_by_x_and_y())
    square_ACBD = Square([point_A, point_B, point_C, point_D], name="ACBD")
    square_meter = meter()
    print(square_meter)


if __name__ == '__main__':
    main()

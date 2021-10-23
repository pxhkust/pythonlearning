from ploygon import Ploygon
from point import Point
from lane_segment import LaneSegment


def main():
    point_A = Point(x=1.1, y=2.4, name="A")
    point_B = Point(x=2.2, y=3.7, name="B")
    point_C = Point(x=2.4, y=9.0, name="C")
    lane_AB = LaneSegment(begin=point_A, end=point_B, name="AB")
    polygon_ABC = Ploygon([point_A, point_B, point_C], name="ABC")
    print(polygon_ABC)
    print(len(polygon_ABC))
    print(polygon_ABC.center)
    print(polygon_ABC[1])
    print(polygon_ABC[:2])


if __name__ == '__main__':
    main()

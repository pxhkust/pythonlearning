from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment
from rectangle import Rectangle


def main():
    point_A = Point(0, 0, "A")
    point_B = Point(1, 2, "B")
    point_C = Point(3, 1, "C")
    point_D = Point(2, -1, "D")
    # segment = LaneSegment(point_A, point_B)
    rectangle = Square([point_A, point_B, point_C, point_D])
    print(rectangle)
    print(rectangle.side)
    print(rectangle.length)
    print(rectangle.width)
    print(rectangle.area)
    print(rectangle.perimeter)



if __name__ == '__main__':
    main()

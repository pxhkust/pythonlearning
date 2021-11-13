from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment
from rectangle import Rectangle


def main():
    point_A = Point(0, 0, "A")
    point_B = Point(2, 0, "B")
    point_C = Point(0, 1, "C")
    point_D = Point(2, 1, "D")
    # segment = LaneSegment(point_A, point_B)
    rectangle = Rectangle([point_A, point_B, point_C, point_D])
    print(rectangle)
    print(rectangle.length)
    print(rectangle.width)
    print(rectangle.area)
    print(rectangle.perimeter)



if __name__ == '__main__':
    main()

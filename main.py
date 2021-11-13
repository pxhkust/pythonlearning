from ploygon import Ploygon
from point import Point
from square import Square
from lane_segment import LaneSegment
from rectangle import Rectangle
from spatial_relationship import segment_to_linear_equation
from parallelogram import Parallelogram


def main():
    point_A = Point(0, 0, "A")
    point_B = Point(2, 0, "B")
    point_C = Point(0, 2, "C")
    point_D = Point(2, 2, "D")
    square = Square([point_A, point_B, point_D, point_C])
    print(square)
    print(square.area)

if __name__ == '__main__':
    main()

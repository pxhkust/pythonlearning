from point import Point
from square import Square


def main():
    point_A = Point(0, 0, "A")
    point_B = Point(3, 0, "B")
    point_C = Point(0, 3, "C")
    point_D = Point(3, 3, "D")
    square = Square([point_A, point_B, point_D, point_C])
    print(square)
    print(square.area)


if __name__ == '__main__':
    main()

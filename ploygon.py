from point import Point
from typing import List


class Ploygon(object):
    def __init__(self, points: List[Point], name: str = ""):
        self.points = points
        self.name = name

    def __repr__(self):
        return "Ploygon {0.name}: {0.points}".format(self)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]

    @property
    def center(self) -> Point:
        center_x, center_y = 0, 0
        for point in self:
            center_x += point.x
            center_y += point.y
        return Point(center_x/len(self),
                     center_y/len(self))

    def sorted_by_x_and_y(self) -> List[Point]:
        return sorted(self.points, key=lambda point: [point.x, point.y])

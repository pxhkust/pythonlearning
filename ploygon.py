from point import Point
from typing import List
from scipy.spatial import ConvexHull


class Ploygon(object):
    def __init__(self, points: List[Point], name: str = ""):
        self.points = points
        self.name = name

    def __repr__(self):
        return "{0.__class__.__name__} {0.name}: {0.points}".format(self)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]

    @property
    def convex_hull(self) -> List[Point]:
        indexes: List[int] = ConvexHull([(point.x, point.y) for point in self.points]).vertices.tolist()
        return [self.points[index] for index in indexes]

    @property
    def center(self) -> Point:
        center_x, center_y = 0, 0
        for point in self:
            center_x += point.x
            center_y += point.y
        return Point(center_x/len(self),
                     center_y/len(self))

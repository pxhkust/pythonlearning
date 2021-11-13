class Point(object):
    def __init__(self, x: float, y: float, name: str = ""):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return "{0.__class__.__name__} {0.name}: ({0.x:.4f}, {0.y:.4f})".format(self)

from ploygon import Ploygon
from typing import List
import math

#问题关键在于Square怎么继承Ploygon的结果

class Square(Ploygon):
    # 还需要初始化Square吗？
    # 没找到怎么继承父辈的结果的写法？

    @property
    def meter(self) -> float:
        return math.sqrt((self.Ploygon.Point.begin.x - self.Ploygon.Point.end.x) ** 2 + (self.Ploygon.Point.begin.y - self.Ploygon.Point.end.y) ** 2)


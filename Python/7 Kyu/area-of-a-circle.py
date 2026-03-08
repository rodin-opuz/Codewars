import math
def circle_area(r):
    if r <= 0:
        raise ValueError
    return math.pi * r ** 2

from math import acos, pi, hypot
from itertools import combinations

def distance(a, b):

    x1, y1, _ = a
    x2, y2, _ = b

    return hypot(x1 - x2, y1 - y2)


def area(r):
    return pi*r**2


def intersection_area(a, b, d):
    r1, r2 = a[-1], b[-1]
    if r1 + r2 <= d:
        return 0
    if r1 > d + r2:
        return area(r2)

    s = (2*d*r1)**2 - (d**2 + r1**2 - r2**2)**2
    d1 = (d**2 + r1**2 - r2**2)/(2*d*r1)
    d2 = (d**2 + r2**2 - r1**2)/(2*d*r2)

    return r1**2*acos(d1) + r2**2*acos(d2) - 0.5*s**0.5


def checkio(data):

    holes = [list(hole) for hole in data]

    while True:
        pairs = sorted((distance(a, b), a, b) for a, b in  combinations(holes, 2))
        for d, a, b in pairs:
            pair = sorted((a, b), key=lambda x: x[-1])
            inter = intersection_area(pair[1], pair[0], distance(*pair))
            if inter >= area(pair[0][-1]) * 0.55 and area(pair[1][-1]) > area(pair[0][-1]) * 1.2:
                pair[1][2] = round(((area(pair[1][-1]) + area(pair[0][-1]))/pi)**0.5, 2)
                holes.remove(pair[0])
                break
        else:
            break

    return [(x, y, r) for (x, y, r) in holes]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]

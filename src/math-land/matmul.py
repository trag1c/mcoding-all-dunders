from collections import namedtuple
from dataclasses import dataclass

Point = namedtuple("Point", ["x", "y"])


@dataclass(slots=True)
class Line:
    p_i: Point
    p_j: Point

    def __matmul__(self, other):
        x1, y1 = self.p_i
        x2, y2 = self.p_j
        x3, y3 = other.p_i
        x4, y4 = other.p_j

        t = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        t /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        Px = x1 + t * (x2 - x1)
        Py = y1 + t * (y2 - y1)

        if not 0 <= t <= 1:
            print("Intersection out of lines")
            return None

        else:
            return Point(Px, Py)

    def __truediv__(self, other):
        intersection = self @ other

        if intersection:
            return (
                Line(self.p_i, intersection),
                Line(intersection, self.p_j),
                Line(other.p_i, intersection),
                Line(intersection, other.p_j),
            )


def main():
    diagonal_up = Line(
        Point(0, 0),
        Point(1, 1),
    )

    diagonal_down = Line(
        Point(0, 1),
        Point(1, 0),
    )

    print(diagonal_down @ diagonal_up)

    print(*(diagonal_down / diagonal_up), sep="\n")


if __name__ == "__main__":
    main()

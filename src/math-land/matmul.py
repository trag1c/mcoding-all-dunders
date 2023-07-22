from collections import namedtuple
from dataclasses import dataclass

Point = namedtuple("Point", ["x", "y"])


@dataclass(slots=True)
class Line:
    p_i: Point
    p_j: Point

    def __matmul__(self, other):
        """Calculate the intersection between two line segments given two
        points on each line segment. Formula extracted from:
        https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        """

        ## Keeping notation from formula
        x1, y1, x2, y2 = *self.p_i, *self.p_j
        x3, y3, x4, y4 = *other.p_i, *other.p_j

        t = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)

        try:
            t /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        except ZeroDivisionError:
            print("Lines are parallel")
            return None

        Px = x1 + t * (x2 - x1)
        Py = y1 + t * (y2 - y1)

        if not 0 <= t <= 1:
            print("Intersection not within line segments")
            return None

        else:
            print("Intersection was found :D")
            return Point(Px, Py)

    # def __truediv__(self, other):
    #     """Division of two line segments results in four line segments"""

    #     intersection = self @ other

    #     if intersection:
    #         return (
    #             Line(self.p_i, intersection),
    #             Line(intersection, self.p_j),
    #             Line(other.p_i, intersection),
    #             Line(intersection, other.p_j),
    #         )


def main():

    ## Diagonal lines
    up_right = Line(
        Point(0, 0),
        Point(1, 1),
    )

    down_right = Line(
        Point(0, 1),
        Point(1, 0),
    )

    print(up_right @ down_right)

    ## Non-intersecting lines
    up_but_away = Line(
        Point(2, 2),
        Point(2, 4),
    )

    print(up_right @ up_but_away)

    ## Parallel lines

    up_right_parallel = Line(
        Point(1, 0),
        Point(2, 1),
    )

    print(up_right @ up_right_parallel)

    ## Overlaping lines
    up_right_overlap = Line(
        Point(0.5, 0.5),
        Point(1.5, 1.5),
    )

    print(up_right @ up_right_overlap)

if __name__ == "__main__":
    main()

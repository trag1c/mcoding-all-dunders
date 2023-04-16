from math import sqrt
from typing import Self

class Vector():
    """
    2D vector with an x- and a y-component.
    Comparisons between vectors are based on their magnitude
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.mag = sqrt(self.x**2 + self.y**2)

    def __ge__(self, other: Self) -> bool:
        """Greater or equal than comparison"""
        if isinstance(other, Vector):
            return self.mag >= other.mag
        else:
            return self.mag >= other

    def __gt__(self, other: Self) -> bool:
        """Greater than comparison"""
        if isinstance(other, Vector):
            return self.mag > other.mag
        else:
            return self.mag > other

    def __le__(self, other: Self) -> bool:
        """Less or equal than comparison"""
        if isinstance(other, Vector):
            return self.mag <= other.mag
        else:
            return self.mag <= other

    def __lt__(self, other: Self) -> bool:
        """Less than comparison"""
        if isinstance(other, Vector):
            return self.mag < other.mag
        else:
            return self.mag < other

    def __eq__(self, other: Self) -> bool:
        """Equal comparison"""
        if isinstance(other, Vector):
            return self.mag == other.mag
        else:
            return self.mag == other

    def __ne__(self, other: Self) -> bool:
        return not self == other


if __name__ == "__main__":

    print("""Define three vectors a,b and c, such that
    |a| < |b|
    |a| = |c|
    |a| = √2
    """)

    a = Vector(1, 1)
    b = Vector(2, 1)
    c = Vector(-1, -1)

    print("\nPrint their magnitudes")
    print(f"|a| = {a.mag:.5f}")
    print(f"|b| = {b.mag:.5f}")
    print(f"|c| = {c.mag:.5f}")

    print("\nGreater or equal than")
    print(f"a ≥ b  \t {a >= b}")       # False
    print(f"a ≥ c  \t {a >= c}")       # True
    print(f"a ≥ √2 \t {a >= sqrt(2)}") # True

    print("\nGreater than")
    print(f"a > b  \t {a > b}")        # False
    print(f"a > c  \t {a > c}")        # False
    print(f"a > √2 \t {a > sqrt(2)}")  # False

    print("\nLess or equal than")
    print(f"a ≤ b  \t {a <= b}")       # True
    print(f"a ≤ c  \t {a <= c}")       # True
    print(f"a ≤ √2 \t {a <= sqrt(2)}") # True

    print("\nLess than")
    print(f"a < b  \t {a < b}")        # True
    print(f"a < c  \t {a < c}")        # False
    print(f"a < √2 \t {a < sqrt(2)}")  # False

    print("\nEqual than")
    print(f"a = b  \t {a == b}")       # False
    print(f"a = c  \t {a == c}")       # True
    print(f"a = √2 \t {a == sqrt(2)}") # True

    print("\nNot equal than")
    print(f"a ≠ b  \t {a != b}")       # True
    print(f"a ≠ c  \t {a != c}")       # False
    print(f"a ≠ √2 \t {a != sqrt(2)}") # False

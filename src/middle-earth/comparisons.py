from math import hypot, isclose, sqrt
from typing import Any


class Force:
    """
    2D force with an x- and a y-component.
    Comparisons between forces are based on their magnitude.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def mag(self) -> float:
        return hypot(self.x, self.y)

    @staticmethod
    def _get_mag(other: Any) -> Any:
        return other.mag if isinstance(other, Force) else other

    def __ge__(self, other: Any) -> bool:
        """Greater or equal than comparison"""
        return self.mag >= self._get_mag(other)

    def __gt__(self, other: Any) -> bool:
        """Greater than comparison"""
        return self.mag > self._get_mag(other)

    def __le__(self, other: Any) -> bool:
        """Less or equal than comparison"""
        return self.mag <= self._get_mag(other)

    def __lt__(self, other: Any) -> bool:
        """Less than comparison"""
        return self.mag < self._get_mag(other)

    def __eq__(self, other: Any) -> bool:
        """Equal comparison"""
        return isclose(self.mag, self._get_mag(other))

    def __ne__(self, other: Any) -> bool:
        """Not equal comparison"""
        return not self == self._get_mag(other)


if __name__ == "__main__":
    print(
        """Define three forces (a, b and c), such that

    |a| < |b|
    |a| = |c| = √2
    """
    )

    a = Force(1, 1)
    b = Force(0, -9)
    c = Force(-1, -1)

    print("\nPrint their magnitudes")
    print(f"|a| = {a.mag:.5f}")
    print(f"|b| = {b.mag:.5f}")
    print(f"|c| = {c.mag:.5f}")
    print(f"√2  = {sqrt(2):.5f}")

    print("\nGreater or equal than")
    print(f"a ≥ b  \t {a >= b}")  # False
    print(f"a ≥ c  \t {a >= c}")  # True
    print(f"a ≥ √2 \t {a >= sqrt(2)}")  # True

    print("\nGreater than")
    print(f"a > b  \t {a > b}")  # False
    print(f"a > c  \t {a > c}")  # False
    print(f"a > √2 \t {a > sqrt(2)}")  # False

    print("\nLess or equal than")
    print(f"a ≤ b  \t {a <= b}")  # True
    print(f"a ≤ c  \t {a <= c}")  # True
    print(f"a ≤ √2 \t {a <= sqrt(2)}")  # True

    print("\nLess than")
    print(f"a < b  \t {a < b}")  # True
    print(f"a < c  \t {a < c}")  # False
    print(f"a < √2 \t {a < sqrt(2)}")  # False

    print("\nEqual than")
    print(f"a = b  \t {a == b}")  # False
    print(f"a = c  \t {a == c}")  # True
    print(f"a = √2 \t {a == sqrt(2)}")  # True

    print("\nNot equal than")
    print(f"a ≠ b  \t {a != b}")  # True
    print(f"a ≠ c  \t {a != c}")  # False
    print(f"a ≠ √2 \t {a != sqrt(2)}")  # False

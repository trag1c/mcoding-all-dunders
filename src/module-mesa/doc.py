"""This module contains a Circle class!"""
import math
from typing import Self


class Circle:
    """Represents a Circle. Takes in a radius float."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    @property
    def area(self) -> float:
        return math.pi * self.radius**2

    @classmethod
    def from_area(cls, area: float) -> Self:
        """Creates a Circle given the area."""
        return cls(math.sqrt(area / math.pi))


def main() -> None:
    print("Module docstring:", __doc__)
    print("Circle docstring:", Circle.__doc__)
    print("Circle.from_area docstring:", Circle.from_area.__doc__)
    print("abs docstring:", abs.__doc__)


if __name__ == "__main__":
    main()

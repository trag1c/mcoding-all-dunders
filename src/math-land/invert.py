from typing import Self


class PrimaryColor:
    """Base class for each primary color in the RGB space

    >>> c = PrimaryColor(100)
    >>> print(c)
    100

    >>> c.another_attr = 200
    Traceback (most recent call last):
        ...
    AttributeError: 'PrimaryColor' object has no attribute 'another_attr'
    """

    __slots__ = ("value",)

    def __init__(self, value: int) -> None:
        """Inititalize and check if the PrimaryColor has a valid value

        >>> PrimaryColor(888)
        Traceback (most recent call last):
            ...
        ValueError: Color value is not between 0 and 255
        """

        if not 0 <= value <= 255:
            raise ValueError("Color value is not between 0 and 255")

        self.value = value

    def __invert__(self) -> Self:
        """Returns the inverse of the color as the complement to 255

        >>> print(~PrimaryColor(100))
        155
        """
        return PrimaryColor(255 - self.value)

    def __str__(self) -> str:
        return str(self.value)


class RGBColor:
    """A color in RGB space.

    >>> pink = RGBColor(255, 192, 203)
    >>> print(pink)
    (255, 192, 203)

    """

    __slots__ = "r", "g", "b"

    def __init__(
        self,
        r: int | PrimaryColor,
        g: int | PrimaryColor,
        b: int | PrimaryColor,
    ) -> None:
        self.r = r if isinstance(r, PrimaryColor) else PrimaryColor(r)
        self.g = g if isinstance(g, PrimaryColor) else PrimaryColor(g)
        self.b = b if isinstance(b, PrimaryColor) else PrimaryColor(b)

    def __invert__(self) -> Self:
        """Calculate the inverse of each PrimaryColor and returns a new
        RGBColor

        >>> pink = RGBColor(255, 192, 203)
        >>> antipink = ~pink
        >>> print(antipink)
        (0, 63, 52)
        """
        return RGBColor(~self.r, ~self.g, ~self.b)

    def __str__(self) -> str:
        return f"({self.r}, {self.g}, {self.b})"


def main():
    print("Inverted colors".center(30, "="))
    red = RGBColor(255, 0, 0)
    print(f"{red=:}, {~red=:} is cyan!")

    orange = RGBColor(255, 165, 0)
    antiorange = ~orange
    print(f"{orange=:}, {antiorange=:}")

    be = PrimaryColor(190)
    gray = RGBColor(be, be, be)
    print(f"{gray=:}, {~gray=:}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()

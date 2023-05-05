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

    __slots__ = "value"

    def __init__(self, value: int) -> None:
        self.value = value
        self.check_valid()

    def __invert__(self):
        """
        Returns the inverse of the color as the complement to 255

        >>> print(~PrimaryColor(100))
        155
        """
        return PrimaryColor(255 - self.value)

    def check_valid(self):
        """
        Check if the PrimaryColor has a valid value

        >>> PrimaryColor(230.5)
        Traceback (most recent call last):
            ...
        TypeError: Color value must be an int

        >>> PrimaryColor(888)
        Traceback (most recent call last):
            ...
        ValueError: Color value is not between 0 and 255
        """

        if not isinstance(self.value, int):
            raise TypeError("Color value must be an int")

        if not 0 <= self.value <= 255:
            raise ValueError("Color value is not between 0 and 255")

    def __str__(self) -> str:
        return f"{self.value}"


class RGBColor:
    """
    A color in RGB space.

    >>> pink = RGBColor(255, 192, 203)
    >>> print(pink)
    (255, 192, 203)

    """

    __slots__ = "r", "g", "b"

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = PrimaryColor(r) if isinstance(r, int) else r
        self.g = PrimaryColor(g) if isinstance(g, int) else g
        self.b = PrimaryColor(b) if isinstance(b, int) else b

    def __invert__(self):
        """Calculate the inverse of each PrimaryColor and returns a new
        RBGColor

        >>> pink = RGBColor(255, 192, 203)
        >>> antipink = ~pink
        >>> print(antipink)
        (0, 63, 52)
        """
        return RGBColor(~self.r, ~self.g, ~self.b)

    def __str__(self) -> str:
        return f"({self.r}, {self.g}, {self.b})"


def main():
    print("==== Inverted colors===")
    red = RGBColor(255, 0, 0)
    print(f"{red=:}, ", f"{~red=:} is cyan!")

    orange = RGBColor(255, 165, 0)
    antiorange = ~orange
    print(f"{orange=:}, ", f"{antiorange=:}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()

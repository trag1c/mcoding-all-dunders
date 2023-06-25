# Dunders __add__, __sub__, __pos__, __neg__,
# __mul__, __floordiv__, __truediv__, __divmod__, __mod__,
# __abs__, __trunc__, __pow__, __ceil__, __floor__. __int__, __float__

from __future__ import annotations

import math


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator: int = numerator
        self.denominator: int = denominator

    def simplify(self) -> Fraction:
        gcd: int = math.gcd(self.numerator, self.denominator)
        negative_remover = (
            -1 if (self.numerator < 0 and self.denominator < 0) else 1
        )

        return Fraction(
            self.numerator // gcd * negative_remover,
            self.denominator // gcd * negative_remover,
        )

    def flip(self) -> Fraction:
        return Fraction(self.denominator, self.numerator)

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return self.numerator // self.denominator

    def __add__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        ).simplify()

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.denominator
            - other.numerator * self.denominator,
            self.denominator * other.denominator,
        ).simplify()

    def __pos__(self) -> Fraction:
        return Fraction(self.numerator, self.denominator).simplify()

    def __neg__(self) -> Fraction:
        return Fraction(-self.numerator, self.denominator).simplify()

    def __mul__(self, other: Fraction | int) -> Fraction:
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator).simplify()

        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        ).simplify()

    def __truediv__(self, other: Fraction) -> Fraction:
        return (self * other.flip()).simplify()

    def __floordiv__(self, other: Fraction) -> int:
        return int(self / other)

    def __mod__(self, other: Fraction) -> Fraction:
        return Fraction((self.numerator * other.denominator) % (other.numerator * self.numerator), self.denominator * other.denominator).simplify()

    def __divmod__(self, other: Fraction) -> tuple[Fraction, Fraction]:
        return (self // other, self % other)

    def __pow__(self, power: int) -> Fraction:
        return Fraction(
            self.numerator**power, self.denominator**power
        ).simplify()

    def __abs__(self) -> Fraction:
        return Fraction(abs(self.numerator), abs(self.denominator)).simplify()

    def __trunc__(self) -> int:
        # possible implementation
        # return int(float(self))

        # better way
        return self.numerator // self.denominator

    def __ceil__(self) -> int:
        return math.ceil(float(self))

    def __floor__(self) -> int:
        return math.floor(float(self))

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"


def main():
    three_over_five: Fraction = Fraction(3, 5)
    one_over_two: Fraction = Fraction(1, 2)
    negative_seven_over_nine: Fraction = Fraction(-7, 9)

    # __float__
    print(
        f"Floating point value of {three_over_five} is {float(three_over_five)}"
    )

    # __int__
    print(
        f"Integer floored value of {three_over_five} is {int(three_over_five)}"
    )

    # __add__
    print(
        f"{three_over_five} + {one_over_two} = {three_over_five + one_over_two}"
    )

    # __sub__
    print(
        f"{three_over_five} - {one_over_two} = {three_over_five - one_over_two}"
    )

    # __pos__
    print(
        f"Positive value of {negative_seven_over_nine} is {+negative_seven_over_nine}"
    )

    # __neg__
    print(f"Negative value of {three_over_five} is {-three_over_five}")

    # __mul__
    print(
        f"{three_over_five} * {one_over_two} = {three_over_five * one_over_two}"
    )

    # __truediv__
    print(
        f"{three_over_five} / {one_over_two} = {three_over_five / one_over_two}"
    )

    # __floordiv__
    print(
        f"{three_over_five} // {one_over_two} = {three_over_five // one_over_two}"
    )

    # __mod__
    print(
        f"{three_over_five} % {one_over_two} = {three_over_five % one_over_two}"
    )

    # __divmod__
    print(
        f"divmod({three_over_five}, {one_over_two}) = {divmod(three_over_five, one_over_two)}"
    )

    # __pow__
    print(f"{three_over_five} ** 2 = {three_over_five ** 2}")

    # __abs__
    print(
        f"Absolute value of {negative_seven_over_nine} is {abs(negative_seven_over_nine)}"
    )

    # __trunc__
    print(
        f"Truncated value of {three_over_five} is {math.trunc(three_over_five)}"
    )

    # __ceil__
    print(f"Ceiled value of {three_over_five} is {math.ceil(three_over_five)}")

    # __floor__
    print(
        f"Floored value of {three_over_five} is {math.floor(three_over_five)}"
    )


if __name__ == "__main__":
    main()

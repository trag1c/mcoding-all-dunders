# Dunders __add__, __sub__, __pos__, __neg__,
# __mul__, __floordiv__, __truediv__, __divmod__, __mod__,
# __abs__, __trunc__, __pow__, __ceil__, __floor__. __int__, __float__

from __future__ import annotations

import math


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator: int = numerator
        self.denominator: int = denominator

        self.simplify()

    def simplify(self) -> Fraction:
        gcd: int = math.gcd(self.numerator, self.denominator)
        negative_remover = -1 if (self.numerator < 0 and self.denominator < 0) else 1

        return Fraction(self.numerator // gcd * negative_remover, self.denominator // gcd * negative_remover)

    def flip(self) -> Fraction:
        return Fraction(self.denominator, self.numerator)

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return self.numerator // self.denominator

    def __add__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        ).simplify()

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
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
            self.numerator * other.numerator, self.denominator * other.denominator
        ).simplify()

    def __truediv__(self, other: Fraction) -> Fraction:
        return (self * other.flip()).simplify()

    def __floordiv__(self, other: Fraction) -> int:
        return int(self / other)

    def __mod__(self, other: Fraction) -> Fraction:
        remainder: int = other - other * (self // other)

        return self - remainder * other

    def __divmod__(self, other: Fraction) -> tuple[Fraction, Fraction]:
        return (self // other,
                self % other)

    def __pow__(self, power: int) -> Fraction:
        return Fraction(self.numerator ** power, self.denominator ** power).simplify()

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


def main():
    pass


if __name__ == "__main__":
    main()

# Dunders __add__, __sub__, __pos__, __neg__,
# __mul__, __floordiv__, __truediv__, __divmod__, __mod__, __int__

from __future__ import annotations
import math


class Number:
    value: int | float = 0

    def __init__(self, value: int | float) -> None:
        self.value = value

    def __int__(self) -> int:
        return int(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __add__(self, other: Number) -> Number:
        return Number(self.value + other.value)

    def __sub__(self, other: Number) -> Number:
        return Number(self.value - other.value)

    def __pos__(self) -> Number:
        return Number(+self.value)

    def __neg__(self) -> Number:
        return Number(-self.value)

    def __mul__(self, other: Number) -> Number:
        return Number(self.value * other.value)

    def __floordiv__(self, other: Number) -> Number:
        return Number(self.value // other.value)

    def __truediv__(self, other: Number) -> Number:
        return Number(self.value / other.value)

    def __divmod__(self, other: Number) -> tuple[Number, Number]:
        return (Number(self.value // other.value),
                Number(self.value % other.value))

    def __mod__(self, other: Number) -> Number:
        return Number(self.value % other.value)

    def __floor__(self) -> Number:
        return Number(math.floor(self.value))

    def __ceil__(self) -> Number:
        return Number(math.ceil(self.value))

    def __str__(self) -> str:  # For printing
        return str(self.value)


def main():
    val1 = Number(-2.71)
    val2 = Number(3.14)

    # Calls __int__ which constructs an integer
    print(f"val1 as intenger: {int(val1)}")

    # Calls __float__ which constructs a float
    print(f"val2 as float: {float(val1)}")

    print(f"val1 + val2: {val1 + val2}")  # Calls __add__
    print(f"val1 - val2: {val1 - val2}")  # Calls __sub__
    print(f"+val1: {+val1}")  # Calls __pos__
    print(f"-val1: {-val1}")  # Calls __neg__
    print(f"val1 * val2: {val1 * val2}")  # Calls __mul__
    print(f"val1 // val2: {val1 // val2}")  # Calls __floordiv__
    print(f"val1 / val2: {val1 / val2}")  # Calls __truediv__
    print(f"divmod(val1, val2): {divmod(val1, val2)}")  # Calls __divmod__
    print(f"val1 % val2: {val1 % val2}")  # Calls __mod__

    print(f"math.floor(val1): {math.floor(val1)}")  # Calls __floordiv__
    print(f"math.ceil(val1): {math.ceil(val1)}")  # Calls __ceil__


if __name__ == "__main__":
    main()

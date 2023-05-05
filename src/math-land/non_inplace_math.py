# Dunders __add__, __sub__, __pos__, __neg__,
# __mul__, __floordiv__, __truediv__, __divmod__, __mod__,
# __abs__, __trunc__, __pow__

from __future__ import annotations

import math


class NumberWrapper:
    value: int | float = 0

    def __init__(self, value: int | float) -> None:
        self.value = value

    def __add__(self, other: NumberWrapper) -> NumberWrapper:
        return NumberWrapper(self.value + other.value)

    def __sub__(self, other: NumberWrapper) -> NumberWrapper:
        return NumberWrapper(self.value - other.value)

    def __pos__(self) -> NumberWrapper:
        return NumberWrapper(+self.value)

    def __neg__(self) -> NumberWrapper:
        return NumberWrapper(-self.value)

    def __abs__(self) -> NumberWrapper:
        return NumberWrapper(abs(self.value))

    def __mul__(self, scalar: int | float) -> NumberWrapper:
        return NumberWrapper(self.value * scalar)

    def __floordiv__(self, divisor: int | float) -> NumberWrapper:
        return NumberWrapper(self.value // divisor)

    def __truediv__(self, divisor: int | float) -> NumberWrapper:
        return NumberWrapper(self.value / divisor)

    def __divmod__(self, divisor: int | float) -> tuple[NumberWrapper, NumberWrapper]:
        return (
            NumberWrapper(self.value // divisor),
            NumberWrapper(self.value % divisor),
        )

    def __mod__(self, divisor: int | float) -> NumberWrapper:
        return NumberWrapper(self.value % divisor)

    def __pow__(self, power: int | float) -> NumberWrapper:
        return NumberWrapper(self.value**power)

    def __floor__(self) -> NumberWrapper:
        return NumberWrapper(math.floor(self.value))

    def __ceil__(self) -> NumberWrapper:
        return NumberWrapper(math.ceil(self.value))

    def __trunc__(self) -> int:
        return int(self.value)

    def __str__(self) -> str:  # For printing
        return str(self.value)


def main():
    number_100 = NumberWrapper(100)
    number_neg200 = NumberWrapper(-200)  # Owes land to the government
    number_5point5 = NumberWrapper(5.5)

    print(f"Combined value of number_100, number_neg200: {number_100 + number_5point5}")  # Calls __add__

    # Calls __sub__
    print(f"The value of number_100 taken away from plot 2: {number_100 - number_5point5}")

    print(f"Positive of number_100 value +(number_100.value): {+number_100}")  # Calls __pos__
    print(f"Negative of number_100 value -(number_100): {-number_100}")  # Calls __neg__
    print(f"Absolute value number_neg200 value: {abs(number_neg200)}")  # Calls __abs__
    print(f"number_100 value being scaled by 3: {number_100 * 3}")  # Calls __mul__

    # Calls __pow__
    print(f"number_5point5 value being raised to the power of 3 {number_5point5 ** 3}")
    # pow(number_5point5, 3) also works

    # Calls __floordiv__
    print(
        "Divisions into plots of land from number_100 of exactly 9 value: "
        f"{number_100 // 9}"
    )
    print(f"Divides number_neg200 into 5 pieces: {number_neg200 / 5}")  # Calls __truediv__

    divisions, remainder = divmod(number_100, 7)  # Calls __divmod__
    print(
        f"number_100 can be divided into {divisions} plots of 7 value each "
        f"with a remainder of {remainder} value"
    )

    # Calls __mod__
    print(
        f"The remainder of dividing number_100 into 22 whole pieces is"
        f"{number_100 % 22}"
    )

    # Calls __floor__
    print(f"The value of number_5point5 rounded down is: {math.floor(number_5point5)}")

    # calls __ceil__
    print(f"The are of number_5point5 rounded up is: {math.ceil(number_5point5)}")

    # calls __trunc__
    print(f"The truncated integer value of number_5point5 {math.trunc(number_5point5)}")


if __name__ == "__main__":
    main()

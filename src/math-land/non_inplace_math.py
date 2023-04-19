# Dunders __add__, __sub__, __pos__, __neg__,
# __mul__, __floordiv__, __truediv__, __divmod__, __mod__,
# __abs__, __trunc__, __pow__

from __future__ import annotations
import math


class Land:
    area: int | float = 0

    def __init__(self, area: int | float) -> None:
        self.area = area

    def __add__(self, other: Land) -> Land:
        return Land(self.area + other.area)

    def __sub__(self, other: Land) -> Land:
        return Land(self.area - other.area)

    def __pos__(self) -> Land:
        return Land(+self.area)

    def __neg__(self) -> Land:
        return Land(-self.area)

    def __abs__(self) -> Land:
        return Land(abs(self.area))

    def __mul__(self, scalar: int | float) -> Land:
        return Land(self.area * scalar)

    def __floordiv__(self, dividend: int | float) -> Land:
        return Land(self.area // dividend)

    def __truediv__(self, dividend: int | float) -> Land:
        return Land(self.area / dividend)

    def __divmod__(self, divided_and_modded: int | float) -> tuple[Land, Land]:
        return (
            Land(self.area // divided_and_modded),
            Land(self.area % divided_and_modded),
        )

    def __mod__(self, modded: int | float) -> Land:
        return Land(self.area % modded)

    def __pow__(self, power: int | float) -> Land:
        return Land(self.area**power)

    def __floor__(self) -> Land:
        return Land(math.floor(self.area))

    def __ceil__(self) -> Land:
        return Land(math.ceil(self.area))

    def __trunc__(self) -> int:
        return int(self.area)

    def __str__(self) -> str:  # For printing
        return str(self.area)


def main():
    plot1 = Land(100)
    plot2 = Land(-200)  # Owes land to the government
    plot3 = Land(5.5)

    print(f"Combined area of plot1, plot2: {plot1 + plot3}")  # Calls __add__

    # Calls __sub__
    print(f"The area of plot1 taken away from plot 2: {plot1 - plot3}")

    print(f"Positive of plot1 area +(plot1.area): {+plot1}")  # Calls __pos__
    print(f"Negative of plot1 area -(plot1): {-plot1}")  # Calls __neg__
    print("Absolute value plot2 area: {abs(plot2)}")  # Calls __abs__
    print(f"plot1 area being scaled by 3: {plot1 * 3}")  # Calls __mul__

    # Calls __pow__
    print(f"plot3 area being raised to the power of 3 {plot3 ** 3}")
    # pow(plot3, 3) also works

    # Calls __floordiv__
    print(
        f"Divisions into plots of land from plot1 of exactly 9 area: "
        f"{plot1 // 9}"
    )
    print(f"Divides plot2 into 5 pieces: {plot2 / 5}")  # Calls __truediv__

    divisions, remainder = divmod(plot1, 7)  # Calls __divmod__
    print(
        f"plot1 can be divided into {divisions} plots of 7 area each "
        f"with a remainder of {remainder} area"
    )

    # Calls __mod__
    print(
        f"The remainder of dividing plot1 into 22 whole pieces is"
        f"{plot1 % 22}"
    )

    # Calls __floor__
    print(f"The area of plot3 rounded down is: {math.floor(plot3)}")

    # calls __ceil__
    print(f"The are of plot3 rounded up is: {math.ceil(plot3)}")

    # calls __trunc__
    print(f"The truncated integer area of plot3 {math.trunc(plot3)}")


if __name__ == "__main__":
    main()

# Dunders __base__, __bases__, __subclasses__


from __future__ import annotations


class Carbon:
    def get_atom(self) -> str:
        return "C"


class Hydrogen:
    def get_atom(self) -> str:
        return "H"


class Oxygen:
    def get_atom(self) -> str:
        return "O"


class Ozone(Oxygen):
    ...


class Water(Oxygen, Hydrogen):
    ...


class CarbonDioxide(Carbon, Oxygen):
    ...


class Glucose(CarbonDioxide, Water):
    ...


# Inheritance tree
#
#          Glucose
#         /        \
# CarbonDioxide     Water
#       |     Ozone   |
#       /\    |      /\
#      /  \   |     /  \
#     /    \  |    /    \
# Carbon     Oxygen   Hydrogen


def main():
    print(f"Glucose derives from {Glucose.__bases__ = }")
    print(f"CarbonDioxide derives from {CarbonDioxide.__bases__ = }")
    print(f"Ozone derives from {Ozone.__base__ = }")

    # __base__ is the first element of __bases__
    # and the first in the inheritance list
    print(f"Water first derives from {Water.__base__ = }")

    # __base__ also determines which method is called
    # if two methods have the same nade

    print(f"Water first derives from {Water().get_atom() = }")
    print(f"Classes that derive from Oxygen: {Oxygen.__subclasses__() = }")


if __name__ == '__main__':
    main()

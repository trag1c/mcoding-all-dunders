# Dunders __base__, __bases__, __subclasses__


from __future__ import annotations


class Carbon:
    ...


class Hydrogen:
    ...


class Oxygen:
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
#         /       \
# CarbonDioxide   Water
#       /   \     /   \
#    Carbon  Oxygen  Hydrogen


def main():
    ...


if __name__ == '__main__':
    main()

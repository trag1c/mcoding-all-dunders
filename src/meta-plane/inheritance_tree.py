# Dunders __base__, __bases__, __subclasses__


from __future__ import annotations


class LivingThing:
    ...


class SmallThing:
    ...


class Animal(LivingThing):
    ...


class Zebra(Animal):
    ...


class Ant(Animal, SmallThing):
    ...


# Inheritance tree
#
#         LivingThing
#        /
#       Animal    SmallThing
#      /      \   /
#     Zebra    Ant


def main():
    # Base class of Zebra
    print(f"{Zebra.__base__ = }")

    # Base class of Ant (since there are mutiple base classes,
    # __base__ returns the first in the inheritance list)
    # The inheritance order also affects the mro (method resolution order)
    print(f"{Ant.__base__ = }")

    # All base classes of Ant
    print(f"{Ant.__bases__ = }")

    # All subclasses of Animal
    print(f"{Animal.__subclasses__() = }")


if __name__ == "__main__":
    main()

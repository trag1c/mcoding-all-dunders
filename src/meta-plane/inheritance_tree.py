# Dunders __base__, __bases__, __subclasses__


from __future__ import annotations


class LivingThing:
    def get_class_name(self) -> str:
        return "LivingThing"


class SmallThing:
    def get_class_name(self) -> str:
        return "SmallThing"


class Cell(LivingThing, SmallThing):
    def get_class_name(self) -> str:
        return "Cell"


class Prokaryote(Cell):
    def get_class_name(self) -> str:
        return "Prokaryote"


class Eukaryote(Cell):
    def get_class_name(self) -> str:
        return "Eukaryote"


class Animal(LivingThing):
    def get_class_name(self) -> str:
        return "Animal"


class Zebra(Animal):
    def get_class_name(self) -> str:
        return "Zebra"


class Ant(Animal, SmallThing):
    def get_class_name(self) -> str:
        return "Ant"


# Inheritance tree
#
#          LivingThing   SmallThing
#         /          \  /    |
#       Animal       Cell    |
#       /    \       /  \    /
#      Zebra  \     PK   EK /
#              \           /
#               \         /
#                \       /
#                 \     /
#                  \   /
#                   Ant


def main():
    ...


if __name__ == "__main__":
    main()

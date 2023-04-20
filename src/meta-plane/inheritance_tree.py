# Dunders __base__, __bases__, __subclasses__, __mro__

# Maybe not __mro_entries__


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


class HydrogenPeroxide(Water):
    ...


class Glucose(CarbonDioxide, Water):
    ...


class MysteryChemical(Glucose, HydrogenPeroxide):
    ...


# Inheritance tree
#           MysteryChemical
#           /             \
#           Glucose       HydrogenPeroxide
#           /     \       /
# CarbonDioxide     Water
#       /   \       /   \
#  Carbon    Oxygen      Hydrogen

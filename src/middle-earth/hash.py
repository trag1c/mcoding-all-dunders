class Unhashable:
    def __eq__(self, other: object) -> bool:
        return self is other


class Citizen:
    def __init__(self, name: str, surname: str, address: str) -> None:
        self.name = name
        self.surname = surname
        self.address = address

    def __hash__(self) -> int:
        return hash((self.name, self.surname, self.address))



    def __eq__(self, other: object) -> bool:
        if isinstance(other, Citizen):
            # objects which compare equal must have the same hash value
            return hash(self) == hash(other)
        return NotImplemented


if __name__ == "__main__":
    jacob_walker = Citizen("Jacob", "Walker", "Cottage St")
    selena_robinson = Citizen("Selena", "Robinson", "Whitney Ave")
    frank_jones = Citizen("Frank", "Jones", "Vista Rd")
    jacob_walker_clone = Citizen("Jacob", "Walker", "Cottage St")

    print(hash(jacob_walker))
    print(hash(selena_robinson))
    print(hash(frank_jones))
    print(hash(jacob_walker_clone))

    print(jacob_walker == jacob_walker_clone)  # True
    print(selena_robinson == frank_jones)  # False

    # Since Citizen objects are hashable, they can be put in a set or a dict
    {jacob_walker: "Jacob Walker"}
    {selena_robinson, frank_jones}

    # Unhashable instances are unhashable because the class
    # defines __eq__ but not __hash__
    try:
        {Unhashable()}
    except TypeError:
        print("Can't hash Unhashable()")

class MyCoolClass:
    def __init__(self, *, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        """Repr prints the python code to create this python object."""
        return f"MyCoolClass(value={self.value!r})"


if __name__ == "__main__":
    my_class = MyCoolClass(value=10)

    class_repr = repr(my_class)

    print("The repr is:", class_repr)
    # Evaling the repr should give us an identical object.
    print("The evaled repr is:", repr(eval(class_repr)))

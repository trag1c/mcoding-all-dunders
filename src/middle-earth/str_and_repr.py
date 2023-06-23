class MyCoolClass:
    def __init__(self, *, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        """Repr prints the python code to create this python object."""
        return f"MyCoolClass(value={self.value!r})"

    def __str__(self) -> str:
        """str returns the human-readable string for this class"""
        return f"My Cool Class Value is: {self.value}"


if __name__ == "__main__":
    my_class = MyCoolClass(value=10)

    print("Printing the output from __repr__()")
    class_repr = repr(my_class)
    print("The repr is:", class_repr)
    # Evaling the repr should give us an identical object.
    print("The evaled repr is:", repr(eval(class_repr)))
    print(f"Calling the repr using f-string: {my_class!r}\n")

    # Following are the ways to call the __str__
    print("Printing the output from __str__()")
    print(my_class)
    print("The str() output is:", str(my_class))
    print(f"Calling the str using f-string: {my_class!s}")

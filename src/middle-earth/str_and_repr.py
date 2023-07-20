import re


def some_func() -> str:
    return "Test"


class MyCoolClass:
    def __init__(self, *, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        """Return a string representation of the object.

        For many types, the __repr__ method returns a string that would
        recreate that object with the same value when passed to the
        built-in eval() function.

        Otherwise, the representation is a string enclosed in angle brackets
        that contains the name of the type of the object with additional
        information often including the name and address of the object.
        """
        return f"MyCoolClass(value={self.value!r})"

    def __str__(self) -> str:
        """str returns the human-readable string for this class"""
        return f"My Cool Class Value is: {self.value}"


if __name__ == "__main__":
    my_class = MyCoolClass(value="∫ f(x) dx")

    print("Printing the output from __repr__()")
    class_repr = repr(my_class)
    print("The repr is:", class_repr)
    print(f"Calling the repr using f-string: {my_class!r}")

    # Evaluating the repr gives us identical object most of the time.
    print("The evaled repr is:", repr(eval(class_repr)))

    # Except in some occasions like:
    # Calling eval on these objects will either not return same object
    # or result in an error.
    digit_regex = re.compile(r"\d")
    print(repr(digit_regex))
    x = some_func
    print(repr(x))
    o = object()
    print(repr(o))

    # You can use ascii to escape the non-printable characters in the repr
    print("The ascii repr of my_class is:", ascii(my_class))
    print(f"Calling the ascii using f-string: {my_class!a}\n")

    # Following are the ways to call the __str__
    print("Printing the output from __str__()")
    print(my_class)
    print("The str() output is:", str(my_class))
    # !s is the modifier for str and is equivalent to {my_class}
    print(f"Calling the str using f-string: {my_class!s} == {my_class}")

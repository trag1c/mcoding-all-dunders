import re


class MyCoolClass:
    def __init__(self, *, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"MyCoolClass(value={self.value!r})"

    def __str__(self) -> str:
        return f"My Cool Class Value is: {self.value}"


if __name__ == "__main__":
    my_class = MyCoolClass(value="∫ f(x) dx")
    print("Printing the output from __repr__()")
    print("The repr is:", repr(my_class))
    print(f"Calling the repr using f-string: {my_class!r}")
    print("The evaled repr is:", repr(eval(repr(my_class))))

    print(repr(re.compile(r"\d")))  # Can't eval repr in these examples
    o = object()
    print(repr(o))

    print("The ascii repr of my_class is:", ascii(my_class))
    print(f"Calling the ascii using f-string: {my_class!a}\n")

    print("Printing the output from __str__()")
    print(my_class)
    print("The str() output is:", str(my_class))
    print(f"Calling the str using f-string: {my_class!s} == {my_class}")

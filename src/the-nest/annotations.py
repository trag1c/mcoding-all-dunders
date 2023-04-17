x: int
y: list[int | float]

class Base:
    a: int
    b: str


class Derived(Base):
    pass


def pretty_bin(n: int, *, sep: str = " ") -> str:
    binary = f"{n:b}"
    while len(binary) % 4 != 0:
        binary = f"0{binary}"
    return sep.join(binary[i:i+4] for i in range(0, len(binary), 4))


def main() -> None:
    print(Base.__annotations__)
    # {'a': <class 'int'>, 'b': <class 'str'>}

    print(Derived.__annotations__)
    # Python <=3.9: {'a': <class 'int'>, 'b': <class 'str'>}
    # Python >=3.10: {}

    print(pretty_bin(12367))  # 0011 0000 0100 1111
    print(pretty_bin.__annotations__)
    # {'n': <class 'int'>, 'sep': <class 'str'>, 'return': <class 'str'>}

    print(__annotations__)  # module annotations
    # {'x': <class 'int'>, 'y': list[int | float]}


if __name__ == "__main__":
    main()

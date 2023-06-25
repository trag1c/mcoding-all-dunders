from __future__ import annotations

import operator as op

ASCII = "".join(map(chr, range(128)))


class Char:
    def __init__(self, char: str | int) -> None:
        self.char = chr(char) if isinstance(char, int) else char

    def __add__(self, other: int) -> Char:
        return Char(op.index(self) + other)

    def __index__(self) -> int:
        return ord(self.char)


def main() -> None:
    a = Char("a")
    z = Char("z")

    # Used for indexing and slicing built-in types
    print(ASCII[Char(69)], ASCII[69])  # E E
    print(ASCII[a : z + 1])  # abcdefghijklmnopqrstuvwxyz

    # Used for numeric conversions
    print(int(z))  # also used by float(), complex(), operator.index()
    print(bin(a))  # also used by oct(), hex()


if __name__ == "__main__":
    main()

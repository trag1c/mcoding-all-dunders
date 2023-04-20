class Char:
    def __init__(self, value: str | int) -> None:
        if isinstance(value, str):
            if len(value) != 1:
                raise ValueError("value must be of length 1")
            value = ord(value)
        self.value = value

    def __repr__(self) -> str:
        return f"{chr(self.value)!r}"

    def __str__(self) -> str:
        return chr(self.value)

    def __index__(self) -> int:
        return self.value

    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)

    def __complex__(self) -> complex:
        return complex(self.value)


def main() -> None:
    c = Char("m")
    print(f"{c}Coding")  # mCoding
    # fmt: off
    print(
        int(c),     # 109
        float(c),   # 109.0
        complex(c)  # (109+0j)
    )
    print(  # the following conversions use __index__
        bin(c),  # 0b1101101
        oct(c),  # 0o155
        hex(c)   # 0x6d
    )
    # fmt: on
    print(range(128)[c])  # 109, __index__ used again
    # range(x)[c] == int(c)  when  x < c < 0x110000


if __name__ == "__main__":
    main()

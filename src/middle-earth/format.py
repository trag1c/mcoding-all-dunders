from struct import pack


class BinarizableFloat(float):
    def __new__(cls, val, *args, **kwargs):
        return super(BinarizableFloat, cls).__new__(cls, val)

    def __format__(self, __format_spec: str) -> str:
        if __format_spec == "b":
            binary_as_string = "".join(
                "{:08b}".format(b) for b in pack("f", self)
            )
            return binary_as_string[::-1]
        else:
            return super().__format__(__format_spec)


def main():
    integer = 32
    float_num = 0.15625
    binfloat = BinarizableFloat(0.15625)

    print("\n-> Integers have a format specification for binary")
    print(f"{integer=} is {type(integer)}.\nIn binary, {integer=:b}")

    print("\n-> But a float does not")
    try:
        print(f"{float_num:b}")

    except ValueError:
        print(f"{float_num=} is {type(float_num)}.\nNo binary :(")

    print(
        "\n-> BinarizableFloat returns a 32bit binary representation",
        "following the IEEE 754 standard",
    )

    print(f"{binfloat=} is {type(binfloat)}.\nIn binary, {binfloat=:b}")

    print("\n-> BinarizableFloat can do math with the standard float")
    print(f"{binfloat + float_num  =: .6f}")
    print(f"{binfloat * float_num  =: .6f}")
    print(f"{binfloat ** float_num =: .6f}")


if __name__ == "__main__":
    main()

from struct import pack


class BinarizableFloat(float):
    """
    Class that inherits from float and implements a format specification
    for printing it in binary.

    >>> positive_float = BinarizableFloat(4.20)
    >>> print(f"{positive_float:b}")
    01000000100001100110011001100110

    >>> negative_float = BinarizableFloat(-6.9)
    >>> print(f"{negative_float:b}")
    11000000110111001100110011001101

    >>> positive_zero = BinarizableFloat(0)
    >>> print(f"{positive_zero:b}")
    00000000000000000000000000000000

    >>> negative_zero = BinarizableFloat(-0.0)
    >>> print(f"{negative_zero:b}")
    10000000000000000000000000000000

    >>> from math import isinf
    >>> infinity = BinarizableFloat(float("inf"))
    >>> print(isinf(infinity))
    True

    >>> print(f"{infinity:b}")
    01111111100000000000000000000000

    >>> overflowed_float =  BinarizableFloat(float(8.0e38))
    >>> print(f"{overflowed_float:b}")
    Traceback (most recent call last):
    ...
    OverflowError: float too large to pack with f format
    """

    def __format__(self, __format_spec: str) -> str:
        """If the format specification is 'b', the IEEE 754 binary32
        representation is returned as a string of zeros and ones.

        The bytes are retrieved from struct.pack() assuming a float for C Type.
        Check https://docs.python.org/3/library/struct.html#format-characters
        for more details.

        Notes:
        - Byte order is fixed to big-endian.
        """

        if __format_spec == "b":
            # Get the four bytes in a float
            bytes = pack(">f", self)

            # Transform bytes into string of bits
            str_bytes = "".join("{:08b}".format(b) for b in bytes)

            return str_bytes

        else:
            return super().__format__(__format_spec)


def main():
    integer = 32
    float_num = 0.15625
    binfloat = BinarizableFloat(float_num)

    print("-> Integers have a format specification for binary")
    print(f"{integer=} is {type(integer).__name__}.\nIn binary, {integer=:b}")

    print("\n-> But a float does not")
    try:
        print(f"{float_num:b}")

    except ValueError:
        print(f"{float_num=} is {type(float_num).__name__}.\nNo binary :(")

    print(
        "\n-> BinarizableFloat returns a 32-bit binary representation",
        "following the IEEE 754 standard",
    )
    print(
        f"{binfloat=} is {type(binfloat).__name__}.",
        f"\nIn binary, {binfloat=:b}",
    )

    print("\n-> BinarizableFloat can do math with the standard float")
    print(f"{binfloat + float_num  =: .6f}")
    print(f"{binfloat * float_num  =: .6f}")
    print(f"{binfloat ** float_num =: .6f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()

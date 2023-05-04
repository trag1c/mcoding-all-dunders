import unittest
from math import isinf
from struct import pack


class BinarizableFloat(float):
    def __new__(cls, val, *args, **kwargs):
        return super(BinarizableFloat, cls).__new__(cls, val)

    def __format__(self, __format_spec: str) -> str:
        """If the format specification is 'b', the IEEE 754 binary32
        representation is returned as a string of zeros and ones.

        The bytes are retrieved from struct.pack() assuming a float for C Type.
        Check https://docs.python.org/3/library/struct.html#format-characters
        for more details.

        Notes:
        - Byte order is fixed to little-endian.
        """

        if __format_spec == "b":
            # Get the four bytes in a float
            bytes = pack(">f", self)

            # Transform bytes into string of bits
            str_bytes = "".join("{:08b}".format(b) for b in bytes)

            return str_bytes

        else:
            return super().__format__(__format_spec)


class BinarizableFloatTests(unittest.TestCase):
    def test_positive_float(self):
        num = BinarizableFloat(4.20)
        self.assertEqual(f"{num:b}", "01000000100001100110011001100110")

    def test_negative_float(self):
        num = BinarizableFloat(-6.9)
        self.assertEqual(f"{num:b}", "11000000110111001100110011001101")

    def test_zeroes(self):
        num = BinarizableFloat(0)
        self.assertEqual(f"{num:b}", "00000000000000000000000000000000")

        num = BinarizableFloat(-0.0)
        self.assertEqual(f"{num:b}", "10000000000000000000000000000000")

    def test_infty(self):
        num = BinarizableFloat(float("inf"))
        self.assertTrue(isinf(num))
        self.assertEqual(f"{num:b}", "01111111100000000000000000000000")

    def test_overflow(self):
        BinarizableFloat(float(8.0e38))
        self.assertRaises(OverflowError)


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

    ## Unit tests
    print("\n=== Unit tests ===")
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()

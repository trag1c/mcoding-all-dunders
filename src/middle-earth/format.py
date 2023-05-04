from struct import pack
from math import isnan, isinf

class BinarizableFloat(float):
    def __new__(cls, val, *args, **kwargs):
        return super(BinarizableFloat, cls).__new__(cls, val)

    def __format__(self, __format_spec: str) -> str:
        """If the format specification is 'b', the IEEE 754 binary32
        representation is returned as a string of zeros and ones. 
        
        The bytes are retrieved from struct.pack() assuming a float for C Type.
        Check https://docs.python.org/3/library/struct.html#format-characters
        for more details.

        - Byte order is fixed to little-endian. 
        - OverflowError is raised 
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

    run_tests()


def run_tests():
    """Run some checks for various floats"""

    # Positive float
    num = BinarizableFloat(4.20)
    assert f"{num:b}" == "01000000100001100110011001100110"

    # Negative float
    num = BinarizableFloat(-6.9)
    assert f"{num:b}" == "11000000110111001100110011001101"

    # Zero
    num = BinarizableFloat(0)
    assert f"{num:b}" == "00000000000000000000000000000000"

    # Negative zero
    num = BinarizableFloat(-0.0)
    assert f"{num:b}" == "10000000000000000000000000000000"

    # Infinite
    num = BinarizableFloat(float("inf"))
    assert isinf(num)
    assert f"{num:b}" == "01111111100000000000000000000000"

    # Overflow
    num = BinarizableFloat(float(8.0E+38))
    try:
        print(f"{num:b}")
    except OverflowError:
        ...
    
if __name__ == "__main__":
    main()
    

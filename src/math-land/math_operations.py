class Vector2:
    """
    A 2D Vector with X and Y coordinates.
    Does bitwise operations on the contents.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __and__(self, other):
        """Bitwise AND operation"""
        return Vector2(self.x & other.x, self.y & other.y)

    def __add__(self, other):
        """Add operation"""
        return Vector2(self.x + other.x, self.y + other.y)

    def __floordiv__(self, other):
        """Floordiv operation"""
        return Vector2(self.x // other.x, self.y // other.y)

    def __lshift__(self, other):
        """Leftshift operation"""
        return Vector2(self.x << other.x, self.y << other.y)

    def __rshift__(self, other):
        """Rightshift operation"""
        return Vector2(self.x >> other.x, self.y >> other.y)

    def __matmul__(self, other):
        """Matmul operation"""
        return Vector2(self.x @ other.x, self.y @ other.y)

    def __mod__(self, other):
        """Modulus operation"""
        return Vector2(self.x % other.x, self.y % other.y)

    def __mul__(self, other):
        """Multiplication operation"""
        return Vector2(self.x * other.x, self.y * other.y)

    def __or__(self, other):
        """Bitwise or operation"""
        return Vector2(self.x | other.x, self.y | other.y)

    def __pow__(self, other):
        """To the power of operation"""
        return Vector2(self.x**other.x, self.y**other.y)

    def __sub__(self, other):
        """Subtraction operation"""
        return Vector2(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        """Division operation"""
        return Vector2(self.x / other.x, self.y / other.y)

    def __xor__(self, other):
        """Exclusive or operation"""
        return Vector2(self.x ^ other.x, self.y ^ other.y)

    def __ixor__(self, other):
        """XOR and assign operation"""
        return self ^ other

    def __itruediv__(self, other):
        """Divide and assign operation"""
        return self / other

    def __isub__(self, other):
        """Subtract and assign operation"""
        return self - other

    def __ipow__(self, other):
        return self**other

    def __ior__(self, other):
        """Bitwise or and assign operation"""
        return self | other

    def __imul__(self, other):
        """Multiply and assign operation"""
        return self * other

    def __imod__(self, other):
        """Modulo and assign operation"""
        return self % other

    def __imatmul__(self, other):
        """Matmul and assign operation"""
        return self @ other

    def __irshift__(self, other):
        """RShift and assign operation"""
        return self >> other

    def __ilshift__(self, other):
        """LShift and assign operation"""
        return self << other

    def __ifloordiv__(self, other):
        """Floordiv and assign operation"""
        return self // other

    def __iadd__(self, other):
        """Add and assign to operation"""
        return self + other

    def __iand__(self, other):
        """Add and assign to operation"""
        return self & other

    def __neg__(self):
        """Negate"""
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        """Positive"""
        return Vector2(+self.x, +self.y)
    
    def __str__(self):
        return f"Vector2(x: {self.x}, y: {self.y})"
    
vector = Vector2(3, 4)
print(vector + Vector2(2, 1)) # Calls __add__ dunder and prints Vector2(x: 5, y: 5)

vector += Vector2(6, 9)
print(vector) # Calls __iadd__ dunder and prints Vector2(x: 9, y: 13)

print(-vector) # Calls __neg__ and prints Vector2(x: -9, y: -13)

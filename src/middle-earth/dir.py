import math


class FunctionContainer:
    def __init__(self, *functions):
        self.functions = functions

    def call_all(self, arg):
        return [(func.__name__, func(arg)) for func in self.functions]

    def __dir__(self):
        return [func.__name__ for func in self.functions]


fc = FunctionContainer(math.tan, math.sin, math.cos)

print(fc.call_all(54.6))

print(dir(fc))

print(dir())

class Composer:
    def __init__(self, *functions):
        self.functions = reversed(functions)

    def __call__(self, args):
        for function in self.functions:
            args = function(args)
        return args


if __name__ == "__main__":

    def one(x):
        return x + 1

    def two(x):
        return x + 2

    def three(x):
        return x + 3

    call = Composer(one, two, three)
    print(call(5))

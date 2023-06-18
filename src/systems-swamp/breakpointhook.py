import contextlib
import sys


@contextlib.contextmanager
def no_breakpoint():
    sys.breakpointhook = lambda *args, **kwargs: print(
        "You didn't think I'd let you debug so easily, did you?",
        file=sys.stderr,
    )
    yield
    sys.breakpointhook = sys.__breakpointhook__


with no_breakpoint():
    breakpoint()
    x = 1
    y = x * 2
    print(y)

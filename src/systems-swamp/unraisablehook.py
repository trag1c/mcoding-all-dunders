"""A context manager to ignore unraiseable errors"""
import contextlib
import sys


@contextlib.contextmanager
def silence_unraiseables():
    sys.unraisablehook = lambda *args, **kwargs: ...
    yield
    sys.unraisablehook = sys.__unraisablehook__


class Foo:
    def __del__(self):
        raise Exception("Whoops!")


with silence_unraiseables():
    # stderr to keep error messages in order
    print("Making Foo with silenced unraisables:", file=sys.stderr)
    Foo()
    print("Done", file=sys.stderr)


print("Making Foo with regular hook:", file=sys.stderr)
Foo()
print("Done", file=sys.stderr)

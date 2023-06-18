"""For real projects, use contextlib.redirect_stdout instead"""
import contextlib
import sys
from io import StringIO
from textwrap import indent
from typing import TextIO, TypeVar

T = TypeVar("T", bound=TextIO)


@contextlib.contextmanager
def redirect_stdout(target: T) -> T:
    sys.stdout = target
    yield target
    sys.stdout = sys.__stdout__


with redirect_stdout(StringIO()) as f:
    print("How much foo could a foo bar bar if a foo bar could bar foo?")
    print("A foo bar could bar as much foo as a foo bar could bar")
    print("if a foo bar could bar foo")


print("And the stdout was:")
print(indent(f.getvalue(), "> "))

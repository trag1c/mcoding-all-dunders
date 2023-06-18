"""For real projects, use contextlib.redirect_stderr instead"""
import contextlib
import sys
from io import StringIO
from textwrap import indent
from typing import TextIO, TypeVar

T = TypeVar("T", bound=TextIO)


@contextlib.contextmanager
def redirect_stderr(target: T) -> T:
    sys.stderr = target
    yield target
    sys.stderr = sys.__stderr__


with redirect_stderr(StringIO()) as f:
    try:
        1 / 0
    except ZeroDivisionError as e:
        sys.excepthook(ZeroDivisionError, e, e.__traceback__)


print("And the error is:")
print(indent(f.getvalue(), "> "))

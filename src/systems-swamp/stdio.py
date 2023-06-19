import builtins
import contextlib
import sys
from io import StringIO
from textwrap import indent
from typing import Any, TextIO, TypeVar

T = TypeVar("T", bound=TextIO)

SAVED_INPUT = input


def _input(prompt: Any) -> str:
    result = SAVED_INPUT(prompt)
    print(result)
    return result


@contextlib.contextmanager
def redirect_stdin(target: TextIO, write_to_stdout: bool = False):
    sys.stdin = target
    if write_to_stdout:
        builtins.input = _input
    yield
    sys.stdin = sys.__stdin__
    if write_to_stdout:
        builtins.input = SAVED_INPUT


@contextlib.contextmanager
def redirect_stdout(target: T) -> T:
    """Example only, use contextlib.redirect_stdout instead"""
    sys.stdout = target
    yield target
    sys.stdout = sys.__stdout__


@contextlib.contextmanager
def redirect_stderr(target: T) -> T:
    """Example only, use contextlib.redirect_stderr instead"""
    sys.stderr = target
    yield target
    sys.stderr = sys.__stderr__


with (
    redirect_stdin(StringIO("Some redirected stdin\n")),
    redirect_stdout(StringIO()) as stdout,
    redirect_stderr(StringIO()) as stderr,
):
    value = input("Input: ")
    print(f"Some stdout, with the input value of `{value}`")
    print("Some stderr", file=sys.stderr)

print("The stdout:", indent(stdout.getvalue(), "> "), sep="\n")
print("The stderr:", indent(stderr.getvalue(), "> "), sep="\n")

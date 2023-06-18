"""No contextlib option!"""
import builtins
import contextlib
import sys
from io import StringIO
from typing import TextIO

SAVED_INPUT = input


def _input(prompt):
    result = SAVED_INPUT(prompt)
    print(result)
    return result


@contextlib.contextmanager
def redirect_stdin(target: TextIO):
    sys.stdin = target
    builtins.input = _input
    yield
    sys.stdout = sys.__stdin__
    builtins.input = SAVED_INPUT


menu = """
1) egg and spam
2) egg bacon and spam
3) egg bacon sausage and spam
4) spam bacon sausage and spam
5) spam egg spam spam bacon and spam
6) spam sausage spam spam bacon spam tomato and spam
""".strip()

stdin = StringIO("Have you got anything without spam?\n1\n")

with redirect_stdin(stdin):
    print("We've got:")
    print(menu)
    choice = input("> ")
    while not choice.isdigit() or int(choice) not in range(1, 7):
        print("No, we've got:")
        print(menu)
        choice = input("> ")
    print("Excellent choice!")
    print("Spam spam spam spam. Lovely spam! Wonderful spam!")

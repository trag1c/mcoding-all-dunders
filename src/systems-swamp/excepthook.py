import sys
from contextlib import redirect_stderr
from io import StringIO
from types import TracebackType
from typing import Type


def memeify(value: str) -> str:
    return "".join(
        c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(value)
    )


def sarcastic_excepthook(
    type: Type[BaseException],
    value: BaseException,
    traceback: TracebackType,
):
    """Makes error messages sArCaStIc"""
    with redirect_stderr(StringIO()) as f:
        sys.__excepthook__(type, value, traceback)
    message = memeify(f.getvalue())
    print(message, file=sys.stderr)


sys.excepthook = sarcastic_excepthook

1 / 0

import sys
from contextlib import redirect_stderr
from io import StringIO
from types import TracebackType


def memeify(value: str) -> str:
    return "".join(
        c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(value)
    )


def sarcastic_excepthook(
    exc_type: type[BaseException],
    exc_val: BaseException,
    exc_tb: TracebackType,
) -> None:
    """Makes error messages sArCaStIc"""
    with redirect_stderr(StringIO()) as f:
        sys.__excepthook__(exc_type, exc_val, exc_tb)
    message = memeify(f.getvalue())
    print(message, file=sys.stderr)


sys.excepthook = sarcastic_excepthook

1 / 0

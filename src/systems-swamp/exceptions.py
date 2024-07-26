from types import TracebackType

SUPPRESSED_HEADER = "(But the context was suppressed (__suppress_context__))"
CONTEXT_HEADER = (
    "- The above error happened while handling this error (__context__):"
)
CAUSE_HEADER = (
    "- The above error was caused by the following error (__cause__):"
)


def print_context(exception: BaseException, pad: int = 0) -> None:
    print(" " * (pad - 2) + CONTEXT_HEADER)
    if exception.__suppress_context__:
        print(" " * pad + SUPPRESSED_HEADER)
    print_error(exception.__context__, pad=pad + 4)


def print_cause(exception: BaseException, pad: int = 0) -> None:
    print(" " * (pad - 2) + CAUSE_HEADER)
    print_error(exception.__cause__, pad=pad + 4)


def print_error(exception: BaseException, pad: int = 0) -> None:
    print(f"{' ' * pad}{type(exception).__name__}: {exception}")
    if exception.__context__ is not None:
        print_context(exception, pad=pad + 4)
    if exception.__cause__ is not None:
        print_cause(exception, pad=pad + 4)


class ExplainErrors:
    """Explains and suppresses any exceptions raised"""

    def __enter__(self) -> None:
        ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        if exc_val is not None:
            print_error(exc_val, pad=4)
            print()
        return True


print("Regular Exception:")
with ExplainErrors():
    result = 1 / 0

print("Exception with context:")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        raise ValueError("Can't use 0")

print("Another Exception with context:")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        result = "a" + 3

print("Exception with suppressed context:")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        raise ValueError("Can't use 0") from None

print("Exception with cause (and suppressed context)")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Can't use 0") from e

print("Exception with cause (and different suppressed context):")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        raise ValueError("Can't use 0") from Exception("Another exception")

print("Exception with cause and context (unsuppressed):")
with ExplainErrors():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        err = ValueError("Can't use 0")
        err.__cause__ = Exception("Another exception")
        err.__suppress_context__ = False
        raise err

print("Manually creating an error with cause and context:")
with ExplainErrors():
    err = Exception("The exception")
    err.__context__ = Exception("The context")
    err.__cause__ = Exception("The cause")
    err.__suppress_context__ = False
    raise err

print("Nested Errors Example:")
with ExplainErrors():
    try:
        try:
            raise Exception("The initial Exception")
        except Exception as e:
            raise Exception("Inside the inner try") from e
    except Exception:
        raise Exception("Inside the outer try") from None

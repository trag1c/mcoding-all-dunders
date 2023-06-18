"""Forces __suppress_context__ to be false when an exception is raised"""


class ForceContext:
    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        exc_val.__suppress_context__ = False
        return False


with ForceContext():
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("Something went wrong!") from None

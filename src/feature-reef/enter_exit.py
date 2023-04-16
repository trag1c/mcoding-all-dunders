# Dunders __enter__ and __exit__

from __future__ import annotations


def handle_error(exception):
    ...


class Context:
    def fancy_function(self) -> None:
        print("executing fancy function")

    def __enter__(self) -> Context:
        print("entering with block")

        return self

    def __exit__(
            self, exception_type, exception_value,
            exception_traceback) -> None:
        print("exiting with block")

        if (exception_value is not None):
            print(f"exception '{exception_type}' "
                  f"occurred at line {exception_traceback.tb_lineno}: "
                  f"{exception_value}")

            print("handling error")
            handle_error(exception_value)


def main() -> None:
    with Context() as ctx:
        ctx.fancy_function()

    try:
        with Context() as ctx:
            raise Exception("error")

    except Exception:
        pass


if __name__ == "__main__":
    main()

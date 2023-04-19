# Dunders __enter__ and __exit__

from __future__ import annotations

from types import TracebackType


class Context:
    def fancy_function(self) -> None:
        print("executing fancy function")

    def __enter__(self) -> Context:
        print("entering with block")

        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_value: BaseException | None,
        exception_traceback: TracebackType,
    ) -> bool:
        print("exiting with block")

        if exception_value is not None:
            print(
                f"exception '{exception_type}' "
                f"occurred at line {exception_traceback.tb_lineno}: "
                f"{exception_value}"
            )

            print("ignoring error")

        return True  # Returning true should suppress the exception


def main() -> None:
    with Context() as ctx:  # Initializes ctx as a Context object
        ctx.fancy_function()
        raise Exception("error")
    # Context.__exit__ suppresses the exception


if __name__ == "__main__":
    main()

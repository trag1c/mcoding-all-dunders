from collections.abc import Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self, items: Sequence[T] | None = None) -> None:
        self.items = list(items or [])

    def __bool__(self) -> bool:
        return len(self.items) > 0

    def put(self, item: T) -> None:
        self.items.append(item)

    def get(self) -> T:
        return self.items.pop(0)


class PlainClass:
    pass


if __name__ == "__main__":
    que = Queue()

    if que:
        print("que is non-empty")
    else:
        print("que is empty")

    print(f"{bool(que)=}")  # False

    que.put("person")

    if que:
        print("que is non-empty")
    else:
        print("que is empty")

    print(f"{bool(que)=}")  # True

    # instances of classes without a `__bool__` method are always truthy
    print(f"{bool(PlainClass())=}")

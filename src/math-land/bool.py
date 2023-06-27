from collections.abc import Sequence
from typing import TypeVar, Generic

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self, items: Sequence[T] | None = None) -> None:
        self.items = list(items or [])

    def __bool__(self) -> bool:
        return len(self.items) > 0

    def put(self, item: T) -> None:
        self.items.append(item)

    def get(self) -> T:
        return self.pop(0)


# no __bool__ defined => always True
class PlainClass:
    pass


if __name__ == "__main__":
    que = Queue()

    if not que:
        print(bool(que))

    que.put("person")

    if que:
        print(bool(que))

    print(bool(PlainClass()))

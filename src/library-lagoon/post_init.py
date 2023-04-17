from dataclasses import dataclass


@dataclass
class Task:
    name: str
    priority: int

    def __post_init__(self) -> None:
        self.priority = min(5, max(1, self.priority))  # clamping priority to [1, 5]


def main() -> None:
    print(Task("do a flip", 4))  # Task(name='do a flip', priority=4)
    print(Task("learn samarium", 10))  # Task(name='learn samarium', priority=5)


if __name__ == "__main__":
    main()

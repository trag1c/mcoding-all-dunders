# Dunders __getitem__, __setitem__, __delitem__

from __future__ import annotations


class LunchBoxes:
    def __init__(self, **names_to_items: list[str]) -> None:
        self.user_items = names_to_items

    def __getitem__(self, name_or_index: str | int) -> str | tuple[str, str]:
        """Returns the value of a key or a pair at index when the dict is sorted"""

        if isinstance(name_or_index, int):
            return sorted(self.user_items.items())[name_or_index]

        return self.user_items[name_or_index]

    def __setitem__(self, name: str, new_items: str) -> None:
        self.user_items[name] = new_items

    def __delitem__(self, name: str) -> None:
        del self.user_items[name]


def main():
    lunchboxes = LunchBoxes(
        alice=["apple", "carrot", "rice"],
        bob=["asparagus", "lemon", "fish"],
        carol=["chocolate", "milk", "bread"],
    )

    print(f"Carol's lunch box: {lunchboxes['carol']}")  # A call to __getitem__
    print(f"Bob's lunch box: {lunchboxes['bob']}")  # A call to __getitem__

    lunchboxes["alice"] = [
        "apple",
        "carrot",
        "rice",
        "chocolate",
    ]  # A call to __setitem__

    print(f"Alice's new lunchbox {lunchboxes['alice']}")

    del lunchboxes["carol"]  # A call to __delitem__

    print(f"Current lunchboxes data: {lunchboxes.user_items}")


if __name__ == "__main__":
    main()

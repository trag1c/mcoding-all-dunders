# Dunders __getitem__, __setitem__, __delitem__

from __future__ import annotations


class Accounts:
    account_data: dict[str, str] = {}

    def __init__(self, account_data: dict[str, str]) -> None:
        self.account_data = account_data

    def __getitem__(self, key: str | int) -> str | tuple[str, str]:
        """Returns the value of a key or a pair at index when the dict is sorted"""

        if isinstance(key, int):
            return sorted(self.account_data.items())[key]

        return self.account_data[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.account_data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.account_data[key]


def main():
    accounts = Accounts(
            {"user1": "data1",
             "user2": "data2",
             "fancyuser": "fancydata"})

    print(f"data at 'user1': {accounts['user1']}")
    print(f"data at index 0: {accounts[0]}")

    accounts["user2"] = "newdata"  # A call to __setitem__

    del accounts["user1"]  # A call to __delitem__

    print(f"Currenet account data: {accounts.account_data}")


if __name__ == "__main__":
    main()

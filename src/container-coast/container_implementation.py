# Dunders __getitem__, __setitem__, __delitem__
# __missing__, __iter__, __next__, __reversed__, __len__, __contains__

from __future__ import annotations

from random import randint


class BinaryTree:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __contains__(self, key):
        if self.key == key:
            return True

        if self.left is not None and key < self.key:
            return key in self.left  # Calls __contains__

        if self.right is not None and self.key < key:
            return key in self.right  # Calls __contains__

        return False

    def __setitem__(self, key, value):
        if (self.key is None) or (self.key == key):
            self.key = key
            self.value = value

        if key < self.key:
            self.left = BinaryTree() if self.left is None else self.left
            self.left[key] = value

        if self.key < key:
            self.right = BinaryTree() if self.right is None else self.right
            self.right[key] = value

    def __getitem__(self, key):
        if self.key == key:
            return self.value

        if key not in self:
            raise KeyError(f"Key {key} not found")

        if key < self.key:
            return self.left[key]

        return self.right[key]

    def __delitem__(self, key):
        if key in self:
            self[key] = None
        else:
            raise KeyError(f"Key {key} not found")

    def __len__(self):
        if self.key is None:
            return 0

        return (
            1
            + (len(self.left) if self.left is not None else 0)
            + (len(self.right) if self.right is not None else 0)
        )

    def __iter__(self):
        if self.left is not None:
            yield from self.left

        yield (self.key, self.value)

        if self.right is not None:
            yield from self.right

    def __reversed__(self):
        if self.right is not None:
            yield from reversed(self.right)

        yield (self.key, self.value)

        if self.left is not None:
            yield from reversed(self.left)


class ListWrapper:
    def __init__(self, value=None):
        self.value = value or []

    def __getitem__(self, index):
        return self.value[index]

    def __len__(self):
        return len(self.value)


class RangeIterator:
    def __init__(self, start, step, stop):
        self.current = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        current_value = self.current

        self.current += self.step

        if self.current > self.stop:
            raise StopIteration

        return current_value


def main():
    tree = BinaryTree()

    for _ in range(20):
        tree[randint(0, 10)] = randint(0, 50)  # Calls __setitem__

    print("Tree in order by keys:")
    for key, value in tree:  # Calls __iter__
        print(f"{key}: {value}")

    print("Tree in reverse order:")  # Calls __reversed__
    for key, value in reversed(tree):
        print(f"{key}: {value}")

    print(f"Tree has {len(tree)} nodes")  # Calls __len__
    print(f"Tree has 8 as a key: {8 in tree}")  # Calls __contains__

    try:
        # Calls __getitem__ but fails and raises a KeyError
        print(tree[100])

    except KeyError as e:
        print(f"Error when trying to access key 100: {e}")

    tree[24] = 150  # Calls __setitem__
    print(f"The tree at key 24 is {tree[24]}")  # Calls __getitem__

    # __iter__ and __reversed__ fallback

    lw = ListWrapper([1, 2, 3, 4, 5])

    # Still works even without __iter__, uses __getitem__ and __len__
    print("Values of list wrapper: ", *lw)

    print("Values of list wrapper reversed: ", *reversed(lw))

    r = RangeIterator(0, 1, 4)
    print(f"First call to range iterator: {next(r) = }")  # Calls __next__
    print(f"Second call to range iteraotr: {next(r) = }")
    print(f"Third call to range iteraotr: {next(r) = }")

    range_0_to_10 = RangeIterator(0, 1, 10)

    # Stops before 10 since StopIteration is raised
    for value in range_0_to_10:
        print(value)


if __name__ == "__main__":
    main()

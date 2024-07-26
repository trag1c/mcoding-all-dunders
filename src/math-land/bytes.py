from pathlib import Path


class File:
    def __init__(self, path):
        self.path = Path(path)

    def __bool__(self):
        return self.path.exists()

    def __str__(self):
        return self.path.name

    def __bytes__(self):
        return self.path.read_bytes()

    def create(self):
        self.path.write_text("Lorem ipsum dolor sit")


def main():
    test_file = File("file.txt")

    if not test_file:
        test_file.create()
        Path("file2.txt").write_bytes(bytes(test_file))

    print(f"{test_file} {'exists' if test_file else 'does not exist'}")


if __name__ == "__main__":
    main()

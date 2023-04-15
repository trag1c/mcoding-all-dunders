# Dunders __enter__ and __exit__

from __future__ import annotations


class DocumentCollection:
    paths: set[str] = set()
    files = {}
    files_are_being_opened: bool = False

    def __init__(self, paths: list[str]):
        for path in paths:
            self.add_file(path)

    def add_file(self, path: str) -> None:
        self.paths.add(path)

        if self.files_are_being_opened and path in self.paths:
            self.files[path] = open(path, "w")

    def __enter__(self) -> None:
        self.files_are_being_opened = True

        for path in self.paths:
            self.add_file(path)

    def __exit__(
            self, exception_type, exception_value,
            exception_traceback) -> None:
        for path, file in self.files.items():
            file.close()

        self.files_are_being_opened = False
        self.files = {}


def main() -> None:
    documents = DocumentCollection(["doc1", "doc2", "doc3"])

    with documents:
        for path, document in documents.files.items():
            if document.writable():
                document.write("Hello, world!")

        documents.add_file("doc4")

        documents.files["doc4"].write("Important data!")
        print(documents.files)

    documents.add_file("doc5")

    with documents:
        print(documents.files.keys())


if __name__ == "__main__":
    main()

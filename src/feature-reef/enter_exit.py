# Dunders __enter__ and __exit__

from __future__ import annotations
from pathlib import Path
import os


class DocumentCollection:
    paths: set[Path] = set()
    invalid_paths: set[Path] = set()
    unopenable_paths: set[Path] = set()
    files = {}
    files_are_being_opened: bool = False

    def __init__(self, paths: list[Path]):
        for path in paths:
            self.add_file(path)

    def add_file(self, path: Path) -> None:
        path_is_file: bool = os.path.isfile(path)
        path_exists: bool = os.path.exists(path)
        path_already_added: bool = (path in self.paths
                                    | self.invalid_paths
                                    | self.unopenable_paths)

        if not path_already_added and path_exists and not path_is_file:
            self.invalid_paths.add(path)

        if not path_already_added and path_is_file:
            self.paths.add(path)

        if not path_already_added and not path_exists:
            self.paths.add(path)

        if self.files_are_being_opened and path in self.paths:
            self._open_file(path)

    def _open_file(self, path: Path) -> None:
        assert self.files_are_being_opened and path in self.paths

        if not os.path.exists(path):
            self.files[path] = open(path, "w")

        else:
            match (os.access(path, os.W_OK), os.access(path, os.R_OK)):
                case (_, False):
                    self.unopenable_paths.add(path)

                case (False, True):
                    self.files[path] = open(path, "r")

                case (True, True):
                    self.files[path] = open(path, "w")

    def open_all_files(self) -> None:
        self.files_are_being_opened = True

        for path in self.paths:
            self.add_file(path)

    def close_all_files(self) -> None:
        for path, file in self.files.items():
            file.close()

        self.files_are_being_opened = False
        self.files = {}

    def __enter__(self) -> None:
        self.open_all_files()

    def __exit__(
            self, exception_type, exception_value,
            exception_traceback) -> None:
        self.close_all_files()


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

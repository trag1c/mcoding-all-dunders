from contextlib import suppress


def main() -> None:
    exc = Exception("uh oh...")

    with suppress(AttributeError):
        print(exc.__notes__)  # not created until add_note is called

    exc.add_note("try running again :)")
    print(exc.__notes__)
    # ['try running again :)']


if __name__ == "__main__":
    main()

import asyncio
from collections.abc import Generator


class Awaitable:
    def __await__(self) -> Generator[None, None, str]:
        """
        This method is called when you `await` an object. A `TypeError`
        is raised if this method doesn't return an iterator.
        """
        yield
        return "Hello world!"


async def main():
    print(await Awaitable())


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from collections.abc import Generator
from typing import Any


class Awaitable:
    def __await__(self) -> Generator[Any, Any, str]:
        """
        This method is called when you `await` an object. A `TypeError`
        is raised if this method doesn't return an iterator.
        """
        yield
        return "Hello world!"


async def async_main():
    print(await Awaitable())


asyncio.new_event_loop().run_until_complete(async_main())

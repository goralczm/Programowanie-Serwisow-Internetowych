import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    res = await fetch('https://api.thecatapi.com/v1/images/search')
    print(res)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

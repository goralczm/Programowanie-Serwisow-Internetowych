import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    cat_api = await fetch('https://api.thecatapi.com/v1/images/search')

    print(cat_api)
    print(cat_api[0]['url'])

    url = cat_api[0]['url']
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.content.read())


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

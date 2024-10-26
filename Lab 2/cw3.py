import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    group = await asyncio.gather(fetch('https://api.thecatapi.com/v1/images/search'),
                                 fetch('https://randomfox.ca/floof/'),
                                 fetch('https://cat-fact.herokuapp.com/facts'),
                                 fetch('https://coffee.alexflipnote.dev/random.json'),
                                 fetch('https://random-d.uk/api/random'))

    for item in group:
        print(item)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

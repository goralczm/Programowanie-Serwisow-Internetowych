import aiohttp
import asyncio

from aiohttp import ClientResponse


async def fetch(url: str) -> ClientResponse:
    async with aiohttp.ClientSession() as session:
        for retry in range(3):
            async with session.get(url) as response:
                if 200 <= response.status <= 299:
                    return await response.json()
                elif 500 <= response.status <= 599:
                    print('Ponawiam zapytanie')
                else:
                    return {}

        return {}


async def main() -> None:
    group = []

    for i in range(100):
        task = asyncio.create_task(fetch('https://api.thecatapi.com/v1/images/search'))
        group.append(task)

    responses = await asyncio.gather(*group)
    print(responses)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

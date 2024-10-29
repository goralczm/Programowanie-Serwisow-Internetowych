import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    cat_api = await fetch('https://api.thecatapi.com/v1/images/search')

    cat_img_url = cat_api[0]['url']

    async with aiohttp.ClientSession() as session:
        async with session.get(cat_img_url) as response:
            img = await response.content.read()
            with open('output.jpg', 'wb') as output:
                output.write(img)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

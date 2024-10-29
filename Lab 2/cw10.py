import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def process_url(url: str, output_file_name: str) -> None:
    data = await fetch(url)
    with open(output_file_name, 'w') as output:
        output.write(str(data))


async def main() -> None:
    await asyncio.gather(process_url('https://dogapi.dog/api/v2/facts', 'facts.txt'),
                         process_url('https://dogapi.dog/api/v2/breeds', 'breeds.txt'),
                         process_url('https://dogapi.dog/api/v2/groups', 'groups.txt')
                         )


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

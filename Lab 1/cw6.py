import asyncio
import random


async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)

    res = random.randint(0, 99)
    print(f'download complete: {res} returned after {delay}s')
    return res


async def mock_download_from_web() -> None:
    await asyncio.gather(fetch(random.randint(1, 5)),
                         fetch(random.randint(1, 5)),
                         fetch(random.randint(1, 5)),
                         fetch(random.randint(1, 5)))


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(mock_download_from_web())
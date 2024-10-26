import asyncio


async def wait_both_intervals() -> None:
    await asyncio.gather(wait_three_seconds(), wait_one_second())

async def wait_three_seconds() -> None:
    await asyncio.sleep(3)
    print("Trzy sekundowe oczekiwanie zakończone")


async def wait_one_second() -> None:
    await asyncio.sleep(1)
    print("Jedno sekundowe oczekiwanie zakończone")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(wait_both_intervals())

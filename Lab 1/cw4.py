import asyncio


async def main() -> None:
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())
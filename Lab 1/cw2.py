import asyncio


async def main() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(2)
    print("World")


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())

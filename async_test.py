import asyncio


async def main() -> None:
    print("Hello World 1")
    await asyncio.sleep(1)
    print("Hello World 2")


if __name__ == '__main__':
    #with asyncio.Runner() as runner:
    #    runner.run(main())

    #asyncio.run(main())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(main())
    task2 = loop.create_task(main())
    task3 = loop.create_task(main())
    task4 = loop.create_task(main())
    task5 = loop.create_task(main())
    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)
    for pending_task in pending:
        pending_task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)

    loop.close()

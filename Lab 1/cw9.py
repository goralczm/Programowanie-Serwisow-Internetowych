import asyncio
import time

async def machine_a_cycle() -> None:
    cycle = 1
    while True:
        print(f'{cycle} Cykl maszyny A')
        cycle += 1
        await asyncio.sleep(2)


async def machine_b_cycle() -> None:
    cycle = 1
    while True:
        print(f'{cycle} Cykl maszyny B')
        cycle += 1
        await asyncio.sleep(3)


async def machine_c_cycle() -> None:
    cycle = 1
    while True:
        print(f'{cycle} Cykl maszyny C')
        cycle += 1
        await asyncio.sleep(5)


async def start_factory() -> None:
    print('Otwieranie fabryki')

    group = asyncio.gather(
        machine_a_cycle(),
        machine_b_cycle(),
        machine_c_cycle()
    )

    return group


async def stop_factory(machines) -> None:
    await asyncio.sleep(15)
    machines.cancel()


async def handle_factory() -> None:
    machines = await start_factory()

    await asyncio.gather(
        machines,
        stop_factory(machines)
    )


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(handle_factory())

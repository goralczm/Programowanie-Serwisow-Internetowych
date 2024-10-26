import asyncio


async def start_kitchen() -> None:
    print('Do roboty chłopaki, mamy dużo zamówień!')
    await asyncio.gather(
        prepare_scrambled_eggs(),
        prepare_omlet(),
        prepare_sandwich()
    )
    print('Koniec na dzisiaj, dobra robota. Do jutra!')


async def chop(what: str) -> None:
    await asyncio.sleep(2)
    print(f'Pokrojono {what}')


async def cook(what: str) -> None:
    await asyncio.sleep(5)
    print(f'Ugotowano {what}')


async def fry(what: str) -> None:
    await asyncio.sleep(3)
    print(f'Usmażono {what}')


async def combine(what: str) -> None:
    print(f'Połączono {what}')


async def prepare_scrambled_eggs() -> None:
    await chop('cebula')
    await cook('pokrojona cebula')
    await combine('pokrojona cebula i jajka')
    await fry('jajecznica')


async def prepare_sandwich() -> None:
    await chop('chleb')
    await chop('chleb')
    await chop('szynka')
    await chop('ser')
    await combine('chleb, szynke i ser')
    await fry('tost z szynką i serem')


async def prepare_omlet() -> None:
    await chop('papryka')
    await chop('cebula')
    await combine('pokrojoną paprykę, cebulę i jajka')
    await fry('omlet z warzywami')


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(start_kitchen())

import asyncio


async def read_file(file_name: str) -> None:
    await asyncio.sleep(2)
    print(f'Wczytywanie pliku {file_name} zakończono')


async def analyse_file(file_name: str) -> None:
    await asyncio.sleep(4)
    print(f'Analiza pliku {file_name} zakończona')


async def save_file(file_name: str) -> None:
    await asyncio.sleep(1)
    print(f'Zapisywanie pliku {file_name} zakończone')


async def process_file(file_name: str) -> None:
    await read_file(file_name)
    await analyse_file(file_name)
    await save_file(file_name)


async def mock_processing_files() -> None:
    await asyncio.gather(
        process_file('Plik 1'),
        process_file('Plik 2'),
        process_file('Plik 3')
    )


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(mock_processing_files())
        
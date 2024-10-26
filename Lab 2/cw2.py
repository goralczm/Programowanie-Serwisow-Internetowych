import aiohttp
import asyncio


async def add_user(url: str, body: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=body) as response:
            return await response.json()


async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    body = {
        "name": "Nowy Użytkownik",
        "avatar": "https://i.sstatic.net/l60Hf.png",
    }

    user = await add_user(url=url, body=body)
    print(user)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

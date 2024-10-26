import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def print_weather_forecast(city: str, latitude: float, longitude: float) -> None:
    res = await fetch(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone=auto&current=temperature_2m,wind_speed_10m,relative_humidity_2m')

    temperature = res['current']['temperature_2m']
    wind_speed = res['current']['wind_speed_10m']
    relative_humidity = res['current']['relative_humidity_2m']

    print(f'Pogoda dla {city} w tym momencie:')
    print(f'Temperature: {temperature}℃')
    print(f'Prędkość Wiatru: {wind_speed} km/h')
    print(f'Wilgotność: {relative_humidity}%')


async def main() -> None:
    await print_weather_forecast('Zakopane', 49.299, 19.9489)


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

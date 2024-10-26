import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def weather_forecast(city: str, latitude: float, longitude: float) -> dict:
    res = await fetch(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone=auto&current=temperature_2m,wind_speed_10m,relative_humidity_2m')

    temperature = res['current']['temperature_2m']
    wind_speed = res['current']['wind_speed_10m']
    relative_humidity = res['current']['relative_humidity_2m']

    return {city: [temperature, wind_speed, relative_humidity]}


def print_weather_forecast(weather_forecast_data: dict) -> None:
    city = list(weather_forecast_data.keys())[0]
    print(f'Pogoda dla {city} w tym momencie:')
    print(f'Temperature: {weather_forecast_data[city][0]}℃')
    print(f'Prędkość Wiatru: {weather_forecast_data[city][1]} km/h')
    print(f'Wilgotność: {weather_forecast_data[city][2]}%')


async def main() -> None:
    res = await asyncio.gather(weather_forecast('Porlamar', 10.57, 63.51),
                               weather_forecast('Moroni', 11.42, 43.15),
                               weather_forecast('Helsinki', 60.10, 24.56))

    for data in res:
        print_weather_forecast(data)
        print("")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

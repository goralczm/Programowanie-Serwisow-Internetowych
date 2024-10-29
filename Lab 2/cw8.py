import aiohttp
import asyncio


TEMPERATURE = 'temperature_2m'
WIND_SPEED = 'wind_speed_10m'
RELATIVE_HUMIDITY = 'relative_humidity_2m'


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def weather_forecast(city: str, latitude: float, longitude: float) -> dict:
    res = await fetch(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone=auto&current=temperature_2m,wind_speed_10m,relative_humidity_2m')

    temperature = res['current'][TEMPERATURE]
    wind_speed = res['current'][WIND_SPEED]
    relative_humidity = res['current'][RELATIVE_HUMIDITY]

    return {city: {
        TEMPERATURE: temperature,
        WIND_SPEED: wind_speed,
        RELATIVE_HUMIDITY: relative_humidity
    }}


def valid_forecast(weather_forecast_data: dict, filter: dict = {}) -> bool:
    city = list(weather_forecast_data.keys())[0]
    city_forecast = weather_forecast_data[city]

    for key in city_forecast:
        if key in filter and not eval(f'{city_forecast[key]} {filter[key]}'):
            return False

    return True


def print_weather_forecast(weather_forecast_data: dict) -> None:
    city = list(weather_forecast_data.keys())[0]
    city_forecast = weather_forecast_data[city]

    print(f'Pogoda dla {city} w tym momencie:')
    print(f'Temperature: {city_forecast[TEMPERATURE]}℃')
    print(f'Prędkość Wiatru: {city_forecast[WIND_SPEED]} km/h')
    print(f'Wilgotność: {city_forecast[RELATIVE_HUMIDITY]}%')


async def main() -> None:
    results = await asyncio.gather(weather_forecast('Porlamar', 10.57, 63.51),
                               weather_forecast('Moroni', 11.42, 43.15),
                               weather_forecast('Helsinki', 60.10, 24.56))


    for data in res:
        if valid_forecast(data):
            print_weather_forecast(data)
            print("")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())

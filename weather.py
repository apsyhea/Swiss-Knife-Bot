import aiohttp
import tokens
import flag
import datetime
from aiogram.types import Message


W_TOKEN = tokens.weather_token

async def weather(message: Message):
    city = message.get_args()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={W_TOKEN}&units=metric") as   response:
            if response.status != 200:
                await message.reply("Sorry, I couldn't find the weather for that city. Please try again.")
                return
 
            data = await response.json()
            tz_offset = datetime.timedelta(seconds=data["timezone"])
            utc_time = datetime.datetime.utcnow()
            local_time = utc_time + tz_offset
            stats_str = f'{flag.flag(data["sys"]["country"])} {local_time:%Y-%m-%d} | {local_time:%H:%M:%S}\n'
            stats_str += f'🌤️ Weather in {data["name"]}, \n'
            stats_str += f'🌡️ Temperature: {data["main"]["temp"]}°C\n'
            stats_str += f'☁️ Description: {data["weather"][0]["description"].title()}\n'
            stats_str += f'💨 Wind Speed: {data["wind"]["speed"]} m/s'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

            await message.reply(f'<b>{stats_str}\n\n💻 Dev: @apsyhea</b>', parse_mode="HTML") 
import aiohttp

from datetime import datetime
from aiogram.types import Message
from secret.token import api_token


async def get_gweather(message: Message, city):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_token}&units=metric&lang=ru"
            async with session.get(url, ssl=False) as response:
                data = await response.json()
                city = data["name"]
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                desc = data["weather"][0]["description"]
                wind = data["wind"]["speed"]
                country = data["sys"]["country"]
                sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
                sunset = datetime.fromtimestamp(data["sys"]["sunset"])
                text = (
                    f"Город - {city} [{country}]\n"
                    f"Температура сейчас: {temp}°C\n"
                    f"Погода сейчас: {desc.capitalize()}\n"
                    f"Влажность: {humidity}%\n"
                    f"Сила ветра: {wind}м/с"
                )
                if sunrise > datetime.now():
                    text += f"\nСледующий восход в {sunrise}"
                if sunset > datetime.now():
                    text += f"\nСледующий закат в {sunset}"

                await message.answer(text + ".")
    except Exception as error:
        print(error)
        await message.answer("Ошибка, проверьте название города")

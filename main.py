import asyncio
from aiogram import Bot, Dispatcher
from secret.token import TOKEN
from apps import handlers, callbacks

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers.router, callbacks.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("rise is sleep")

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from database.crud import init_db

from handlers import start, instagram

logging.basicConfig(level=logging.INFO)



async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(instagram.router)

    init_db()
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
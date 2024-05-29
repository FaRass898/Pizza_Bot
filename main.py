import asyncio
import logging
from aiogram import Bot

from config import dp, bot, set_commands, database
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.pizza import pizza_router
from handlers.nuggets import nuggets_router
from handlers.milkshakes import milkshakes_router
from handlers.survey import survey_router
from handlers.apartment_search import apartment_router

async def on_startup(bot: Bot) -> None:
    await database.create_tables()



async def main():

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(pizza_router)
    dp.include_router(nuggets_router)
    dp.include_router(milkshakes_router)
    dp.include_router(survey_router)
    dp.include_router(apartment_router)


    await set_commands()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

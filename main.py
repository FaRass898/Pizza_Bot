import asyncio
from config import dp, bot, set_commands
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.pizza import pizza_router
from handlers.nuggets import nuggets_router
from handlers.milkshakes import milkshakes_router
from handlers.survey import survey_router

async def main():

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(pizza_router)
    dp.include_router(nuggets_router)
    dp.include_router(milkshakes_router)
    dp.include_router(survey_router)

    await set_commands()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

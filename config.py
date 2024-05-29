from aiogram import Bot, Dispatcher, types
from os import getenv
from dotenv import load_dotenv
from database.database import Database
from pathlib import Path

load_dotenv()
database = Database(Path('__file__').parent / 'db.sqlite')


dev = getenv("DEV",0)
if not dev:
    from aiogram.client.session.aiohttp import AiohttpSession
    print("started on server")
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("TOKEN"), session=session)
else:
    print("started on dev")
    bot = Bot(token=getenv("TOKEN"))

dp = Dispatcher()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='начало'),
        types.BotCommand(command='stop', description='конец опроса'),
        types.BotCommand(command='search', description='поиск квартиры')

    ])

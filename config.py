from aiogram import Bot, Dispatcher, types
from os import getenv
from dotenv import load_dotenv
from database.database import Database
from pathlib import Path


database = Database(Path('__file__').parent / 'db.sqlite')



load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='начало'),
        types.BotCommand(command='stop', description='конец опроса')

    ])

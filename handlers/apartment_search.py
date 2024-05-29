from aiogram import Router,F, types
from aiogram.filters import Command
from crawler.house_kg import HouseCrawler

apartment_router = Router()

@apartment_router.message(Command("search"))
async def search(message: types.Message):
    crawler = HouseCrawler()
    page = crawler.get_page()
    links = crawler.get_links(page)
    for link in links:
        await message.answer(link)

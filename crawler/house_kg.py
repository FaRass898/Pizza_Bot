import httpx
from parsel import Selector


class HouseCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    async def get_page(self, url: str):
        response = await httpx.get(self.MAIN_URL)
        print(response.status_code)
        return response.text

    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("div.listing a::attr(href)").getall()
        links = list(map(lambda x: self.BASE_URL + x, links))
        return links



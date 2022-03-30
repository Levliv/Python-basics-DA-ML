from bs4 import BeautifulSoup
import aiohttp
import asyncio

url = "https://www.thisfuckeduphomerdoesnotexist.com"


async def get_image_links():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            images = soup.find_all("img")
            for image in images:
                if image.get("id") == ["image-payload"]:
                    return image.get("src")


async def get_image_by_link(link: str, filename: str):
    with urlopen(link) as img, open(filename, "wb") as file:
        copyfileobj(img, file)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_image_links())
print(loop)

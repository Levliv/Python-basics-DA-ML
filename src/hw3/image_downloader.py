from bs4 import BeautifulSoup
import aiohttp
import asyncio

url = "https://www.thisfuckeduphomerdoesnotexist.com"


async def get_image_links():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            images = soup.find_all("img")
            for image in images:
                if image.get("id") == ["image-payload"]:
                    return image.get("src")


loop = asyncio.get_event_loop()
loop.run_until_complete(get_image_links())
print(loop)

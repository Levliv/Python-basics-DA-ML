from bs4 import BeautifulSoup
import aiohttp
import asyncio
import os
from urllib.request import urlopen
from shutil import copyfileobj


async def get_image_link():
    url = "https://www.thisfuckeduphomerdoesnotexist.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            images = soup.find_all("img")
            for image in images:
                if image.get("class") == ["image-payload"]:
                    return image["src"]


async def get_image_by_link(link: str, filename: str):
    with urlopen(link) as img, open(filename, "wb") as file:
        copyfileobj(img, file)


async def get_image():
    link = await get_image_link()
    label = link.split("/")[-1]
    await get_image_by_link(link, f"data/{label}")


def downloader(cli: int):
    directory_name = "data"
    if os.path.isdir(directory_name):
        for file in os.listdir(directory_name):
            os.remove(f"{directory_name}/{file}")
    else:
        os.mkdir(directory_name)
    loop = asyncio.get_event_loop()
    group = asyncio.gather(*[loop.create_task(get_image()) for _ in range(cli)])
    loop.run_until_complete(group)
    print(f"downloaded {cli} photos successfully, find them in \'data\' directory")
    return directory_name

downloader(4)

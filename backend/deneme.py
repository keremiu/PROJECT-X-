from pornhub_api import PornhubApi

api = PornhubApi()

import asyncio

from pornhub_api.backends.aiohttp import AioHttpBackend


async def execute():
    async with AioHttpBackend() as backend:
        api = PornhubApi(backend=backend)
        video = await api.video.get_by_id("ph560b93077ddae")
        print(video.title)

asyncio.run(execute())

videos = api.search.search_videos(
    "Elsa Jean",
    ordering="mostviewed",
    period="weekly",
    tags=["white"],
)
for vid in videos:
    print(vid.title, vid.video_id, vid.url)
    
stars = api.stars.all()

name_file = open("foo.txt", "w", encoding="utf-8")

for star in stars.stars:
    name_file.write(f"{star.star.star_name}\n")

name_file.close()    
from pornhub_api import PornhubApi

import random

from model import Query

from pornhub_api.backends.aiohttp import AioHttpBackend

api_instance = None


async def get_api():
    global api_instance
    if api_instance is None:
        backend = AioHttpBackend()  # Oturum açık tutuluyor
        api_instance = PornhubApi(backend=backend)
    return api_instance

# İçe aktarmalar ve global değişkenler

async def fetch_video_data(query: Query):
    global api_instance  
    if api_instance is None:
        await get_api()  

    videos = await api_instance.search.search_videos(
        query.name,
        ordering=query.ordering,
        period=query.period,
        tags=query.tags
    )
    video_list = [video for video in videos]  # videos iterable'ını bir listeye dönüştür

    if video_list:
        # Return a random video
        selected_video = random.choice(video_list)  # Listeden rastgele bir video seç
        return {
            "title": selected_video.title,
            "url": selected_video.url
        }
    else:
        # Return a message if no videos are found
        return {"message": "No videos found"}

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

    # API çağrısında kullanılacak parametreleri hazırla
    search_params = {}
    if query.name:
        search_params["q"] = query.name
    if query.ordering:
        search_params["ordering"] = query.ordering
    if query.period:
        search_params["period"] = query.period
    if query.tags:
        search_params["tags"] = query.tags

    videos = await api_instance.search.search_videos(**search_params)
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


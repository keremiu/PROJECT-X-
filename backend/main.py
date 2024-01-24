from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
#from Scrapper import run_scrapper  
#from fastapi_utils.tasks import repeat_every

from model import Query
from generator import fetch_video_data, get_api
app = FastAPI()
origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/api/Query")
async def create_item(item: Query):
    video_data = await fetch_video_data(item)
    return video_data

@app.on_event("startup")
async def startup_event():
    # Initialize the API at startup
    await get_api()
    
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=3000)
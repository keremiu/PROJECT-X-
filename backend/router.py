from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
#from Scrapper import run_scrapper  
#from fastapi_utils.tasks import repeat_every

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

@app.get("/api/results")
async def get_teams():
    responses = []
    for name in names:
        response = await fetch_all_teams(name)
        response = (name, response)
        responses.append(response)
    return responses
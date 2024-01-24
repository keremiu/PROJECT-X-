from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from model import Query
from generator import fetch_video_data, get_api

app = FastAPI()

# CORS için tüm kökenlere izin ver
origins = ["*"]

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
    # Tüm ağ arayüzlerinden erişime izin ver
    uvicorn.run(app, host="0.0.0.0", port=3000)

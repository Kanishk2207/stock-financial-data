from os import environ as env

from fastapi import FastAPI

from routers import data_injestion

app = FastAPI()

app.include_router(data_injestion.router)

@app.get('/', tags=['base'])
async def root():
    return {
        "message": "welcome to the app"
    }
from fastapi import FastAPI
from app.auth import router as auth_router
from app.routes import router as scraper_router

import webbrowser
import threading
import time


app = FastAPI(
    title="Amazon Price Updater",
    version="2.0.0"
)


app.include_router(auth_router)

app.include_router(scraper_router)



def open_browser():

    time.sleep(2)

    webbrowser.open(
        "http://127.0.0.1:8000"
    )


@app.on_event("startup")
async def startup_event():

    threading.Thread(
        target=open_browser
    ).start()
from fastapi import FastAPI

from src.config import read_config
import uvicorn

from src.models import db_connect, db_disconnect
from src.views import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = read_config()
    db_connect(config.DATABASE_URL)
    yield
    db_disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")

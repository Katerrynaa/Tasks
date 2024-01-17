from fastapi import FastAPI

from src.config import read_config
import uvicorn

from src.models import db_connect, db_disconnect
from src.views import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):  # pragma: no cover
    config = read_config()
    db_connect(config.DATABASE_URL)
    yield
    db_disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


# @app.on_event("startup")
# def startup():
#     config = read_config()
#     db_connect(config.DATABASE_URL)
#
#
# @app.on_event("shutdown")
# def shutdown():
#     db_disconnect()



if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")

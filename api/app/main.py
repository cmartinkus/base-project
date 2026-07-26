from fastapi import FastAPI

from app.api.router import router
from api.app.config import configure_logging


configure_logging()

app = FastAPI()

app.include_router(router)
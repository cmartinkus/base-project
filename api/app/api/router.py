from fastapi import APIRouter

from app.api.endpoints import health
from app.api.endpoints import users

router = APIRouter()

router.include_router(health.router)

router.include_router(users.router)
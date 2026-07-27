from fastapi import APIRouter

from api.endpoints import health
from api.endpoints import users

router = APIRouter()

router.include_router(health.router)

router.include_router(users.router)
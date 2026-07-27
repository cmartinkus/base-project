from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db, get_user_service
from repositories.user_repository import UserRepository
from services.user_service import UserService
from schemas.users import (
    UserCreate,
    UserResponse,
)
router = APIRouter()


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return service.get_users()

@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service),
):

    return service.create_user(user)
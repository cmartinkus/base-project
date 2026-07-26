from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_user_service
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter()


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return service.get_users()
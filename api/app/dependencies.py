from app.database.session import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_user_service(
    db: Session = Depends(get_db),
) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)
from sqlalchemy.orm import Session

from app.database.models import User


class UserRepository:

    def __init__(self, db: Session):

        self.db = db

    def get_all(self):

        return self.db.query(User).all()
from repositories.user_repository import UserRepository
from schemas.users import UserCreate

class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def create_user(self, user: UserCreate):

        if self.repository.email_exists(user.email):
            raise DuplicateEmailException()

        return self.repository.create(
            name=user.name,
            email=user.email,
        )

    def get_users(self):

        return self.repository.get_all()
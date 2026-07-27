from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def create_user(self, request: CreateUserRequest):

        if self.repository.email_exists(request.email):
            raise DuplicateEmailException()

        password = hash_password(request.password)

        user = User(
            name=request.name,
            email=request.email,
            password=password,
        )

        self.repository.save(user)

        send_email(user.email)

        return user

    def get_users(self):

        return self.repository.get_all()
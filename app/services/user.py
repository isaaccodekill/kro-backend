from app.models.user import User
from app.repository.user import UserRepository
from app.schemas import CreateUser


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_email(email)

    def create_user(self, user: CreateUser, password_hash):
        new_user = User(
            email=user.email,
            hashed_password=password_hash,
            first_name=user.first_name,
            last_name=user.last_name
        )
        return self.user_repo.create(new_user)

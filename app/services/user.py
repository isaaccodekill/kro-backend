from app.repository.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def create_user(self, user):
        return self.user_repo.create(user)


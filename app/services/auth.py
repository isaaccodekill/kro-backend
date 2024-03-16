from app.models.user import User
from app.schemas import CreateUser, User as UserSchema
from app.services.user import UserService
from app.utils.auth import verify_password, get_password_hash, create_token
from fastapi import HTTPException



class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def login(self, email: str, password: str):
        user: User = self.user_service.get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=400, detail="{description: 'Bad login credentials'}")

        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail="{description: 'Bad login credentials'}")

        return create_token({"sub": user.email}),


    def register(self, user_data: CreateUser):
        user: User = self.user_service.get_user_by_email(user_data.email)
        if user is not None:
            raise HTTPException(status_code=400, detail="{description: 'User already exists'}")
        new_user: User = self.user_service.create_user(user_data, get_password_hash(user_data.password))
        # seed transactions for the user

        return new_user

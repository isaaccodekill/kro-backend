from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from repository.user import UserRepository
from services.user import UserService


def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db_session=Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository)

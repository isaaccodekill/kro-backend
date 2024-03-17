from fastapi import Depends, Request, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.repository.transaction import TransactionRepository
from app.services.auth import AuthService
from app.repository.user import UserRepository
from app.services.transaction import TransactionService
from app.services.user import UserService
from app.utils.auth import decode_token


def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_transaction_repository(db_session=Depends(get_db_session)) -> TransactionRepository:
    return TransactionRepository(db_session)


def get_transaction_service(
        transaction_repository: TransactionRepository = Depends(get_transaction_repository)) -> TransactionService:
    return TransactionService(transaction_repository)


def get_user_repository(db_session=Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository)


def get_auth_service(user_service: UserService = Depends(get_user_service)) -> AuthService:
    return AuthService(user_service)


async def get_current_user(request: Request):
    token = request.cookies.get("token")
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # decode token and get user_id
    user_id = decode_token(token).get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user_id

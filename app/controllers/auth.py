from fastapi import APIRouter, Depends, Response, HTTPException
from app.schemas import LoginUser, User, CreateUser

from app.services.auth import AuthService
from app.dependecies import get_auth_service, get_user_service
from app.services.user import UserService

router = APIRouter()


@router.post("/login")
async def login(data: LoginUser, response: Response, auth_service: AuthService = Depends(get_auth_service),
                user_service: UserService = Depends(get_user_service)):
    token = auth_service.login(data.email, data.password)
    print(token, "the token")
    if token is None:
        raise HTTPException(status_code=401, detail="Bad login credentials")

    user = user_service.get_user_by_email(data.email)
    if user is None:
        raise HTTPException(status_code=401, detail="Bad login credentials")

    user_response = User(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name
    )

    response.set_cookie(key="token", value=token, httponly=True, samesite="lax", max_age=1800 * 24)
    return {"description": "success", "user": user_response}


@router.post("/register")
async def register(register_data: CreateUser, auth_service: AuthService = Depends(get_auth_service)):
    auth_service.register(register_data)
    return {
        "description": "success",
    }


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="token")
    return {"description": "success"}
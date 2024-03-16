from fastapi import APIRouter, Depends, HTTPException, status

from app.dependecies import get_user_service
from app.services.user import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"},
               400: {"description": "Bad Request"},
               200: {"description": "Success", "user": "User"}
               }
)


@router.get("/profile")
async def get_profile(user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"description": "User not found"})
    return user


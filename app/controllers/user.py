from fastapi import APIRouter, Depends, HTTPException, status

from app.dependecies import get_user_service, get_current_user
from app.services.user import UserService

router = APIRouter()


@router.get("/profile")
async def get_profile(user_id: int = Depends(get_current_user), user_service: UserService = Depends(get_user_service)):
    # get the email from the token that's in the cookie
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"description": "User not found"})
    return user


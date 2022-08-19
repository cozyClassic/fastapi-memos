import bcrypt
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

user_router = APIRouter(
    
    responses={404: {"description": "Not found"}},
)

@user_router.post("/sign-in/{user_id}")
async def get_user_token(user_id:int):
    pass
    return "JWT TOKEN"

@user_router.post("/sign-up")
async def create_user():
    pass
    return "success"

@user_router.get("/")
async def test():
    return {"message": "Hello user Router"}
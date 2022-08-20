from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from .model import Memo
from .schema import MemoCreateSchema
from core.database.database import get_db
from core.helper.login import get_current_user

memo_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@memo_router.post("/")
async def create_memo(
    memo_create_schema:MemoCreateSchema,
    db:Session = Depends(get_db),
    token:str | None = Header(default=None)
    ):

    user_data = await get_current_user(token)
    if not user_data["success"]: 
        return user_data

    new_memo:Memo = Memo(
        title=memo_create_schema.title,
        content=memo_create_schema.content,
        author_id = int(user_data["user_id"]))
    
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)
    
    return new_memo


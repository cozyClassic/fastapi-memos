from fastapi import APIRouter, Depends, Header, Path, HTTPException, Query
from sqlalchemy.orm import Session

from core.users.model import User

from .model import Memo
from .schema import MemoCreateSchema, MemoGetSchema
from core.database.database import get_db
from core.helper.login import get_current_user
from core.helper.pages import PageInfo
from core.helper.constatns import USER_ID_1_SAMPLE_JWT

memo_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@memo_router.post("/")
async def create_memo(
    memo_create_schema:MemoCreateSchema,
    token:str = Header(description=f"sample JWT :{USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db),
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

@memo_router.get("/{memo_id}", response_model = MemoGetSchema)
async def get_memo_detail(
    memo_id:int = Path(default=1, ge=1),
    db:Session = Depends(get_db)
) -> MemoGetSchema:
    memo = db.query(Memo, User
        ).join(User
        ).with_entities(
            Memo.title,
            Memo.content,
            Memo.create_at,
            Memo.author_id,
            User.account.label("author_account")
        ).filter(Memo.id==memo_id, Memo.remove_at==None
        ).first()

    if not memo :
         raise HTTPException(status_code=404, detail="data not found")

    return memo

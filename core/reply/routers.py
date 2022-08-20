from datetime import datetime

from fastapi import APIRouter, Depends, Header, Path, HTTPException, Query
from sqlalchemy.orm import Session

from core.users.model import User

from .model import Reply
from .schema import ReplyCreateSchema, ReplyGetSchema, ReplyUpdateSchema
from core.memos.model import Memo
from core.database.database import get_db
from core.helper.login import get_current_user
from core.helper.pages import PageInfo
from core.helper.constants import USER_ID_1_SAMPLE_JWT

reply_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@reply_router.post("/{memo_id}")
async def create_reply(
    memo_id:int,
    memo_create_schema:ReplyCreateSchema,
    token:str = Header(description=f"sample JWT :{USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db),
    ) -> ReplyCreateSchema:

    user_data = await get_current_user(token)
    memo:Memo = db.query(Memo
        ).filter(Memo.id == memo_id, Memo.remove_at == None
        ).first()
    
    if not memo :
        raise HTTPException(status_code=404, detail="data not found")

    reply:Reply = Reply(
        content=memo_create_schema.content,
        memo_id = memo.id,
        author_id = int(user_data["user_id"]))
    
    db.add(reply)
    db.commit()
    db.refresh(reply)
    
    return reply

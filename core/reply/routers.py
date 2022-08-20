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

@reply_router.post("/{memo_id}", response_model= ReplyCreateSchema)
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

@reply_router.put("/{reply_id}", response_model = ReplyCreateSchema)
async def update_reply(
    update_memo:ReplyCreateSchema,
    reply_id:int,
    token:str = Header(description=f"sample JWT :{USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db),
    ):

    user_data = await get_current_user(token)

    old_reply:Reply = db.query(Reply
        ).filter(Reply.id==reply_id, Reply.remove_at==None
        ).first()
    
    if not old_reply:
        raise HTTPException(status_code=404, detail="data not found")
    
    if old_reply.author_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
    
    old_reply.content = update_memo.content
    
    db.add(old_reply)
    db.commit()
    db.refresh(old_reply)
    
    return old_reply


@reply_router.delete("/{reply_id}")
async def delete_reply(
    reply_id:int,
    token:str = Header(description=f"sample JWT :{USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db)
):
    
    user_data = await get_current_user(token)

    reply:Reply = db.query(Reply
        ).filter(Reply.id==reply_id, Reply.remove_at==None
        ).first()
    
    if not reply:
        raise HTTPException(status_code=404, detail="data not found")
    
    if reply.author_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
    
    reply.remove_at = datetime.now()

    db.add(reply)
    db.commit()
    db.refresh(reply)

    return {"success":True}

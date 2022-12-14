from datetime import datetime
import math

from fastapi import APIRouter, Depends, Header, Path, HTTPException, Query
from sqlalchemy.orm import Session, aliased

from .model import Memo
from .schema import MemoCreateSchema, MemoDetailSchema, MemoGetSchema, MemoUpdateSchema
from core.database.database import get_db
from core.users.model import User
from core.reply.model import Reply
from core.helper.login import get_current_user
from core.helper.constants import USER_ID_1_SAMPLE_JWT

memo_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@memo_router.post("/")
async def create_memo(
    memo_create_schema:MemoCreateSchema,
    token:str = Header(description=f"sample JWT @@ {USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db),
    ):

    user_data = await get_current_user(token)

    new_memo:Memo = Memo(
        title=memo_create_schema.title,
        content=memo_create_schema.content,
        author_id = int(user_data["user_id"]))
    
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)
    
    return new_memo

@memo_router.get("/{memo_id}", response_model = MemoDetailSchema)
async def get_memo_detail(
    memo_id:int = Path(default=1, ge=1),
    db:Session = Depends(get_db)
) -> MemoGetSchema:

    memo_author = aliased(User)
    reply_author= aliased(User)
    memo = db.query(Memo
        ).outerjoin(Memo.replies
        ).join(memo_author, Memo.author
        ).outerjoin(reply_author, Reply.author
        ).with_entities(
            Memo.title,
            Memo.content,
            Memo.create_at,
            Memo.author_id,
            Reply,
            memo_author.account.label("memo_author"),
            reply_author.account.label("reply_author")
        ).filter(Memo.id==memo_id, Memo.remove_at==None, Reply.remove_at == None
        ).all()

    if not memo :
        raise HTTPException(status_code=404, detail="data not found")

    if memo[0].Reply is None :
        return memo[0]

    _memo = dict(memo[0])
    
    _memo["replies"] = [{
        "reply_id": m.Reply.id,
        "content":m.Reply.content,
        "author_id":m.Reply.author_id,
        "reply_author":m.reply_author,
        "create_at": m.Reply.create_at
        } for m in memo]

    return _memo

@memo_router.get("/list/")
async def get_memo_list(
    page:int = Query(default=1, ge=1),
    db:Session = Depends(get_db)
):
    PAGE_SIZE = 20
    
    memo_query = db.query(Memo, User
        ).join(User
        ).with_entities(
            Memo.title,
            Memo.create_at,
            User.account.label("memo_author"),
        ).filter(Memo.remove_at==None)
    
    total_count = memo_query.count()
    total_page = math.ceil(total_count/PAGE_SIZE)
    page_end = page >= total_page
    memos = memo_query.offset(PAGE_SIZE*(page-1)
        ).limit(PAGE_SIZE
        ).all()

    return {
        "success" : True,
        "data":memos,
        "page_info":{
            "total_count":total_count,
            "total_page":total_page,
            "page_end":page_end,
        },
    }

@memo_router.patch("/{memo_id}", response_model = MemoCreateSchema)
async def update_memo(
    update_memo:MemoUpdateSchema,
    memo_id:int = Path(default=None, ge=1),
    token:str = Header(description=f"sample JWT @@ {USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db),
    ):

    user_data = await get_current_user(token)

    old_memo:Memo = db.query(Memo
        ).filter(Memo.id==memo_id, Memo.remove_at==None
        ).first()
    
    if not old_memo:
        raise HTTPException(status_code=404, detail="data not found")
    
    if old_memo.author_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
    
    if update_memo.title is not None:
        old_memo.title = update_memo.title
    if update_memo.content is not None:
        old_memo.content = update_memo.content
    
    db.add(old_memo)
    db.commit()
    db.refresh(old_memo)
    
    return old_memo


@memo_router.delete("/{memo_id}")
async def delete_memo(
    memo_id:int = Path(default=1, ge=1),
    token:str = Header(description=f"sample JWT @@ {USER_ID_1_SAMPLE_JWT}"),
    db:Session = Depends(get_db)
):
    user_data = await get_current_user(token)
    
    memo = db.query(Memo
        ).filter(Memo.id==memo_id, Memo.remove_at==None
        ).first()

    if not memo:
        raise HTTPException(status_code=404, detail="data not found")

    if memo.author_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
    
    memo.remove_at = datetime.now()

    db.add(memo)
    db.commit()
    db.refresh(memo)

    return {"success":True}

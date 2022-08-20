from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from jose import jwt

from .model import User
from .schema import UserSchema
from core.database.database import get_db
from core.config.secrets import SECRET_KEY, ALGORITHM, pwd_context
from core.helper.constants import DATE_TIME_FORM

user_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@user_router.post("/sign-in/")
async def get_user_token(
    user_schema:UserSchema,
    db:Session = Depends(get_db)
    ):
    account = user_schema.account.lower()
    password = user_schema.password

    user:User = db.query(User).filter_by(
        account = account
    ).first()

    if user is not None and pwd_context.verify(password, user.password):
        expire_date = (datetime.now() + timedelta(days=1)).strftime(DATE_TIME_FORM)
        encoded_jwt = jwt.encode({"user_id":user.id, "expire_at":expire_date}, SECRET_KEY, ALGORITHM)

        return {"success":True, "data":{"token":encoded_jwt}}

    return {"success:" : False, "data": {"account/password is wrong"}}

@user_router.post("/sign-up")
async def create_user(
    user_schema:UserSchema,
    db:Session = Depends(get_db)
    ):
    """account는 영문/숫자로만 3글자 이상이어야 함.
    password는 6글자 이상이어야 함."""
    account = user_schema.account.lower()
    password = user_schema.password

    duplicated_user = db.query(User).filter_by(
        account= account
    ).first()
    if duplicated_user is not None :
        return {"success" : False, "data": "account duplicated"}
    
    new_user = User(
        account = account,
        password = pwd_context.hash(password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success":True, "data":{"user_id":new_user.id}}

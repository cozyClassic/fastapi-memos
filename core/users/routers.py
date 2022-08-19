from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from .model import User
from .schema import UserSchema
from core.database.database import get_db
from core.config.secrets import SECRET_KEY, ALGORITHM, pwd_context

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
        encoded_jwt = jwt.encode({"user_id":user.id}, SECRET_KEY, ALGORITHM)
        expire_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        return {"success":True, "data":{"token":encoded_jwt, "expire_at":expire_date}}

    return {"success:" : False, "data": {"account/password is wrong"}}

@user_router.post("/sign-up")
async def create_user(
    user_schema:UserSchema,
    db:Session = Depends(get_db)
    ):
    # 0. 자동변환 : 계정은 소문자로 일괄 치환
    account = user_schema.account.lower()
    password = user_schema.password

    # 1. 밸리데이션
    # 계정은 소문자(자동변환)+숫자만. 3글자 이상
    # 비밀번호는 6글자 이상, 72글자(72bytes)이하

    # 2. 계정 중복 검색
    duplicated_user = db.query(User).filter_by(
        account= account
    ).first()
    if duplicated_user is not None :
        return {"success" : False, "data": "account duplicated"}
    
    # 3. 계정 생성
    new_user = User(
        account = account,
        password = pwd_context.hash(password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success":True, "data":{"user_id":new_user.id}}

@user_router.get("/")
async def test():
    return {"message": "Hello user Router"}

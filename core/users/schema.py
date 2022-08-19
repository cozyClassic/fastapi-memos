from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int | None = None
    account: str
    
    class Config:
        title = "사용자 정보"
        orm_mode = True

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    user_id: int
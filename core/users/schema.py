from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    account: str = Field(default=None, min_length=3, max_length=30)
    password: str = Field(default=None, min_length=6, max_lnegth=30)
    
    class Config:
        title = "계정, 비밀번호"
        orm_mode = True

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    user_id: int
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    account: str = Field(
        default="user01",
        min_length=3,
        max_length=30,
        regex="^[A-Za-z0-9]{3,50}$"
    )

    password: str = Field(
        default="123456",
        min_length=6,
        max_lnegth=30,
        regex="(?=.{6,})"
    )
    class Config:
        title = "계정, 비밀번호"
        orm_mode = True

from pydantic import BaseModel

from core.helper.author import AuthorSchema

class MemoCreateSchema(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True

class MemoUpdateSchema(MemoCreateSchema):
    title: str|None
    content: str|None

class MemoGetSchema(AuthorSchema, MemoCreateSchema):
    pass

from pydantic import BaseModel

from core.helper.author import AuthorSchema
from core.reply.schema import ReplyGetSchema

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

class MemoDetailSchema(MemoGetSchema):
    replies: list[ReplyGetSchema] | None = None

from pydantic import BaseModel

from core.helper.author import AuthorSchema

class ReplyCreateSchema(BaseModel):
    content: str

    class Config:
        orm_mode = True

class ReplyGetSchema(AuthorSchema, ReplyCreateSchema):
    reply_id:int
    pass

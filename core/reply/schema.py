from pydantic import BaseModel

from core.helper.author import AuthorSchema

class ReplyCreateSchema(BaseModel):
    content: str

    class Config:
        orm_mode = True

class ReplyUpdateSchema(ReplyCreateSchema):
    content: str

class ReplyGetSchema(AuthorSchema, ReplyCreateSchema):
    pass

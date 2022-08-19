from pydantic import BaseModel

class MemoSchema(BaseModel):
    title: str
    content: str

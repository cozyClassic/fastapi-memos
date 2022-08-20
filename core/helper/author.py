from datetime import date, datetime

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    author: str
    author_id: int
    create_at: date | datetime

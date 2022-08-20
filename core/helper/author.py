from datetime import date, datetime

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    memo_author: str | None
    reply_author: str | None
    author_id: int
    create_at: date | datetime

from datetime import datetime, date
from pydantic import BaseModel

class AuthorSchema(BaseModel):
    author_account: str
    author_id: int
    create_at: date | datetime

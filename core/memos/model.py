from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from core.helper.timestamps import Removable
from core.database.database import Base

class Memo(Base, Removable):
    __tablename__ = "memo"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable = False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", back_populates = "memos")
    replies = relationship("Reply", back_populates = "memo")

    def __repr__(self):
        return f"title:{self.title}, create_at:{self.create_at}"

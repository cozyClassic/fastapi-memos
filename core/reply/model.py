from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from core.helper.timestamps import Removable
from core.database.database import Base

class Reply(Base, Removable):
    __tablename__ = "reply"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable = False)
    memo_id = Column(Integer, ForeignKey("memo.id"))
    author_id = Column(Integer, ForeignKey("user.id"))

    memo = relationship("Memo", back_populates = "replies")
    author = relationship("User", back_populates = "replies")

    def __repr__(self):
        return f"memo:{self.memo_id}, author:{self.author_id}"

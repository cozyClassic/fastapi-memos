from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    account = Column(String(100), unique=True, nullable = False)
    password = Column(String(100), nullable=False)

    memos = relationship("Memo", back_populates = "author")
    replies = relationship("Reply", back_populates = "author")

    def __repr__(self):
        return f"user:{self.account}"

from sqlalchemy import Column, Integer, String

from core.database.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    account = Column(String, nullable = False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"user:{self.id}"

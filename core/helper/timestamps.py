from datetime import datetime

from sqlalchemy import Column, DateTime

from core.database.database import Base

class Removable(Base):
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    remove_at = Column(DateTime, default=None, nullable=False)

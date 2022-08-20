from datetime import datetime

from sqlalchemy import Column, DateTime

# nullable=False로 실수해서 수동으로 DB Column 변경함.
# ALTER TABLE memo MODIFY COLUMN remove_at DATETIME NULL;
class Removable:
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    remove_at = Column(DateTime, default=None, nullable=True)

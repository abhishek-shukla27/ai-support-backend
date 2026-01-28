from sqlalchemy import Column, String
from sqlalchemy.dialects.sqlite import BLOB
import uuid

from app.db.database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    industry = Column(String, nullable=False)

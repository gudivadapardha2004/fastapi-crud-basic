import uuid
from sqlalchemy import Column, String, Integer
from database import Base

class Users(Base):
    __tablename__ = "users"

    userID = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(50))
    age = Column(Integer)
    password = Column(String(100))
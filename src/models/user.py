from models.base import Base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects import postgresql


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(postgresql.TEXT, nullable=False)

from sqlalchemy import Column, Integer, String
from .database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)

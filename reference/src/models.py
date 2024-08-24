from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel


class User(SQLModel):
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

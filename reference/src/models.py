from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel


# remove typing to get an error
class User(SQLModel):
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)

from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

from src.config import settings

engine = create_engine(settings.DATABASE_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    class Config:
        orm_mode = True


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", back_populates="recipes")
    ingredients = relationship("Ingredient", back_populates="recipe")

    class Config:
        orm_mode = True


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship("Recipe", back_populates="ingredients")
    quantity = Column(Integer)
    unit = Column(String)

    class Config:
        orm_mode = True

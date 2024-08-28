from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    recipes = relationship("Recipe", back_populates="user")

    class Config:
        orm_mode = True


recipe_ingredients = Table('recipe_ingredients', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id'), primary_key=True)
)

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", back_populates="recipes")
    ingredients = relationship("Ingredient", secondary=recipe_ingredients, back_populates="recipes")

    class Config:
        orm_mode = True


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe", secondary=recipe_ingredients, back_populates="ingredients")
    unit = Column(String)

    class Config:
        orm_mode = True

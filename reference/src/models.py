from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    class Config:
        orm_mode = True


class FoodRecipe(Base):
    __tablename__ = 'food_recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", back_populates="food_recipes")
    ingredients = relationship("Ingredients", back_populates="food_recipe")

    class Config:
        orm_mode = True


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    edited_name = Column(String)
    food_recipe_id = Column(Integer, ForeignKey('food_recipe.id'))
    food_recipe = relationship("FoodRecipe", back_populates="ingredients")

    class Config:
        orm_mode = True

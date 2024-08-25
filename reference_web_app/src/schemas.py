from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    email: str
    hashed_password: str

    class Config:
        orm_mode = True


class Ingredient(BaseModel):
    id: str
    name: str
    quantity: int
    unit: str

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    id: str
    name: str
    ingredients: List[Ingredient]

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: str
    password: str


class CreateFoodRecipe(BaseModel):
    name: str
    ingredients: List[str]


class CreateIngredient(BaseModel):
    name: str
    quantity: int
    unit: str

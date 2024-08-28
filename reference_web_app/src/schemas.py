from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: str
    password: str


class IngredientBase(BaseModel):
    id: int
    name: str
    unit: str | None

    class Config:
        from_attributes = True


class CreateIngredient(BaseModel):
    name: str
    unit: str


class RecipeBase(BaseModel):
    id: int
    name: str
    ingredients: List[IngredientBase]
    user: UserBase | None

    class Config:
        from_attributes = True


class CreateRecipe(BaseModel):
    name: str
    ingredient_ids: List[int]
    user_id: int | None = None

from typing import List
from sqlalchemy.orm import Session

from models import User, Recipe, Ingredient
from schemas import UserBase, Recipe, Ingredient, CreateUser, CreateFoodRecipe, CreateIngredient


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: CreateUser):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_ingredient(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()


def get_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ingredient).offset(skip).limit(limit).all()


def create_ingredient(db: Session, ingredient: CreateIngredient):
    db_ingredient = Ingredient(name=ingredient.name)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient


def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Recipe).offset(skip).limit(limit).all()


def create_recipe(db: Session, recipe: CreateFoodRecipe, ingredient_ids: List[int]):
    db_recipe = Recipe(name=recipe.name, description=recipe.description)
    db_recipe.ingredients = [get_ingredient(db, ingredient_id) for ingredient_id in ingredient_ids]
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

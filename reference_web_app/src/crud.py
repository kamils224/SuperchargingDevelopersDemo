from typing import List
from sqlalchemy.orm import Session

import src.models as models
import src.schemas as schemas


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.CreateUser) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_ingredient(db: Session, ingredient_id: int) -> models.Ingredient:
    return db.query(models.Ingredient).filter(models.Ingredient.id == ingredient_id).first()


def get_ingredients(db: Session, skip: int = 0, limit: int = 100) -> List[models.Ingredient]:
    return db.query(models.Ingredient).offset(skip).limit(limit).all()


def create_ingredient(db: Session, ingredient: schemas.CreateIngredient) -> models.Ingredient:
    db_ingredient = models.Ingredient(name=ingredient.name, unit=ingredient.unit)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient


def get_recipe(db: Session, recipe_id: int) -> models.Recipe:
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Recipe]:
    return db.query(models.Recipe).offset(skip).limit(limit).all()


def create_recipe(db: Session, recipe: schemas.CreateRecipe) -> models.Recipe:
    db_recipe = models.Recipe(name=recipe.name)
    db_recipe.ingredients = [get_ingredient(db, ingredient_id) for ingredient_id in recipe.ingredient_ids]
    db_recipe.user_id = recipe.user_id
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

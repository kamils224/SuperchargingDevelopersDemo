from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db

import src.schemas as schemas
import src.crud as crud


api_router = APIRouter()


@api_router.get("/hello-world")
def hello_world():
    return {"Hello": "World"}


@api_router.delete("/ingredient/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    crud.delete_ingredient(db, ingredient_id)
    return {"message": "Ingredient deleted"}


@api_router.delete("/recipe/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    crud.delete_recipe(db, recipe_id)
    return {"message": "Recipe deleted"}


@api_router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return {"message": "User deleted"}


@api_router.get("/ingredient/", response_model=list[schemas.IngredientBase])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ingredients = crud.get_ingredients(db, skip=skip, limit=limit)
    return ingredients


@api_router.get("/ingredient/{ingredient_id}", response_model=schemas.IngredientBase)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = crud.get_ingredient(db, ingredient_id)
    return ingredient


@api_router.get("/recipe/{recipe_id}", response_model=schemas.RecipeBase)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    return recipe


@api_router.get("/recipe/", response_model=list[schemas.RecipeBase])
def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    print(recipes[0].ingredients[0])
    return recipes


@api_router.get("/user/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return user


@api_router.get("/user/", response_model=list[schemas.UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@api_router.post("/ingredient/", response_model=schemas.IngredientBase)
def create_ingredient(ingredient: schemas.CreateIngredient, db: Session = Depends(get_db)):
    created_ingredient = crud.create_ingredient(db, ingredient)
    return created_ingredient


@api_router.post("/recipe/", response_model=schemas.RecipeBase)
def create_recipe(recipe: schemas.CreateRecipe, db: Session = Depends(get_db)):
    created_recipe = crud.create_recipe(db, recipe)
    return created_recipe


@api_router.post("/user/", response_model=schemas.UserBase)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    created_user = crud.create_user(db, user)
    return created_user


@api_router.put("/ingredient/{ingredient_id}", response_model=schemas.IngredientBase)
def update_ingredient(ingredient_id: int, ingredient: schemas.CreateIngredient, db: Session = Depends(get_db)):
    updated_ingredient = crud.update_ingredient(db, ingredient_id, ingredient)
    return updated_ingredient


@api_router.put("/recipe/{recipe_id}", response_model=schemas.RecipeBase)
def update_recipe(recipe_id: int, recipe: schemas.RecipeBase, db: Session = Depends(get_db)):
    updated_recipe = crud.update_recipe(db, recipe_id, recipe)
    return updated_recipe


@api_router.put("/user/{user_id}", response_model=schemas.UserBase)
def update_user(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)
    return updated_user

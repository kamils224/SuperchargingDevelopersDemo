from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/hello-world")
def hello_world():
    return {"Hello": "World"}


@api_router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
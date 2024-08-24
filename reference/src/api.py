from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/hello-world")
def hello_world():
    return {"Hello": "World"}

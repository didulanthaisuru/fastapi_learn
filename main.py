from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool=True

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/about")
def about():
    return {"info": "This is an API built with FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": "User found"}

@app.get("/search")
def search_users(name: str,age: int):
    return {"name": name, "age": age, "message": "User searched"}

@app.post("/users/")
def create_user(user: User):
    return {"message": "User created", "user": user}
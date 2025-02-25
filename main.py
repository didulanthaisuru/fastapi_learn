from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import User, Gender, Role  # Importing the User model and enums

# FastAPI app initialization
app = FastAPI()

# Sample in-memory database (List of users)
db: List[User] = [
    User(
        id=uuid4(),  # Generate a unique UUID for the user
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),  # Generate a unique UUID for the user
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

# Fetch all users (this will be accessible via /api)
@app.get("/api", response_model=List[User])
async def fetch_users():
    return db

# New user endpoint
@app.get("/new")
async def new_user():
    return {"message": "Create a new user"}

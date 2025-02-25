from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from enum import Enum

# Enum for Gender
class Gender(str, Enum):
    male = "male"
    female = "female"

# Enum for Role
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# User model definition
class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

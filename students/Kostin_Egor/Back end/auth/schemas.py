from pydantic import BaseModel
from fastapi_users import schemas
from datetime import datetime

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    login: str
    role_id: int
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    email: str
    username: str  
    class Config:
        from_attributes = True

class UserCreate(schemas.BaseUserCreate):
    email: str
    login: str
    password: str
    role_id: int

class CreateRole(BaseModel):
    id: int
    name: str
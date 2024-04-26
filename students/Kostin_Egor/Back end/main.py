from typing import List
from typing import Optional
from fastapi_users import fastapi_users
from fastapi import FastAPI, Depends, HTTPException
from auth.auth import auth_backend
from auth.database import get_async_session
from models.models import Role, User
from auth.schemas import UserRead, UserCreate,CreateRole
from auth.tools import fastapi_users, current_user, from_role_to_schema, from_user_to_schemas
from sqlalchemy.ext.asyncio import AsyncSession
from user.router import app as user
from application.aplic import app as Appl
from Service.router import app as Ser
app = FastAPI()

app.include_router(user)
app.include_router(Appl)
app.include_router(Ser)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.login}"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


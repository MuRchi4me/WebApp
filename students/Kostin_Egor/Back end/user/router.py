from typing import List
from typing import Optional
from fastapi_users import fastapi_users
from fastapi import APIRouter, FastAPI, Depends, HTTPException, Response
from auth.auth import auth_backend
from auth.database import get_async_session
from models.models import Role, User
from auth.schemas import UserRead, UserCreate,CreateRole
from auth.tools import fastapi_users, current_user, from_role_to_schema, from_user_to_schemas
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

app = APIRouter(
    prefix="/user",
    tags=["User"]
)

@app.get("/get_all_user")
async def get_all_user(user_id: Optional[int] = None, user: User = Depends(current_user),session: AsyncSession = Depends(get_async_session)) -> List[UserRead]:
    try:
        users = await User.get_all_user(session=session)
        if users == []:
            raise HTTPException(status_code=403, detail="Not found")
        posts: List[UserRead] = []
        if user_id == None:
            for i in users:
                post = from_user_to_schemas(i)
                posts.append(post)
        else:
            for i in users:
                if i.id == user_id:
                    post = from_user_to_schemas(i)
                    posts.append(post)
        return posts
    except Exception as e:
        raise e 

@app.post("/create_role")
async def create_role(role_name: str, session: AsyncSession = Depends(get_async_session)) -> CreateRole:
    role = await Role.get_role_by_name(role_name=role_name, session=session)
    if role != None:
        raise HTTPException(status_code=409, detail="Alredy exist")
    try:
        role = await Role.add_role(role_name, session)
        role_schema = from_role_to_schema(role)
        return role_schema
    except Exception as e:
        raise e

@app.get("/get_all_role")
async def get_all_role(session: AsyncSession = Depends(get_async_session)) -> list[CreateRole]:
    try:
        print = await Role.get_all_role(session)
        if print == []:
            raise HTTPException(status_code=403, detail="Not found")
        posts: List[CreateRole] = []
        for i in print:
            post = from_role_to_schema(i)
            posts.append(post)
        return posts    
    except Exception as e:
        raise e 

@app.get("/current")
async def get_current_user(user: User = Depends(current_user)) -> UserRead:
    return user

@app.get("/fff")
async def fff(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    if user.role_id != 1:
        raise  HTTPException(status_code=403, detail="Forbiden")

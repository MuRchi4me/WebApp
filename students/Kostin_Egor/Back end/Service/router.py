from datetime import datetime
from typing import List
from typing import Optional
from fastapi_users import fastapi_users
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from application.schemas import UpdateAplic
from auth.auth import auth_backend
from auth.database import get_async_session
from models.models import Role, User
from auth.schemas import UserRead, UserCreate,CreateRole
from auth.tools import fastapi_users, current_user, from_role_to_schema, from_user_to_schemas
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Application, Attachment, AplSer, Service
from Outlook.outlook import Outlook
# from Outlook.main import ANUS
app = APIRouter(
    prefix="/service",
    tags=["service"]
)

#     POST

@app.post("/make_inactive")
async def make_inactive(id_service:int, session: AsyncSession = Depends(get_async_session)):
    asu = await Service.get_active_by_id(id_service=id_service, session=session)
    if asu == True:
        await Service.make_inactive(id_service=id_service, actives=False,session=session)
    else:
        await Service.make_inactive(id_service=id_service, actives=True,session=session)
    return 

@app.post("/add_service")
async def add_service(name:str,description:str,session: AsyncSession = Depends(get_async_session)):
    result=await Service.add_service(name=name,description=description,session=session)
    return result

#     GET

@app.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Service.get_all(session=session)
@app.get("/get_by_id")
async def get_by_id(id_service: int, session: AsyncSession = Depends(get_async_session)):
    return await Service.get_by_id(id_service, session=session)

#     PUT

@app.put("/update_service")
async def update_service(id_service:int,name: str, description:str, session: AsyncSession = Depends(get_async_session)):
    res = await Service.update_service(id_service=id_service, name=name, description=description,session=session)
    return res

#     DELETE

@app.delete("/delete_service")
async def delete_service(id_service: int, session: AsyncSession = Depends(get_async_session)):
    await Service.delete_service(id_service=id_service, session=session)
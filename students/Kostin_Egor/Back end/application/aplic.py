from datetime import datetime
from typing import List
from typing import Optional
from fastapi_users import fastapi_users
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from application.schemas import UpdateAplic, Done_Close_Aplic
from auth.auth import auth_backend
from auth.database import get_async_session
from models.models import Role, User
from auth.schemas import UserRead, UserCreate,CreateRole
from auth.tools import fastapi_users, current_user, from_role_to_schema, from_user_to_schemas
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Application, Attachment, AplSer
from Outlook.outlook import Outlook
from minio import Minio
import email.utils
import io
app = APIRouter(
    prefix="/aplication",
    tags=["Aplication"]
)

#     POST

@app.post("/make_apli")
async def make_aplic(session: AsyncSession = Depends(get_async_session)):
    try:
        mail = Outlook()
        mail.login('suppnmzxis@outlook.com','1234Test')
        mail.inbox()
        mail.read()
        client = Minio(endpoint="localhost:9000",   # адрес сервера
                    access_key='minio',          # логин админа
                    secret_key='minio124',       # пароль админа
                    secure=False)                # опциональный параметр, отвечающий за вкл/выкл защищенное TLS соединение
        apola = await Application.add_application(name = mail.mailsubject(),description= mail.mailbody(), customer= mail.mailfrom(), session=session)
        buckname="bucket"+str(apola)
        client.make_bucket(bucket_name=buckname) 
        for filename, data in mail.mailattachments():
                try:
                    client.put_object(
                        buckname,
                        filename,
                        io.BytesIO(data),
                        len(data)
                    )
                    url = client.presigned_get_object(
                            buckname,
                            filename,
                            expires=datetime.timedelta(hours=164)
                        )
                    await Attachment.add_attachment(url=url, id_application=apola, session=session)
                except Exception as err:
                    return err
    except Exception as e:
        return e
    
#    GET

@app.get("/get_all_file_for_aplic")
async def get_all_file_for_aplic(application_id: int, session: AsyncSession = Depends(get_async_session)):
    ala= await Attachment.get_by_id(application_id=application_id, session=session)
    return ala

#    PUT

@app.put("/accept_aplic")

async def accept_aplic(application: UpdateAplic, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    sup = await Application.accept_application(application_id=application.application_id, new_status=application.new_status.name, executor=user.id,work_start_at=datetime.utcnow(),session=session)
    for x in application.id_service:
        await AplSer.add_AplSer(application_id=application.application_id,service_id= x, session=session)
    mail = Outlook()
    mail.login('suppnmzxis@outlook.com','1234Test')
    sendermail = email.utils.parseaddr(sup)[1]
    sendername = email.utils.parseaddr(sup)[0]
    asuka = await Application.get_services_name_for_application(application_id=application.application_id, session=session)
    mail.sendEmail(sendermail, f"Ваша заявка принята с номером {application.application_id}" ,f"Уважаемый {sendername}, ваша заявка принята в работу.\nВам будут оказаны услуги:\n {'\n, '.join(map(str, asuka))}. \n C уважением {user.name}, почта для связи {user.email}")

@app.put("/done_aplic")
async def done_aplic(application: Done_Close_Aplic, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    sup = await Application.done_application(application_id=application.application_id, new_status=application.new_status.name, completed_at=datetime.utcnow(), session=session)
    mail = Outlook()
    mail.login('suppnmzxis@outlook.com','1234Test')
    sendermail = email.utils.parseaddr(sup)[1]
    sendername = email.utils.parseaddr(sup)[0]
    asuka = await Application.get_services_name_for_application(application_id=application.application_id, session=session)
    mail.sendEmail(sendermail, f"Ваша заявка с номером {application.application_id} завершена"  ,f"Уважаемый {sendername}, ваша заявка была обработана.\nВам были оказаны услуги:\n {'\n, '.join(map(str, asuka))}. \n C уважением {user.name}, почта для связи {user.email}")

@app.put("/close_aplic")
async def close_aplic(application: Done_Close_Aplic , user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    sup = await Application.done_application(application_id=application.application_id, new_status=application.new_status.name, completed_at=datetime.utcnow(), session=session)
    mail = Outlook()
    mail.login('suppnmzxis@outlook.com','1234Test')
    sendermail = email.utils.parseaddr(sup)[1]
    sendername = email.utils.parseaddr(sup)[0]
    asuka = await Application.get_services_name_for_application(application_id=application.application_id, session=session)
    mail.sendEmail(sendermail, f"Ваша заявка с номером {application.application_id} отклонена"  ,f"Уважаемый {sendername}, ваша заявка была отклонена. C уважением {user.name}, почта для связи {user.email}")

#     DELETE

@app.delete("/delete_application")
async def delete_application(id_application: int, session: AsyncSession = Depends(get_async_session)):
    await Application.delete_application(id_application=id_application, session=session)


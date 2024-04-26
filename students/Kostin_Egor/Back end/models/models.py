from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Boolean, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship, joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, insert, update, delete
metadata = MetaData()

class Base(DeclarativeBase):
    metadata = metadata

class Role(Base):
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    @staticmethod
    async def add_role(role_name: str, session: AsyncSession):
        stmt = insert(Role).values(name = role_name)
        await session.execute(stmt)
        await session.flush()
        query = select(Role).where(Role.name == role_name)
        result = (await session.execute(query)).scalar_one()
        return result
    @staticmethod
    async def get_all_role(session: AsyncSession):
        query = select(Role)
        result = (await session.execute(query)).scalars().all()
        return result
    @staticmethod
    async def get_role_by_name(role_name: str, session: AsyncSession):
        query = select(Role).where(Role.name==role_name)
        res = (await session.execute(query)).scalar_one_or_none()
        return res
    
class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    login: Mapped[str] = mapped_column(String, nullable=True)
    haswhed_password: Mapped[str] = mapped_column(String, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)

    @staticmethod
    async def get_all_user(session: AsyncSession):
        query = select(User)
        result = (await session.execute(query)).scalars().all()
        return result

    @staticmethod
    async def get_by_id(user_id: int, session: AsyncSession):
        query = select(User).filter(User.id_user == user_id)
        result = await session.execute(query).scalar_one_or_none()
        return result

    @staticmethod
    async def get_by_mail(user_mail: str, session: AsyncSession):
        query = select(User).filter(User.mail == user_mail)
        result = await session.execute(query)              
        return result

    @staticmethod
    async def get_users_by_role(role: str, session: AsyncSession):
        query = select(User).filter(User.role == role)
        result = await session.execute(query)
        return result.scalars().all()

    @staticmethod
    async def add_user(id_user: int, name: str, second_name: str, mail: str, role: str, session: AsyncSession):
        user = User(id_user=id_user, name=name, second_name=second_name, mail=mail, role=role)
        session.add(user)
        await session.flush()
        return user

class Service(Base):
    __tablename__ = "service"
    id_service: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)

    @staticmethod
    async def get_all(session: AsyncSession):
        query=select(Service)
        result = (await session.execute(query)).scalars().all()
        return result
    @staticmethod
    async def make_inactive(id_service:int, actives:bool, session: AsyncSession):
        query=update(Service).where(Service.id_service==id_service).values(is_active=actives)
        await session.execute(query)
    @staticmethod
    async def get_active_by_id(id_service: int, session: AsyncSession):
        query = select(Service).where(Service.id_service == id_service)
        result = (await session.execute(query)).scalar_one_or_none()
        return result.is_active
    @staticmethod
    async def get_by_id(id: int, session: AsyncSession):
       query = select(Service).where(Service.id_service == id)
       result = (await session.execute(query)).scalar_one_or_none()
       return result
    @staticmethod
    async def add_service(name: str, description: str, session: AsyncSession):
        stmt = insert(Service).values(name = name, description = description)
        await session.execute(stmt)
        await session.flush()
        query = select(Service).where(Service.name == name)
        result = (await session.execute(query)).scalar_one()
        return result
    @staticmethod
    async def update_service(id_service: int, name:str,description:str, session: AsyncSession):
        query= update(Service).where(Service.id_service==id_service).values(name=name, description=description)
        await session.execute(query)
        await session.flush()
        stmt = select(Service).where(Service.name==name)
        res = (await session.execute(stmt)).scalar_one_or_none()
        return res
    @staticmethod
    async def delete_service(id_service: int, session: AsyncSession):
        query= delete(Service).where(Service.id_service==id_service)
        await session.execute(query)
        await session.flush()

class Application(Base):
    __tablename__ = "application"
    id_application: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="OPEN")
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    work_start_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    completed_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    customer: Mapped[str] = mapped_column(String, nullable=False)
    id_executor: Mapped[User] = mapped_column(Integer, ForeignKey("user.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    

    @staticmethod
    async def get_all(session: AsyncSession): 
        query = select(Application)
        result = await session.execute(query).scalar().all()
        return result
    
    @staticmethod
    async def get_services_for_application(application_id: int, session: AsyncSession):
        # Выполняем запрос для соединения таблиц AplSer и Service
        stmt = select(Service).join(AplSer).filter(AplSer.application_id == application_id)
        result = await session.execute(stmt)
        # Получаем все услуги, принадлежащие данной заявке
        services = result.scalars().all()
        return services
    
    @staticmethod
    async def get_services_name_for_application(application_id: int, session: AsyncSession):
        # Выполняем запрос для соединения таблиц AplSer и Service
        stmt = select(Service.name).join(AplSer).filter(AplSer.application_id == application_id)
        result = await session.execute(stmt)
        # Получаем все услуги, принадлежащие данной заявке
        services = result.scalars().all()
        return services
    @staticmethod
    async def get_by_id(application_id: int, session: AsyncSession):
        query = select(Application).filter(Application.id_application == application_id)
        result = (await session.execute(query)).scalar_one_or_none()
        return result

    @staticmethod
    async def add_application(name: str, description: str, customer: int, session: AsyncSession):
        stmt = insert(Application).values(name=name, description=description, customer=customer)
        await session.execute(stmt)
        await session.flush()
        query = select(Application).where(Application.name==name, Application.description==description, Application.customer==customer)
        result = (await session.execute(query)).scalar()
        return result.id_application

    @staticmethod
    async def accept_application(application_id: int, new_status: str, executor: int,work_start_at: TIMESTAMP, session: AsyncSession):
        query = update(Application).where(Application.id_application == application_id).values(status=str(new_status), id_executor=executor,  work_start_at=work_start_at)
        await session.execute(query)
        await session.flush()
        stmt= select(Application.customer).where(Application.id_application == application_id)
        return (await session.execute(stmt)).scalar_one()
    
    @staticmethod
    async def done_application(application_id: int , new_status: str , completed_at: TIMESTAMP , session: AsyncSession):
        query = update(Application).where(Application.id_application == application_id).values(status=str(new_status), completed_at=completed_at)
        await session.execute(query)
        await session.flush()
        stmt= select(Application.customer).where(Application.id_application == application_id)
        return (await session.execute(stmt)).scalar_one()
    
    @staticmethod
    async def delete_application(id_application: int, session: AsyncSession):
        query= delete(Application).where(Application.id_application==id_application)
        await session.execute(query)
        quer= delete(AplSer).where(AplSer.application_id==id_application)
        await session.execute(quer)
        await session.flush()

class Attachment(Base):
    __tablename__ = "attachment"
    id_attachment: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    id_application: Mapped[Application] = mapped_column(Integer, ForeignKey('application.id_application', ondelete="CASCADE"))

    @staticmethod
    async def add_attachment(url: str, id_application: int, session: AsyncSession):
        stmt = insert(Attachment).values(url=url, id_application=id_application)
        await session.execute(stmt)
        await session.flush()
        # query = select(Attachment.id_attachment).where()
        return
    
    @staticmethod
    async def get_by_id(application_id: int, session: AsyncSession):
            query = select(Attachment.url).filter(Attachment.id_application == application_id)
            result = (await session.execute(query)).scalars().all()
            return result

class AplSer(Base):
    __tablename__ = "AplSer"
    application_id:Mapped[int] = mapped_column(Integer, ForeignKey("application.id_application", ondelete="CASCADE"), primary_key=True)
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("service.id_service", ondelete="CASCADE"), primary_key=True)

    @staticmethod
    async def add_AplSer(application_id: int, service_id: int, session: AsyncSession):
        create_post = insert(AplSer).values(application_id = application_id, service_id = service_id)
        await session.execute(create_post)
        await session.flush()
        return
# class ApplicationService(Base):
#     __tablename__ = "application_service"
#     application_id: Mapped[int] = mapped_column(Integer, ForeignKey('application.id_application', primary_key=True))
#     service_id: Mapped[int] = mapped_column(Integer, ForeignKey('service.id_service', primary_key=True))

# class ApplicationService(Base):
#     __tablename__ = "application_service"
#     application_id: Mapped[int] = mapped_column(
#         Integer,
#         ForeignKey('application.id_application', ondelete="CASCADE"),
#         primary_key=True
#     )
#     service_id: Mapped[int] = mapped_column(
#         Integer,
#         ForeignKey('service.id_service', ondelete="CASCADE"),
#         primary_key=True
#     )

#     @staticmethod
#     async def application_with_all_service(session: AsyncSession):
#         query=(
#             select(Application)
#             .options(joinedload(Application))
#             .options(selectinload(Service))
#         )
#         result = (await session.execute(query)).scalars().all()
#         return result
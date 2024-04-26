from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase, joinedload
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyBaseUserTable
from auth.database import async_db_session
from sqlalchemy import func
metadata = MetaData()
from typing import List, Optional

class Base(DeclarativeBase):
    metadata = metadata

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    login: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    status: Mapped[str] = mapped_column(String, nullable=False, default="Основатель")
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=True)
    company: Mapped["Company"] = relationship(back_populates="user")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    employee: Mapped[List["Employee"]] = relationship(back_populates="user")

    @staticmethod
    async def get_status(user_id: int, session: AsyncSession):
        query = select(User.status).where(User.id == user_id)
        result = (await session.execute(query)).scalar_one()
        return result
    
    @staticmethod
    async def get_id_by_email(email: str, session: AsyncSession):
        query = select(User).where(User.email == email)
        result = (await session.execute(query)).scalar_one()
        return result.id
    
    @staticmethod
    async def set_company_id(user_id: int, company_id: int, session: AsyncSession):
        stmt = update(User).where(User.id == user_id).values(company_id = company_id)
        await session.execute(stmt)
        await session.flush()
        query = select(User).where(User.id == user_id)
        result = (await session.execute(query)).scalar_one()
        return



class Employee(User, Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="employee")

    @staticmethod
    async def create(user_id: int, session: AsyncSession):
        stmt = insert(Employee).values(id = int(user_id))
        await session.execute(stmt)
        await session.flush()
        query = select(Employee).where(Employee.id == user_id).options(joinedload(Employee.user))
        result = (await session.execute(query)).scalar_one()
        return result

class Access(Base):
    __tablename__ = "access"
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), primary_key=True)

    @staticmethod
    async def add_publisher_access(employee_id: int, session: AsyncSession):
        create_post = insert(Access).values(employee_id = employee_id, role_id = 1)
        edit_post = insert(Access).values(employee_id = employee_id, role_id = 2)
        await session.execute(create_post)
        await session.execute(edit_post)
        await session.flush()
        return

class Role(Base):
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    @staticmethod
    async def add_role(role_name: str, session: AsyncSession):
        stmt = insert(Role).values(name = role_name)
        await session.execute(stmt)
        await session.flush()
        query = select(Role).where(Role.name == role_name)
        result = (await session.execute(query)).scalar_one()
        return result

class Company(Base):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    inn: Mapped[int] = mapped_column(Integer, nullable=False)
    registration: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped[List["User"]] = relationship(back_populates="company")
    post: Mapped[List["Post"]] = relationship(back_populates="company")

    @staticmethod
    async def create(name: str, inn: int, reg: str, session: AsyncSession):
        stmt = insert(Company).values(name = name, inn = inn, registration = reg)
        await session.execute(stmt)
        await session.flush()
        query = select(Company).where(Company.inn == inn)
        result = (await session.execute(query)).scalar_one()
        return result
    @staticmethod
    async def get_by_inn(inn: int, session: AsyncSession):
        query = select(Company).where(Company.inn == inn)
        result = (await session.execute(query)).scalar_one_or_none()
        return result

class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post_type: Mapped[str] = mapped_column(String, nullable=False)
    header: Mapped[str] = mapped_column(String, nullable=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    company: Mapped["Company"] = relationship(back_populates="post")
    sport_id: Mapped[int] = mapped_column(ForeignKey("sport.id"))
    sport: Mapped["Sport"] = relationship(back_populates="post")
    news: Mapped[List["News"]]= relationship(back_populates="post")
    forecast: Mapped[List["Forecast"]] = relationship(back_populates="post")
    type: Mapped[str] = mapped_column(String)
    __mapper_args__ = {'polymorphic_identity': 'post','polymorphic_on': type}

   

    @staticmethod
    async def get(post_id: int, session: AsyncSession):
        query = select(Post).where(Post.id == post_id).options(joinedload(Post.company)).options(joinedload(Post.sport)).order_by(Post.id.desc()).limit(1)
        result = (await session.execute(query)).scalar_one_or_none()
        return result
    
    @staticmethod
    async def create(company_id: int, sport_id: int, post_type: str, header: str, text: str, session: AsyncSession) -> "Post":
        stmt = insert(Post).values(post_type = str(post_type), header = str(header), text = str(text),\
                                        company_id = int(company_id), sport_id = int(sport_id), type = "post")
        await session.execute(stmt)
        await session.flush()
        query = select(Post).where(Post.company_id == company_id, Post.sport_id == sport_id).options(joinedload(Post.company)).options(joinedload(Post.sport)).order_by(Post.id.desc()).limit(1)
        result = (await session.execute(query)).scalar_one()
        return result
    
    @staticmethod
    async def update(id: int, session: AsyncSession, header: str, text: str):
        stmt = update(Post).where(Post.id == id).values(header = header, text = text)
        await session.execute(stmt)
        await session.flush()
        query = select(Post).where(Post.id == id).options(joinedload(Post.company)).options(joinedload(Post.sport)).order_by(Post.id.desc()).limit(1)
        result = (await session.execute(query)).scalar_one()
        return result
    
    @staticmethod
    async def delete(post_id: int, session: AsyncSession):
        stmt = delete(Post).where(Post.id == post_id)
        await session.execute(stmt)
        await session.flush() 
        return
    
    @staticmethod
    async def get_posts(early_date: Optional[datetime], late_date: Optional[datetime], limit: int, page: int, sport: list[int], company_id: int, search: Optional[str], session: AsyncSession):
        offset = (page - 1) * limit

        count_query = select(func.count()).where(Post.company_id == company_id).where(Post.post_type =="News")
        if early_date:
            count_query = count_query.where(Post.created_at >= early_date)
        if late_date:
            count_query = count_query.where(Post.created_at <= late_date)
        if sport:
            count_query = count_query.where(Post.sport_id.in_(sport))
        if search:
            count_query = count_query.filter(Post.header.ilike(f"%{search}%"))
        query = select(Post).where(Post.company_id == company_id).where(Post.post_type =="News")
        if early_date:
            query = query.where(Post.created_at >= early_date)
        if late_date:
            query = query.where(Post.created_at <= late_date)
        if sport:
            query = query.where(Post.sport_id.in_(sport))
        if search:
            query = query.filter(Post.header.ilike(f"%{search}%"))
        query = query.options(joinedload(Post.company), joinedload(Post.sport)).limit(limit).offset(offset)

        count_result = await session.execute(count_query)
        total_posts = count_result.scalar_one()

        result = await session.execute(query)
        posts = result.scalars().all()

        return posts, total_posts

class Sport(Base):
    __tablename__ = "sport"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    post: Mapped[List["Post"]] = relationship(back_populates="sport")

    @staticmethod
    async def create(name: str, session: AsyncSession) -> "Sport":
        stmt = insert(Sport).values(name = name)
        await session.execute(stmt)
        await session.flush()
        query = select(Sport).where(Sport.name == name)
        result = (await session.execute(query)).scalar_one()
        return result
    
    @staticmethod
    async def get_by_name(name: str, session: AsyncSession):
        query = select(Sport).where(Sport.name == name)
        result = (await session.execute(query)).scalar_one_or_none()
        return result

    @staticmethod
    async def get_by_id(id: int, session: AsyncSession):
        query = select(Sport).where(Sport.id == id)
        result = (await session.execute(query)).scalar_one_or_none()
        return result
    
    @staticmethod
    async def get_all_sport(session: AsyncSession):
        query = select(Sport)
        result = (await session.execute(query)).scalars().all()
        return result
    
    
class News(Post, Base):
    __tablename__ = "news"
    __mapper_args__ = {'polymorphic_identity': 'news'}
    id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    post: Mapped["Post"] = relationship(back_populates="news")

class Forecast(Post):
    __tablename__ = "forecast"
    __mapper_args__ = {'polymorphic_identity': 'forecast'}
    id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
    match_id: Mapped[int] = mapped_column(Integer, nullable=False)
    result: Mapped[str] = mapped_column(String, nullable=False)
    match_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    post: Mapped["Post"] = relationship(back_populates="forecast")

    @staticmethod
    async def create_forecast(company_id: int, sport_id: int, post_type: str, text: str, match_id: int, result: str, header:str, match_date: datetime, session: AsyncSession) -> "Forecast":
        stmt = insert(Post).values(post_type = str(post_type), text = str(text),\
                                        company_id = int(company_id), sport_id = int(sport_id), type = "forecast", header = str(header))
        post_result = await session.execute(stmt)
        await session.flush()

        post_id = post_result.inserted_primary_key[0] #type: ignore

        forecast_stmt = insert(Forecast).values(id=post_id, match_date=match_date, match_id=match_id, result=result)
        await session.execute(forecast_stmt)

        query = select(Forecast).where(Forecast.id == post_id).options(joinedload(Forecast.post), joinedload(Forecast.company), joinedload(Forecast.sport))
        forecast_result = (await session.execute(query)).scalar_one()
        return forecast_result
    
    @staticmethod
    async def get_forecasts(early_date: Optional[datetime], late_date: Optional[datetime], limit: int, page: int, sport: list[int], company_id: int, search: Optional[str], match_id: Optional[int], session: AsyncSession):
        offset = (page - 1) * limit
        query = select(Forecast).where(Forecast.company_id == company_id)
        if match_id:
            query = query.where(Forecast.match_id == match_id)
        if early_date:
            query = query.where(Forecast.created_at >= early_date)
        if late_date:
            query = query.where(Forecast.created_at <= late_date)
        if sport:
            query = query.where(Forecast.sport_id.in_(sport))
        if search:
            query = query.filter(Forecast.header.ilike(f"%{search}%"))
        query = query.options(joinedload(Forecast.post), joinedload(Forecast.company), joinedload(Forecast.sport)).limit(limit).offset(offset)

        result = await session.execute(query)
        posts = result.scalars().all()

        return posts
    
    @staticmethod
    async def get(forecast_id: int, session: AsyncSession):
        stmt = select(Forecast).where(Forecast.id == forecast_id).options(joinedload(Forecast.post), joinedload(Forecast.company), joinedload(Forecast.sport))
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def delete(forecast_id: int, session: AsyncSession):
        stmt = delete(Forecast).where(Forecast.id == forecast_id)
        await session.execute(stmt)
        stm = delete(Post).where(Post.id == forecast_id)
        await session.execute(stm)
        await session.flush()
        return
    
    @staticmethod
    async def update_forecast(forecast_id: int, session: AsyncSession, header: str, text: str, match_id: int, match_date:datetime):
        stmt = update(Post).where(Post.id == forecast_id).values(header = header, text = text)
        stmts = update(Forecast).where(Forecast.id == forecast_id).values(match_id = match_id, match_date=match_date)
        await session.execute(stmt)
        await session.execute(stmts)
        await session.flush()
        query = select(Forecast).where(Forecast.id == forecast_id).options(joinedload(Forecast.post), joinedload(Forecast.company), joinedload(Forecast.sport)).order_by(Post.id.desc()).limit(1)
        result = (await session.execute(query)).scalar_one()
        return result 
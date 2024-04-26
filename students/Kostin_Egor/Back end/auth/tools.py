from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from models.models import Role, User
from auth.auth import auth_backend
from auth.schemas import CreateRole, UserRead

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()

def from_user_to_schemas(user: User):
    user_schema = UserRead(id = user.id, email = user.email, login = user.login, role_id= user.role_id)
    return user_schema

def from_role_to_schema(role: Role):
    role_shcema = CreateRole(id = role.id, name = role.name)
    return role_shcema
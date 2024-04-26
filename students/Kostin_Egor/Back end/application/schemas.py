from pydantic import BaseModel
from fastapi_users import schemas
from datetime import datetime
from enum import Enum
from typing import List
class TypeApplic(Enum):
    OPEN = "Open"
    ATWORK = "Atwork"
    COMLITED = "Complited"
    REJECTED = "Rejected"
    OVERDUE = "Overdue"


class UpdateAplic(BaseModel):
    application_id: int
    new_status: TypeApplic
    id_service: List[int]

class Done_Close_Aplic(BaseModel):
    application_id: int
    new_status: TypeApplic



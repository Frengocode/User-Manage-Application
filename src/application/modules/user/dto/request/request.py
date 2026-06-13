from pydantic import BaseModel, EmailStr
from typing import Optional
from src.application.modules.user.domain.value_objects.role import RoleEnum


class SCreateUserRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    surname: Optional[str] = None
    role: RoleEnum
    password: str

from typing import Optional

from pydantic import BaseModel, EmailStr

from src.application.modules.user.domain.value_objects.role import RoleEnum


class SCreateUserRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    surname: Optional[str] = None
    role: RoleEnum
    password: str



class SGetAuthUserRequest(BaseModel):
    email: EmailStr
    password: str
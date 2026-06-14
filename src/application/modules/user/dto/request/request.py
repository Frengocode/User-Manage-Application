from typing import Optional

from pydantic import BaseModel, EmailStr

from src.application.common.shared.pagination.pagination import BasePagination
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


class SUpdateUserRequest(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None


class SGetUsersRequest(BasePagination):
    pass

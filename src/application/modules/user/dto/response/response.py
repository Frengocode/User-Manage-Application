from pydantic import BaseModel, EmailStr
from typing import Optional
from src.application.modules.user.domain.value_objects.role import RoleEnum


class SUser(BaseModel):
    id: str
    email: EmailStr
    name: Optional[str] = None
    surname: Optional[str] = None
    role: RoleEnum
    created_at: str
    updated_at: str

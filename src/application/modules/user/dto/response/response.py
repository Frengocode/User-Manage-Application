from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.role import RoleEnum


class SUser(BaseModel):
    id: str
    email: EmailStr
    name: Optional[str] = None
    surname: Optional[str] = None
    role: RoleEnum
    created_at: datetime
    updated_at: Optional[str] = None

    @classmethod
    def cls(cls, user: User) -> SUser:
        return cls(
            id=user.id.value,
            email=user.email.value,
            name=user.name.value,
            surname=user.surname.value,
            role=user.role.value,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

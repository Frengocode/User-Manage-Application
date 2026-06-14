from __future__ import annotations

from pydantic import BaseModel

from src.application.modules.user.domain.entities.user import User


class UserCreatedEventPayload(BaseModel):
    id: str
    email: str

    @classmethod
    def cls(cls, user: User) -> UserCreatedEventPayload:
        return cls(id=user.id.value, email=user.email.value)

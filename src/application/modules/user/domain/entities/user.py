from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.application.modules.user.domain.exceptions.exceptions import (
    ExistUserException,
    PermissionDenied,
)
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.is_active import IsActive
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.password import Password
from src.application.modules.user.domain.value_objects.role import Role, RoleEnum
from src.application.modules.user.domain.value_objects.surname import Surname


@dataclass(frozen=True)
class User:
    id: Id
    name: Optional[Name] = None
    surname: Optional[Surname] = None
    email: Email
    password: Password
    is_active: IsActive
    role: Role
    created_at: datetime
    updated_at: Optional[datetime] = None

    def verify_exist_user(self, email: Email) -> None:
        """Verifie's exist user"""
        if self.email == email:
            raise ExistUserException()

    def is_admin(self, role: Role) -> None:
        """Checks is user admin or not"""
        if role != RoleEnum.ADMIN._value:
            raise PermissionDenied()

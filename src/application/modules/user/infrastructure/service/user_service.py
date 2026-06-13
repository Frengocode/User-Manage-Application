import logging
from dataclasses import dataclass
from typing import List, Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.exceptions.exceptions import ExistUserException
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.password import Password
from src.application.modules.user.domain.value_objects.role import Role
from src.application.modules.user.domain.value_objects.surname import Surname
from src.application.modules.user.exceptions.exceptions import ExistUserExceptionHTTP
from src.application.modules.user.interfaces.repository.iuser_repository import (
    IUserRepository,
)
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UserService(IUserService):
    repository: IUserRepository

    async def create_user(
        self,
        id: Id,
        email: Email,
        password: Password,
        role: Role,
        name: Optional[Name] = None,
        surname: Optional[Surname] = None,
    ) -> User: ...

    async def get_exist_user(self, email: Email) -> None:
        """If exist user exists by same email, return 400"""
        user: User = await self.repository.get_user_by_email(email=email)
        try:
            user.verify_exist_user(email=email)
        except ExistUserException as e:
            log.error("This email was used by other user %s", email)
            raise ExistUserExceptionHTTP()

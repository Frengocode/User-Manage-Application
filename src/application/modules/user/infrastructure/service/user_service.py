import logging
from dataclasses import dataclass
from typing import List, Optional

from src.application.common.shared.pagination.pagination import BasePagination
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.exceptions.exceptions import (
    ExistUserException,
    InvalidNameException,
    InvalidSurnameException,
    PermissionDenied,
)
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.password import Password
from src.application.modules.user.domain.value_objects.role import Role
from src.application.modules.user.domain.value_objects.surname import Surname
from src.application.modules.user.exceptions.exceptions import (
    AccessDeniedExceptionHTTP,
    ExistUserExceptionHTTP,
    InvalidNameExceptionHTTP,
    InvalidSurnameExceptionHTTP,
    UserNotFoundExceptionHTTP,
)
from src.application.modules.user.interfaces.repository.iuser_repository import (
    IUserRepository,
)
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger
from src.application.common.shared.auth.interfaces.hash.ihash import IHash

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UserService(IUserService):
    repository: IUserRepository
    hasher: IHash

    async def create_user(
        self,
        email: Email,
        password: Password,
        role: Role,
        name: Optional[Name] = None,
        surname: Optional[Surname] = None,
    ) -> User:

        try:
            # Verifie's exist user by email (If exists)
            await self.get_exist_user(email=email)

            user_data: User = User(
                id=id.generate(),
                name=name,
                surname=surname,
                email=email,
                password=Password(self.hasher.hash_value(password)),
                role=role,
            )
            created_user: User = await self.repository.create_user(user=user_data)

            return created_user

        except InvalidNameException:
            log.error("Invalid name, name can't have 10 words %s", name)
            raise InvalidNameExceptionHTTP()

        except InvalidSurnameException:
            log.error("Surname can not be more than 10 words %s", surname)
            raise InvalidSurnameExceptionHTTP()

    async def get_user(self, id: Id) -> Optional[User]:
        """Get's user or returns 404"""
        user: User | None = await self.repository.get_user(id=id)
        if not user:
            log.error("User not found %s", id)
            raise UserNotFoundExceptionHTTP()
        return user

    async def get_users(
        self, user: User, pagination: BasePagination
    ) -> Optional[List[User]]:
        """Get's users (only for admins)"""

        try:
            user.is_admin(user.role)
            return await self.repository.get_users(pagination=pagination)
        except PermissionDenied:
            log.error(
                "Users can't get, list of users (Access only for admins) %s", user.role
            )
            raise AccessDeniedExceptionHTTP()

    async def get_exist_user(self, email: Email) -> None:
        """If exist user exists by same email, return 400"""
        user: User = await self.repository.get_user_by_email(email=email)
        try:
            user.verify_exist_user(email=email)
        except ExistUserException:
            log.error("This email was used by other user %s", email)
            raise ExistUserExceptionHTTP()

    async def activate_user(self, user: User) -> User:
        """Activates user"""
        return await self.repository.update_status(user=user)

    async def delete_user(self, user: User) -> User:
        """Deletes user (only for admin)"""
        try:
            user.is_admin(role=Role(user.role))
            return await self.repository.delete_user(user_id=Id(user.id))
        except PermissionDenied:
            log.error("Admins only can delete users %s", user.role)
            raise AccessDeniedExceptionHTTP()

    async def update_user(
        self,
        user_id: Id,
        name: Optional[Name] = None,
        surname: Optional[Surname] = None,
    ) -> User:
        """Updates user"""
        return await self.repository.update_user(
            user_id=user_id, name=name, surname=surname
        )

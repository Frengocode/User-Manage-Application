from typing import List, Optional, Protocol

from src.application.common.shared.pagination.pagination import BasePagination
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.password import Password
from src.application.modules.user.domain.value_objects.role import Role
from src.application.modules.user.domain.value_objects.surname import Surname


class IUserService(Protocol):

    async def create_user(
        self,
        id: Id,
        email: Email,
        password: Password,
        role: Role,
        name: Optional[Name] = None,
        surname: Optional[Surname] = None,
    ) -> User: ...

    async def get_user(self, id: Id) -> Optional[User]: ...

    """ Get's user or returns 404 """

    async def get_exist_user(self, email: Email) -> None: ...

    """ Get's exist user by email, if exists, returns 404 """

    async def get_users(self, user: User, pagination: BasePagination) -> List[User]: ...

    """ Get's users, can use only users with Admin role """

    async def activate_user(self, user: User) -> User: ...

    """ Activate's user """

    async def delete_user(self, user: User) -> User: ...

    """ Delete's user """

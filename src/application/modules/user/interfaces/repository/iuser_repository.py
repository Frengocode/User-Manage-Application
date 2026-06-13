from abc import ABC, abstractmethod
from typing import List, Optional

from src.application.common.shared.pagination.pagination import BasePagination
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.surname import Surname
from src.application.modules.user.domain.value_objects.id import Id


class IUserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: User) -> User: ...

    @abstractmethod
    async def get_user(self, user_id: Id) -> User | None: ...

    @abstractmethod
    async def get_users(self, pagination: BasePagination) -> List[User]: ...

    @abstractmethod
    async def get_user_by_email(self, email: Email) -> User | None: ...

    @abstractmethod
    async def update_user(
        self,
        user_id: Id,
        name: Optional[Name] = None,
        surname: Optional[Surname] = Name,
    ) -> User: ...

    @abstractmethod
    async def update_status(self, user: User) -> User | None: ...

    @abstractmethod
    async def delete_user(self, user_id: Id) -> None: ...

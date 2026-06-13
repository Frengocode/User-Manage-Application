from abc import ABC, abstractmethod

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id


class IUserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: User) -> User: ...

    @abstractmethod
    async def get_user(self, id: Id) -> User | None: ...

    @abstractmethod
    async def get_user_by_email(self, email: Email) -> User | None: ...

    @abstractmethod
    async def update_user(self, user: User) -> User | None: ...

    @abstractmethod
    async def update_status(self, user: User) -> User | None: ...

    @abstractmethod
    async def delete_user(self, id: Id) -> None: ...

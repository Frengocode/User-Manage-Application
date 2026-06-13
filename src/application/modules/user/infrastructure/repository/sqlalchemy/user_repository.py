from dataclasses import dataclass

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.is_active import IsActive
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.role import Role
from src.application.modules.user.domain.value_objects.surname import Surname
from src.application.modules.user.infrastructure.models.sqlalchemy.user import (
    SQLAlchemyUser,
)
from src.application.modules.user.interfaces.repository.iuser_repository import (
    IUserRepository,
)


@dataclass(frozen=True)
class SQLALchemyUserRepository(IUserRepository):
    session: AsyncSession
    model = SQLAlchemyUser

    async def create_user(self, user: User) -> User:
        creating_user: SQLAlchemyUser = SQLAlchemyUser(
            id=user.id,
            email=user.email,
            password=user.password,
            name=user.name,
            surname=user.surname,
        )
        self.session.add(creating_user)
        await self.session.commit()

        return User(
            id=Id(creating_user.id),
            email=Email(creating_user.email),
            name=Name(creating_user.name),
            surname=Surname(creating_user.surname),
            role=Role(creating_user.role),
            is_active=IsActive(creating_user.is_active),
            created_at=creating_user.created_at,
            updated_at=creating_user.updated_at,
        )

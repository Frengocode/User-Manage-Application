from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import List, Optional, Union

from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.shared.pagination.pagination import BasePagination
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.domain.value_objects.is_active import IsActive
from src.application.modules.user.domain.value_objects.name import Name
from src.application.modules.user.domain.value_objects.password import Password
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

    def _model_to_domain(
        self,
        model: Union[List[SQLAlchemyUser], SQLAlchemyUser],
    ) -> Union[List[User], User]:

        if model is not None:
            if isinstance(model, list):
                return [
                    User(
                        id=Id(user.id),
                        name=Name(user.name),
                        surname=Surname(user.surname),
                        email=Email(user.email),
                        role=Role(user.role),
                        password=Password(user.password),
                        is_active=IsActive(user.is_active),
                        created_at=user.created_at,
                        updated_at=user.updated_at,
                    )
                    for user in model
                ]

            return User(
                id=Id(model.id),
                name=Name(model.name),
                surname=Surname(model.surname),
                email=Email(model.email),
                role=Role(model.role),
                password=Password(model.password),
                is_active=IsActive(model.is_active),
                created_at=model.created_at,
                updated_at=model.updated_at,
            )

    async def create_user(self, user: User) -> User:
        creating_user: SQLAlchemyUser = self.model(
            id=user.id.value,
            email=user.email.value,
            password=user.password.value,
            name=user.name.value,
            role=user.role.value,
            surname=user.surname.value,
        )
        self.session.add(creating_user)
        await self.session.commit()
        await self.session.refresh(creating_user)

        # Dumps orm object into domain model object
        return self._model_to_domain(creating_user)

    async def get_user(self, user_id: Id) -> User | None:
        """Get's user by Id"""

        stmt: Select[SQLAlchemyUser] = select(self.model).filter_by(id=user_id.value)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        user: SQLAlchemyUser = result.scalars().first()

        # Dumps orm object into domain model object
        return self._model_to_domain(user)

    async def get_users(self, pagination: BasePagination) -> List[User]:
        """Get's users"""
        stmt: Select[SQLAlchemyUser] = (
            select(self.model).offset(pagination.offset).limit(pagination.limit)
        )
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        users: List[SQLAlchemyUser] = result.scalars().all()
        return self._model_to_domain(users)

    async def get_user_by_email(self, email: Email) -> User | None:
        """Get's user by email"""

        stmt: Select[SQLAlchemyUser] = select(self.model).filter_by(email=email.value)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        user: SQLAlchemyUser = result.scalars().first()

        # Dumps orm object into domain model object
        return self._model_to_domain(user)

    async def update_status(self, user: User) -> User:
        """Updates user status"""
        stmt: Select[SQLAlchemyUser] = select(self.model).filter_by(id=user.id.value)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        updating_user: SQLAlchemyUser = result.scalars().first()

        updating_user.is_active = True
        await self.session.commit()
        await self.session.refresh(updating_user)

        # Dumps orm object into domain model object
        return self._model_to_domain(updating_user)

    async def update_user(
        self,
        user_id: Id,
        name: Optional[Name] = None,
        surname: Optional[Surname] = None,
    ) -> User:

        stmt = select(self.model).filter_by(id=user_id.value)
        result = await self.session.execute(stmt)

        updating_user = result.scalars().first()

        if name is not None:
            updating_user.name = name.value

        if surname is not None:
            updating_user.surname = surname.value

        await self.session.commit()
        await self.session.refresh(updating_user)

        return self._model_to_domain(updating_user)

    async def delete_user(self, user_id: Id) -> Optional[User]:
        """Delete user"""
        stmt: Select[SQLAlchemyUser] = select(self.model).filter_by(id=user_id.value)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        user: SQLAlchemyUser = result.scalars().first()
        if user is not None:
            await self.session.delete(user)
            await self.session.commit()

            # Dumps orm object into domain model object
            user.id = user_id.value
            return self._model_to_domain(user)

    async def get_not_activated_users(self) -> List[User]:
        time_threshold = datetime.now(timezone.utc) - timedelta(hours=1)
        stmt: Select[SQLAlchemyUser] = select(self.model).filter(
            self.model.created_at <= time_threshold, self.model.is_active == False
        )
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        users: List[SQLAlchemyUser] = result.scalars().all()

        # Dumps orm object into domain model object
        return self._model_to_domain(users)

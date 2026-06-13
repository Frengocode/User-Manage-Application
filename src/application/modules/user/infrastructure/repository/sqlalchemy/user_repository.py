from dataclasses import dataclass
from typing import List, Union

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
        self, model: Union[List[SQLAlchemyUser], SQLAlchemyUser]
    ) -> Union[List[User], User]:
        """Dumps orm objects or object into domain model object"""

        # Cheking data type of orm object
        if model is not None:
            if isinstance(model, list):
                for user in model:
                    return User(
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
            id=user.id,
            email=user.email,
            password=user.password,
            name=user.name,
            role=user.role,
            surname=user.surname,
        )
        self.session.add(creating_user)
        await self.session.commit()

        # Dumps orm object into domain model object
        return self._model_to_domain(creating_user)

    async def get_user(self, user_id: Id) -> User | None:
        """Get's user by Id"""

        stmt: Select[SQLAlchemyUser] = select(self.model).where(id=user_id)
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

        stmt: Select[SQLAlchemyUser] = select(self.model).where(id=email)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        user: SQLAlchemyUser = result.scalars().first()

        # Dumps orm object into domain model object
        return self._model_to_domain(user)

    async def update_status(self, user: User) -> User:
        """Updates user status"""
        stmt: Select[SQLAlchemyUser] = select(self.model).where(id=user.id)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        updating_user: SQLAlchemyUser = result.scalars().first()

        updating_user.is_active = True
        await self.session.commit()
        await self.session.refresh(updating_user)

        # Dumps orm object into domain model object
        return self._model_to_domain(updating_user)

    async def update_user(self, user: User) -> User:
        """Update user"""
        stmt: Select[SQLAlchemyUser] = select(self.model).where(id=user.id)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        updating_user: SQLAlchemyUser = result.scalars().first()

        for name, value in user.__dict__:
            setattr(name, value, updating_user)
        await self.session.commit()
        await self.session.refresh(updating_user)

        # Dumps orm object into domain model object
        return self._model_to_domain(updating_user)

    async def delete_user(self, user_id: Id) -> User:
        """Delete user"""
        stmt: Select[SQLAlchemyUser] = select(self.model).where(id=user_id)
        result: Result[SQLAlchemyUser] = await self.session.execute(stmt)
        user: SQLAlchemyUser = result.scalars().first()
        await self.session.delete(user)
        await self.session.commit()
        await self.session.refresh(user)

        # Dumps orm object into domain model object
        return self._model_to_domain(user)

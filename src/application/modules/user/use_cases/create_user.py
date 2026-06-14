import logging
from dataclasses import dataclass

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects import (email, id, name,
                                                               password, role,
                                                               surname)
from src.application.modules.user.dto.request.request import SCreateUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.interfaces.events.payload.user_created_payload import \
    UserCreatedEventPayload
from src.application.modules.user.interfaces.events.user_created_event import \
    IUserCreatedEvent
from src.application.modules.user.interfaces.services.iuser_service import \
    IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class CreateUserUseCase:
    service: IUserService
    event: IUserCreatedEvent

    async def execute(self, request: SCreateUserRequest) -> SUser:

        created_user: User = await self.service.create_user(
            email=email.Email(request.email),
            password=password.Password(request.password),
            role=role.Role(request.role.value),
            name=name.Name.create(request.name),
            surname=surname.Surname.create(request.surname),
        )

        event_payload: UserCreatedEventPayload = UserCreatedEventPayload.cls(
            created_user
        )
        await self.event.publish_event(event_payload)
        log.info("User created successfully %s", created_user.id)
        return SUser.cls(created_user)

import logging
from dataclasses import dataclass
from typing import Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects import id, name, surname
from src.application.modules.user.dto.request.request import SUpdateUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UpdateUserUseCase:
    service: IUserService

    async def execute(
        self, user_id: int, request: SUpdateUserRequest
    ) -> Optional[SUser]:

        # Getting user for verify existing
        await self.service.get_user(id=id.Id(user_id))

        updated_user: User = await self.service.update_user(
            user_id=id.Id(user_id),
            name=name.Name(request.name),
            surname=surname.Surname(request.surname),
        )
        log.info("User was successfully updated %s", user_id)
        return SUser.cls(updated_user)

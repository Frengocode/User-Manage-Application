from dataclasses import dataclass
from typing import Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.dto.request.request import SGetAuthUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.modules.user.interfaces.use_cases.iget_auth_user import (
    IGetAuthUserUseCase,
)
from src.application.modules.user.exceptions.exceptions import InvalidDataExceptionHTTP
from src.application.modules.user.domain.exceptions.exceptions import (
    InvalidPasswordException,
)
from src.application.modules.user.domain.value_objects.password import Password
import logging
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class GetAuthUserUseCase(IGetAuthUserUseCase):
    service: IUserService

    async def execute(self, request: SGetAuthUserRequest) -> Optional[SUser]:
        try:
            user: Optional[User] = await self.service.get_user_by_email(
                email=Email(request.email)
            )
            user.password.verify_password(password=Password(request.password))
        except InvalidPasswordException:
            log.info("Invalid email or password %s", request.email)
            raise InvalidDataExceptionHTTP()

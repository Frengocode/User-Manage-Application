import logging
from dataclasses import dataclass
from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm

from src.application.common.shared.auth.interfaces.token.refresh_token_generator import (
    IRefreshTokenGenerator,
)
from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.modules.auth.dto.responses.response import (
    SLogin,
)
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects import email, password
from src.application.modules.user.interfaces.use_cases.iget_auth_user import (
    IGetAuthUserUseCase,
)
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class LoginUseCase:
    get_auth_user_use_case: IGetAuthUserUseCase
    token_generator: ITokenGenerator
    refresh_token_generator: IRefreshTokenGenerator

    async def execute(self, form: OAuth2PasswordRequestForm) -> Optional[SLogin]:

        user: Optional[User] = await self.get_auth_user_use_case.execute(
            email=email.Email(form.username), password=password.Password(form.password)
        )
        generated_access_token: str = self.token_generator.create_token(
            data={"sub": user.id.value}
        )
        generated_refresh_token: str = (
            self.refresh_token_generator.create_refresh_token(
                data={"sub": user.id.value}
            )
        )

        log.info("Access token was successfully generated %s ", user.id.value)
        return SLogin(
            access_token=generated_access_token, refresh_token=generated_refresh_token
        )

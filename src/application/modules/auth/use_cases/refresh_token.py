import logging
from dataclasses import dataclass
from typing import Any, Dict

from jose import jwt

from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.common.shared.config.config import settings
from src.application.modules.auth.dto.responses.response import SAccessToken
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class RefreshTokenUseCase:
    token_generator: ITokenGenerator

    async def execute(self, token: str) -> SAccessToken:
        payload: Dict[Any, Any] = jwt.decode(
            token=token,
            key=settings.auth.JWT_SECRET_KEY.get_secret_value(),
            algorithms=settings.auth.JWT_ALGORITHM,
        )

        user_id: str = payload["sub"]
        access_token: str = self.token_generator.create_token(data={"sub": user_id})
        log.info("Token was successfuly generated for %s", user_id)
        return SAccessToken(access_token=access_token)

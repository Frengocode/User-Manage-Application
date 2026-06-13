from datetime import datetime, timedelta
from jose import jwt

from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.common.shared.config.config import settings

from datetime import datetime, timedelta

from jose import jwt

from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.common.shared.config.config import settings


class RefreshTokenGenerator(ITokenGenerator):

    @staticmethod
    def create_refresh_token(data: dict) -> str:
        to_encode = data.copy()

        if "sub" in to_encode:
            to_encode["sub"] = str(to_encode["sub"])

        expire = datetime.utcnow() + timedelta(
            days=settings.auth.JWT_REFRESH_TOKEN_EXPIRE_DAYS
        )

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(
            to_encode,
            settings.auth.JWT_SECRET_KEY.get_secret_value(),
            algorithm=settings.auth.JWT_ALGORITHM,
        )

        return encoded_jwt

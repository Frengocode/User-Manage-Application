from datetime import datetime, timedelta

from jose import jwt

from src.application.common.shared.auth.interfaces.token.token_generator import \
    ITokenGenerator
from src.application.common.shared.config.config import settings


class AccessTokenGenerator(ITokenGenerator):

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()

        if "sub" in to_encode:
            to_encode["sub"] = str(to_encode["sub"])

        else:
            expire = datetime.utcnow() + timedelta(
                days=settings.auth.JWT_ACCESS_TOKEN_EXPIRE_days
            )

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(
            to_encode,
            settings.auth.JWT_SECRET_KEY.get_secret_value(),
            algorithm=settings.auth.JWT_ALGORITHM,
        )
        return encoded_jwt

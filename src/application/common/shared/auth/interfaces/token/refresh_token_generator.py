from typing import Protocol


class IRefreshTokenGenerator(Protocol):
    def generate_refresh_token(self, token: str) -> str: ...

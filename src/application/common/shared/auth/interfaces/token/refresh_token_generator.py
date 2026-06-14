from typing import Protocol


class IRefreshTokenGenerator(Protocol):
    def create_refresh_token(self, data: dict) -> str: ...

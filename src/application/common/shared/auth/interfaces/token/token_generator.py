from typing import Protocol


class ITokenGenerator(Protocol):
    def create_token(data: dict) -> str: ...

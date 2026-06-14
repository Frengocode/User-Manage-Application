from typing import Protocol


class ITokenGenerator(Protocol):
    def create_token(self, data: dict) -> str: ...

    """ Generates token """

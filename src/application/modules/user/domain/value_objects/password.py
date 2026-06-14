from __future__ import annotations
from dataclasses import dataclass
from src.application.modules.user.domain.exceptions.exceptions import (
    InvalidPasswordException,
)


@dataclass(frozen=True)
class Password:
    value: str

    def verify_password(self, password: Password) -> None:
        if self.value != password:
            raise InvalidPasswordException()

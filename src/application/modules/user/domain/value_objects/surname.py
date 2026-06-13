from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from application.modules.user.domain.exceptions.exceptions import (
    InvalidSurnameException,
)


@dataclass(frozen=True)
class Surname:
    value: Optional[str] = None

    @classmethod
    def create(cls, surname: Optional[str]) -> Surname:
        if surname is not None and len(surname) > 10:
            return Surname(value=surname)
        raise InvalidSurnameException()

    def update_surname(self, new_surname: Optional[str]) -> Surname:
        if len(new_surname) > 10:
            raise InvalidSurnameException()

        if not new_surname.strip():
            return self
        return Surname(value=new_surname)

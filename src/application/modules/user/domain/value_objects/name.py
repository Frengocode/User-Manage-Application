from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from application.modules.user.domain.exceptions.exceptions import \
    InvalidNameException


@dataclass(frozen=True)
class Name:
    value: Optional[str] = None

    @classmethod
    def create(cls, name: Optional[str]) -> Name:
        if name is not None and len(name) > 10:
            return Name(value=name)
        raise InvalidNameException()

    def update_name(self, new_name: Optional[str]) -> Name:
        if len(new_name) > 10:
            raise InvalidNameException()

        if not new_name.strip():
            return self
        return Name(value=new_name)

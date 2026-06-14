from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Surname:
    value: Optional[str] = None

    @classmethod
    def create(cls, surname: Optional[str]) -> Surname:
        if surname is not None:
            return Surname(value=surname)

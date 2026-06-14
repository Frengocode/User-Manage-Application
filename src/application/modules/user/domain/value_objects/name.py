from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Name:
    value: Optional[str] = None

    @classmethod
    def create(cls, name: Optional[str]) -> Name:
        if name is not None:
            return Name(value=name)

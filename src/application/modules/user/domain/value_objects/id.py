from __future__ import annotations

import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class Id:
    value: str

    @staticmethod
    def generate() -> Id:
        return Id(str(uuid.uuid4()))

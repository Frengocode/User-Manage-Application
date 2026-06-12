from dataclasses import dataclass
from enum import Enum


class RoleEnum(Enum):
    ADMIN: str = "admin"
    USER: str = "user"


@dataclass(frozen=True)
class Role:
    value: str

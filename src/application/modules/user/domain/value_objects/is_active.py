from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IsActive:
    value: bool

    def update_status(self) -> IsActive:
        return IsActive(value=True)

from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    value: str

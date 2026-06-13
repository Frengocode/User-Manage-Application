from typing import Protocol


class IHash(Protocol):

    def hash_value(self, value: str) -> str: ...

    """ Hashes value """

    def verify_hash(self, secret: str, hash: str) -> bool: ...

    """ Verifie's hash """

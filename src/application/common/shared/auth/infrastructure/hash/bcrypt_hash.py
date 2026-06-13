import base64
import hashlib
from dataclasses import dataclass

import bcrypt
from passlib.context import CryptContext

from src.application.common.shared.auth.interfaces.hash.ihash import IHash


@dataclass(frozen=True)
class BcryptHash(IHash):
    crypt_context = CryptContext(schemes=["bcrypt"])

    def hash_value(value: str) -> str:
        prehashed = hashlib.sha256(value.encode("utf-8")).digest()

        encoded = base64.b64encode(prehashed)

        hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

        return hashed.decode("utf-8")

    def verify_hash(secret: str, hash: str) -> bool:
        prehashed = hashlib.sha256(secret.encode("utf-8")).digest()
        encoded = base64.b64encode(prehashed)

        return bcrypt.checkpw(encoded, hash.encode("utf-8"))

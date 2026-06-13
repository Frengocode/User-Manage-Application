from pydantic import BaseModel


class UserCreatedEventPayload(BaseModel):
    id: str
    email: str

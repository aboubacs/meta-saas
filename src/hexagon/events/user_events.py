from pydantic import BaseModel


class UserEvent(BaseModel):
    pass


class UserRegistered(UserEvent):
    id: str
    email: str
    instance_id: str

from pydantic import BaseModel


class UserRegistered(BaseModel):
    user_id: str
    email: str
    instance_id: str

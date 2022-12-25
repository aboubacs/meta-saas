from pydantic import BaseModel, EmailStr


class RegisterUserCommand(BaseModel):
    instance_id: str
    id: str
    email: EmailStr

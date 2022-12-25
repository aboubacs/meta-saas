from pydantic import BaseModel, EmailStr, SecretStr


class RegisterUserCommand(BaseModel):
    instance_id: str
    id: str
    email: EmailStr
    password: SecretStr

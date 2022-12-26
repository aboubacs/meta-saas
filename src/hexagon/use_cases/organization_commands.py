from pydantic import BaseModel


class CreateOrganizationCommand(BaseModel):
    id: str
    name: str

from pydantic import BaseModel


class OrganizationCreated(BaseModel):
    id: str
    name: str
    owner_user_id: str
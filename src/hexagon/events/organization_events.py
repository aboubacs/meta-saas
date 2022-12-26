from pydantic import BaseModel


class OrganizationCreated(BaseModel):
    organization_id: str
    instance_id: str
    name: str
    owner_user_id: str
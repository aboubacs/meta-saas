from pydantic import BaseModel


class InstanceCreated(BaseModel):
    instance_id: str
    name: str

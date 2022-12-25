from pydantic import BaseModel


class CreateInstanceCommand(BaseModel):
    id: str
    name: str

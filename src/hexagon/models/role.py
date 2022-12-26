from dataclasses import dataclass


@dataclass
class Role:
    id: str
    name: str
    instance_id: str
    description: str = ""
